"""
GTM Message Generator — produces 3 outreach message variants (pain_first, roi_first, curiosity_first)
from a GTM brief and buyer persona context.
"""

import os
import json
import uuid
from typing import List, Dict, Any, Optional
from collections import Counter

from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger

logger = get_logger('mirofish.gtm_message_generator')

_MOCK_PATH = os.path.join(
    os.path.dirname(__file__), '../../../mock_data/gtm_messages.json'
)

ANGLES = ['pain_first', 'roi_first', 'curiosity_first']

SYSTEM_PROMPT = """You are a senior B2B cold outreach copywriter specializing in founder-led sales.
Generate concise, founder-style outreach messages for cold outbound email and LinkedIn.

Rules:
- Max 80 words per message body
- No buzzwords or corporate marketing language
- Sound like a real person, not a marketing department
- Use {first_name} as the only personalization token
- Subject line: max 10 words, no clickbait
- Make each angle feel genuinely different in opening style and value framing
- Return ONLY a valid JSON array of 3 objects, no markdown

Each object must have these fields:
{
  "id": "<unique id like msg_pain_001>",
  "angle": "<pain_first | roi_first | curiosity_first>",
  "subject_line": "<compelling subject line>",
  "body": "<80-word max message with {first_name} token>",
  "target_persona_reasoning": "<one sentence on who this angle works best for>"
}"""


def _build_user_prompt(brief: Any, personas: list) -> str:
    # Summarize the most common message angle preferences from personas
    angles = [p.get('likely_message_angle', '') for p in personas if p.get('likely_message_angle')]
    angle_dist = Counter(angles)
    angle_summary = ', '.join(f"{k}: {v}" for k, v in angle_dist.most_common())

    competitors = ', '.join(brief.competitors) if brief.competitors else 'not specified'

    return f"""GTM Brief:
Product: {brief.product_name} — {brief.product_description}
ICP: {brief.icp}
Pricing: {brief.pricing_model}
Target Market: {brief.target_market}
Sales Channel: {brief.sales_channel}
Main Pain Point: {brief.pain_point}
GTM Goal: {brief.gtm_goal}
Competitors: {competitors}

Persona angle preferences (from {len(personas)} buyer personas): {angle_summary}

Generate exactly 3 outreach messages — one pain_first, one roi_first, one curiosity_first.
Tailor to the specific product and ICP above.
Make each genuinely different in opening style and value framing."""


def _validate(msg: dict) -> bool:
    required = ['id', 'angle', 'subject_line', 'body', 'target_persona_reasoning']
    return all(f in msg and msg[f] for f in required) and msg.get('angle') in ANGLES


def _load_mock() -> List[Dict]:
    try:
        with open(_MOCK_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Could not load mock messages: {e}")
        return []


class GTMMessageGenerator:

    def __init__(self):
        self._llm: Optional[LLMClient] = None

    def _get_llm(self) -> LLMClient:
        if self._llm is None:
            self._llm = LLMClient()
        return self._llm

    def generate(self, brief: Any, personas: list) -> List[Dict]:
        """
        Generate 3 outreach message variants from a GTMBrief.
        Falls back to mock data on any error.
        """
        try:
            messages_prompt = [
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': _build_user_prompt(brief, personas)},
            ]
            result = self._get_llm().chat_json(messages_prompt, temperature=0.7, max_tokens=2000)

            if isinstance(result, list):
                msgs = result
            elif isinstance(result, dict):
                msgs = next((v for v in result.values() if isinstance(v, list)), [])
            else:
                raise ValueError(f"Unexpected response type: {type(result)}")

            valid = [m for m in msgs if _validate(m)]
            if len(valid) < 3:
                logger.warning(f"Only {len(valid)} valid messages from LLM, using mock fallback")
                return _load_mock()

            # Ensure unique ids
            for m in valid:
                if not m.get('id'):
                    m['id'] = f"msg_{m['angle']}_{str(uuid.uuid4())[:6]}"

            logger.info("Generated 3 outreach message variants via LLM")
            return valid[:3]

        except Exception as e:
            logger.warning(f"Message generation via LLM failed ({e}), using mock fallback")
            return _load_mock()
