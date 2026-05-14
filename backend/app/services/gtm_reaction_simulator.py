"""
GTM Reaction Simulator — simulates buyer reactions to outreach messages.
For each of 3 messages × 12 personas = 36 reactions total.
Makes 3 LLM calls (one per message), each returning 12 persona reactions.
Falls back to mock data if any call fails.
"""

import os
import json
import uuid
from typing import List, Dict, Any, Optional

from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger

logger = get_logger('mirofish.gtm_reaction_simulator')

_MOCK_PATH = os.path.join(
    os.path.dirname(__file__), '../../../mock_data/gtm_reactions.json'
)

SYSTEM_PROMPT = """You are a B2B buyer simulation engine.
For each buyer persona, generate a realistic reaction to the outreach message below.

Rules:
- Base scores on the persona's goals, pain points, objections, skepticism level, and communication style
- Vary scores meaningfully — do NOT give all personas similar scores
- Skeptical or finance buyers should score lower; early-stage operators and founders higher for pain/urgency messages
- interest_score is primary; drive verdict from it (≥7 = positive, 4-6.9 = neutral, <4 = negative)
- simulated_reply should sound like a real person — concise, authentic, includes their likely skepticism or enthusiasm
- Return ONLY a valid JSON array, no markdown

Each reaction object must have these exact fields:
{
  "id": "<unique id>",
  "persona_id": "<from persona list>",
  "message_id": "<from message>",
  "interest_score": <0.0-10.0>,
  "clarity_score": <0.0-10.0>,
  "trust_score": <0.0-10.0>,
  "urgency_score": <0.0-10.0>,
  "objection": "<specific objection this persona would raise>",
  "buying_trigger": "<what would make them actually move forward>",
  "preferred_cta": "<their preferred next step>",
  "risk_signal": "<one concern or risk they perceive>",
  "simulated_reply": "<one sentence they'd actually write back>",
  "verdict": "<positive | neutral | negative>"
}"""


def _build_reaction_prompt(message: dict, personas: list) -> str:
    persona_list = []
    for p in personas:
        persona_list.append(
            f"- {p['id']}: {p['name']}, {p['title']} at {p['company_type']} ({p['company_stage']}). "
            f"Goal: {p['primary_goal']}. "
            f"Likely message angle: {p.get('likely_message_angle', 'unknown')}. "
            f"Skepticism: {p.get('skepticism_level', 3)}/5. "
            f"Main objection: {p.get('objections', ['unknown'])[0] if p.get('objections') else 'unknown'}."
        )
    personas_text = '\n'.join(persona_list)

    return f"""Outreach Message:
Angle: {message['angle']}
Subject: {message['subject_line']}
Body: {message['body']}

Buyer Personas ({len(personas)} total):
{personas_text}

Generate one reaction object per persona (total: {len(personas)} reactions).
Set message_id to "{message['id']}" for all reactions.
Vary scores based on how well this message angle matches each persona's priorities."""


def _compute_verdict(interest_score: float) -> str:
    if interest_score >= 7.0:
        return 'positive'
    if interest_score >= 4.0:
        return 'neutral'
    return 'negative'


def _validate_reaction(r: dict) -> bool:
    required = [
        'id', 'persona_id', 'message_id', 'interest_score', 'clarity_score',
        'trust_score', 'urgency_score', 'objection', 'buying_trigger',
        'preferred_cta', 'risk_signal', 'simulated_reply', 'verdict',
    ]
    if not all(f in r for f in required):
        return False
    for score_field in ('interest_score', 'clarity_score', 'trust_score', 'urgency_score'):
        try:
            val = float(r[score_field])
            if not (0 <= val <= 10):
                return False
        except (TypeError, ValueError):
            return False
    return True


def _load_mock_reactions() -> List[Dict]:
    try:
        with open(_MOCK_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('reactions', [])
    except Exception as e:
        logger.error(f"Could not load mock reactions: {e}")
        return []


class GTMReactionSimulator:

    def __init__(self):
        self._llm: Optional[LLMClient] = None

    def _get_llm(self) -> LLMClient:
        if self._llm is None:
            self._llm = LLMClient()
        return self._llm

    def simulate_all(self, messages: list, personas: list) -> List[Dict]:
        """
        Simulate reactions for all messages × personas.
        Makes one LLM call per message; falls back to mock for any failed call.
        Returns a flat list of all reactions.
        """
        all_reactions = []
        mock_needed = False

        for message in messages:
            try:
                reactions = self._simulate_for_message(message, personas)
                if not reactions:
                    mock_needed = True
                    break
                all_reactions.extend(reactions)
            except Exception as e:
                logger.warning(f"Reaction simulation failed for message {message.get('id')}: {e}")
                mock_needed = True
                break

        if mock_needed or len(all_reactions) < len(messages) * len(personas) * 0.5:
            logger.warning("Using mock fallback for all reactions")
            return _load_mock_reactions()

        logger.info(f"Simulated {len(all_reactions)} buyer reactions via LLM")
        return all_reactions

    def _simulate_for_message(self, message: dict, personas: list) -> List[Dict]:
        """Single LLM call: 1 message × N personas → N reactions."""
        prompt_messages = [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': _build_reaction_prompt(message, personas)},
        ]
        result = self._get_llm().chat_json(prompt_messages, temperature=0.6, max_tokens=6000)

        if isinstance(result, list):
            reactions = result
        elif isinstance(result, dict):
            reactions = next((v for v in result.values() if isinstance(v, list)), [])
        else:
            raise ValueError(f"Unexpected response type: {type(result)}")

        # Validate, fix, and ensure required fields
        valid = []
        for r in reactions:
            if not isinstance(r, dict):
                continue
            # Coerce scores to float
            for score in ('interest_score', 'clarity_score', 'trust_score', 'urgency_score'):
                try:
                    r[score] = float(r.get(score, 5.0))
                    r[score] = max(0.0, min(10.0, r[score]))
                except (TypeError, ValueError):
                    r[score] = 5.0
            # Ensure verdict matches interest_score
            r['verdict'] = _compute_verdict(r['interest_score'])
            # Ensure unique id
            if not r.get('id'):
                r['id'] = f"rxn_{r.get('persona_id', 'unknown')}_{message['id']}_{str(uuid.uuid4())[:6]}"
            # Ensure message_id is set
            r['message_id'] = message['id']
            if _validate_reaction(r):
                valid.append(r)

        if len(valid) < len(personas) * 0.5:
            logger.warning(f"Only {len(valid)}/{len(personas)} valid reactions for message {message['id']}")
            return []

        return valid
