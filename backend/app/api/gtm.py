"""
GTM Simulation Lab — API endpoints for GTM brief submission, preview, and persona generation.
"""

import os
import json
from flask import request, jsonify
from . import gtm_bp
from ..models.gtm_brief import GTMBriefManager
from ..utils.logger import get_logger

logger = get_logger('mirofish.api.gtm')

_MOCK_PREVIEW_PATH = os.path.join(
    os.path.dirname(__file__), '../../../../mock_data/gtm_preview.json'
)


def _load_mock_preview():
    """Load the static mock preview data from backend/mock_data/gtm_preview.json."""
    try:
        with open(_MOCK_PREVIEW_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.warning(f"Could not load mock preview data: {e}")
        return {"personas": [], "message_angle_teasers": []}


def _personas_path(brief_id: str) -> str:
    from ..config import Config
    return os.path.join(Config.UPLOAD_FOLDER, 'gtm_briefs', brief_id, 'personas.json')


def _save_personas(brief_id: str, personas: list):
    path = _personas_path(brief_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(personas, f, ensure_ascii=False, indent=2)


def _load_cached_personas(brief_id: str):
    path = _personas_path(brief_id)
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


@gtm_bp.route('/brief', methods=['POST'])
def submit_brief():
    """
    POST /api/gtm/brief

    Accepts a GTM brief payload, validates it, persists it, and returns
    the brief_id for downstream simulation steps.
    """
    data = request.get_json(silent=True) or {}

    errors = GTMBriefManager.validate(data)
    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    try:
        brief = GTMBriefManager.create_brief(data)
        logger.info(f"GTM brief created: {brief.brief_id}")
        return jsonify({
            'success': True,
            'data': {
                'brief_id': brief.brief_id,
                'brief': brief.to_dict(),
            }
        })
    except Exception as e:
        logger.error(f"Failed to create GTM brief: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@gtm_bp.route('/brief/<brief_id>', methods=['GET'])
def get_brief(brief_id: str):
    """GET /api/gtm/brief/<brief_id> — retrieve a stored GTM brief."""
    brief = GTMBriefManager.get_brief(brief_id)
    if not brief:
        return jsonify({'success': False, 'error': f'Brief not found: {brief_id}'}), 404
    return jsonify({'success': True, 'data': brief.to_dict()})


@gtm_bp.route('/brief/<brief_id>/preview', methods=['GET'])
def get_preview(brief_id: str):
    """
    GET /api/gtm/brief/<brief_id>/preview

    Returns a quick 3-persona preview (mock) for the Home.vue teaser state.
    Intentionally fast — does not call LLM.
    Full 12-persona generation is done via POST /api/gtm/personas/<brief_id>.
    """
    brief = GTMBriefManager.get_brief(brief_id)
    if not brief:
        return jsonify({'success': False, 'error': f'Brief not found: {brief_id}'}), 404

    preview = _load_mock_preview()
    return jsonify({'success': True, 'data': preview})


@gtm_bp.route('/personas/<brief_id>', methods=['POST'])
def generate_personas(brief_id: str):
    """
    POST /api/gtm/personas/<brief_id>

    Generate 10-12 buyer personas using LLM + GTM brief context.
    Caches result to uploads/gtm_briefs/<brief_id>/personas.json.
    Returns cached personas if already generated (idempotent).
    """
    brief = GTMBriefManager.get_brief(brief_id)
    if not brief:
        return jsonify({'success': False, 'error': f'Brief not found: {brief_id}'}), 404

    # Return cached if available
    cached = _load_cached_personas(brief_id)
    if cached:
        logger.info(f"Returning cached personas for brief {brief_id}")
        return jsonify({'success': True, 'data': cached, 'cached': True})

    try:
        from ..services.gtm_persona_generator import GTMPersonaGenerator
        generator = GTMPersonaGenerator()
        count = request.get_json(silent=True, force=True) or {}
        n = int(count.get('count', 12))
        personas = generator.generate(brief, count=n)
        _save_personas(brief_id, personas)
        logger.info(f"Generated and cached {len(personas)} personas for brief {brief_id}")
        return jsonify({'success': True, 'data': personas, 'cached': False})
    except Exception as e:
        logger.error(f"Persona generation failed: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@gtm_bp.route('/personas/<brief_id>', methods=['GET'])
def get_personas(brief_id: str):
    """
    GET /api/gtm/personas/<brief_id>

    Returns cached personas if available. If not cached, generates them on-demand
    and caches the result. Use POST for an explicit generation trigger.
    """
    brief = GTMBriefManager.get_brief(brief_id)
    if not brief:
        return jsonify({'success': False, 'error': f'Brief not found: {brief_id}'}), 404

    cached = _load_cached_personas(brief_id)
    if cached:
        return jsonify({'success': True, 'data': cached, 'cached': True})

    # Auto-generate on GET if not cached
    try:
        from ..services.gtm_persona_generator import GTMPersonaGenerator
        generator = GTMPersonaGenerator()
        personas = generator.generate(brief, count=12)
        _save_personas(brief_id, personas)
        return jsonify({'success': True, 'data': personas, 'cached': False})
    except Exception as e:
        logger.error(f"On-demand persona generation failed: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@gtm_bp.route('/briefs', methods=['GET'])
def list_briefs():
    """GET /api/gtm/briefs — list recent GTM briefs."""
    limit = request.args.get('limit', 20, type=int)
    briefs = GTMBriefManager.list_briefs(limit=limit)
    return jsonify({
        'success': True,
        'data': [b.to_dict() for b in briefs],
        'count': len(briefs),
    })
