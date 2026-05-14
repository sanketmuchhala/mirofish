"""
GTM Aggregator — pure Python aggregation of message reactions.
No LLM calls. Takes messages + reactions → summaries + winner.
"""

from collections import Counter
from typing import List, Dict, Any


def _verdict(interest_score: float) -> str:
    if interest_score >= 7.0:
        return 'positive'
    if interest_score >= 4.0:
        return 'neutral'
    return 'negative'


def _angle_label(angle: str) -> str:
    return {
        'pain_first': 'Pain-First',
        'roi_first': 'ROI-First',
        'curiosity_first': 'Curiosity-First',
    }.get(angle, angle)


def _recommendation(summary: dict) -> str:
    angle = summary['angle']
    pos = summary['positive_count']
    neg = summary['negative_count']
    avg = summary['average_interest_score']

    if avg >= 7.5:
        return f"Strong signal — {pos} of {pos + summary['neutral_count'] + neg} personas responded positively."
    if avg >= 6.0:
        return f"Moderate signal. Best for {', '.join(summary['best_fit_personas'][:2])} personas."
    return f"Weak signal for most personas. {_angle_label(angle)} messaging may need repositioning."


def aggregate(messages: list, reactions: list) -> dict:
    """
    Aggregate reactions per message and compute the winning angle.

    Args:
        messages: list of OutreachMessage dicts
        reactions: list of BuyerReaction dicts

    Returns:
        dict with keys:
          summaries: list of MessageTestSummary dicts
          winner: WinnerResult dict
    """
    # Group reactions by message_id
    by_message: Dict[str, List[dict]] = {}
    for r in reactions:
        mid = r.get('message_id', '')
        by_message.setdefault(mid, []).append(r)

    summaries = []
    for msg in messages:
        mid = msg['id']
        rxns = by_message.get(mid, [])
        if not rxns:
            continue

        n = len(rxns)
        avg_interest = round(sum(r.get('interest_score', 5) for r in rxns) / n, 2)
        avg_clarity  = round(sum(r.get('clarity_score', 5) for r in rxns) / n, 2)
        avg_trust    = round(sum(r.get('trust_score', 5) for r in rxns) / n, 2)
        avg_urgency  = round(sum(r.get('urgency_score', 5) for r in rxns) / n, 2)

        verdicts = [_verdict(r.get('interest_score', 5)) for r in rxns]
        pos_count = verdicts.count('positive')
        neu_count = verdicts.count('neutral')
        neg_count = verdicts.count('negative')

        # Top objections (most common non-empty strings)
        objections = [r.get('objection', '') for r in rxns if r.get('objection')]
        top_objections = [obj for obj, _ in Counter(objections).most_common(3)]

        # Best/worst fit personas (by interest_score)
        sorted_rxns = sorted(rxns, key=lambda r: r.get('interest_score', 5), reverse=True)
        best_fit = [r['persona_id'] for r in sorted_rxns[:3] if r.get('persona_id')]
        worst_fit = [r['persona_id'] for r in sorted_rxns[-3:] if r.get('persona_id')]

        summary = {
            'message_id': mid,
            'angle': msg.get('angle', ''),
            'average_interest_score': avg_interest,
            'average_clarity_score': avg_clarity,
            'average_trust_score': avg_trust,
            'average_urgency_score': avg_urgency,
            'positive_count': pos_count,
            'neutral_count': neu_count,
            'negative_count': neg_count,
            'top_objections': top_objections,
            'best_fit_personas': best_fit,
            'worst_fit_personas': worst_fit,
            'recommendation': '',
        }
        summary['recommendation'] = _recommendation(summary)
        summaries.append(summary)

    winner = _compute_winner(summaries)

    return {'summaries': summaries, 'winner': winner}


def _compute_winner(summaries: list) -> dict:
    if not summaries:
        return {'winner_message_id': None, 'winner_angle': None, 'close_test': False, 'note': None}

    ranked = sorted(
        summaries,
        key=lambda s: (
            s['average_interest_score'],
            s['positive_count'],
            s['average_trust_score'],
        ),
        reverse=True,
    )

    winner = ranked[0]
    runner_up = ranked[1] if len(ranked) > 1 else None

    close_test = (
        runner_up is not None
        and abs(winner['average_interest_score'] - runner_up['average_interest_score']) < 0.5
    )

    note = (
        'Close test — the top two angles are within 0.5 points. '
        'Run real outbound validation with both before committing.'
        if close_test else None
    )

    return {
        'winner_message_id': winner['message_id'],
        'winner_angle': winner['angle'],
        'close_test': close_test,
        'note': note,
    }
