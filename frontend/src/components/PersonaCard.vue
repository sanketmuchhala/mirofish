<template>
  <!-- COMPACT MODE: for Home.vue quick preview (3-persona teaser) -->
  <div v-if="compact" class="persona-card" :class="persona.reaction">
    <div class="persona-name">{{ persona.name }}</div>
    <div class="persona-role">{{ persona.title || persona.role }}</div>
    <div class="persona-company">{{ persona.company_type || persona.company }} · {{ persona.company_stage }}</div>
    <div class="persona-reaction-badge" :class="persona.reaction">
      {{ reactionLabel }}
    </div>
    <div class="persona-quote">"{{ persona.likely_response }}"</div>
  </div>

  <!-- FULL MODE: for GTMPersonasView grid -->
  <div v-else class="persona-card-full" :class="persona.reaction">
    <!-- Header -->
    <div class="pcf-header">
      <div class="pcf-identity">
        <div class="pcf-name">{{ persona.name }}</div>
        <div class="pcf-title">{{ persona.title }}</div>
        <div class="pcf-company">{{ persona.company_type }} · {{ persona.company_stage }}</div>
      </div>
      <div class="pcf-badges">
        <span class="reaction-badge" :class="persona.reaction">{{ reactionLabel }}</span>
        <span class="skep-badge" :title="`Skepticism: ${persona.skepticism_level}/5`">
          {{ '●'.repeat(persona.skepticism_level) }}{{ '○'.repeat(5 - persona.skepticism_level) }}
        </span>
      </div>
    </div>

    <!-- Goal -->
    <div class="pcf-row">
      <span class="pcf-row-label">GOAL</span>
      <span class="pcf-row-value">{{ persona.primary_goal }}</span>
    </div>

    <!-- Pain Points -->
    <div class="pcf-row" v-if="persona.pain_points?.length">
      <span class="pcf-row-label">PAINS</span>
      <span class="pcf-row-value">{{ persona.pain_points.join(' · ') }}</span>
    </div>

    <!-- Top Objection -->
    <div class="pcf-row" v-if="persona.objections?.length">
      <span class="pcf-row-label">OBJECTS</span>
      <span class="pcf-row-value objection-text">"{{ persona.objections[0] }}"</span>
    </div>

    <!-- Buying Triggers -->
    <div class="pcf-row" v-if="persona.buying_triggers?.length">
      <span class="pcf-row-label">TRIGGERS</span>
      <span class="pcf-row-value">{{ persona.buying_triggers.slice(0, 2).join(' · ') }}</span>
    </div>

    <!-- Divider -->
    <div class="pcf-divider"></div>

    <!-- Budget / Risk / Channel -->
    <div class="pcf-meta-row">
      <span class="pcf-meta-item">
        Budget: <strong :class="`sens-${persona.budget_sensitivity}`">{{ (persona.budget_sensitivity || '').toUpperCase() }}</strong>
      </span>
      <span class="pcf-meta-sep">·</span>
      <span class="pcf-meta-item">
        Risk: <strong :class="`risk-${persona.risk_tolerance}`">{{ (persona.risk_tolerance || '').toUpperCase() }}</strong>
      </span>
      <span class="pcf-meta-sep">·</span>
      <span class="pcf-meta-item">
        Best: <strong>{{ angleLabel }}</strong>
      </span>
    </div>

    <!-- Summary -->
    <div class="pcf-summary">"{{ persona.summary }}"</div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  /** Full persona object from the GTM persona generator */
  persona: {
    type: Object,
    required: true,
  },
  /** If true, renders the compact teaser card (for Home.vue preview) */
  compact: {
    type: Boolean,
    default: false,
  },
})

const reactionLabel = computed(() => {
  const map = { interested: '✓ Interested', neutral: '→ Neutral', objection: '⚠ Objection' }
  return map[props.persona.reaction] ?? props.persona.reaction
})

const angleLabel = computed(() => {
  const map = { pain_led: 'Pain-Led', roi_led: 'ROI-Led', social_proof_led: 'Social Proof' }
  return map[props.persona.likely_message_angle] ?? props.persona.likely_message_angle ?? '—'
})
</script>

<style scoped>
/* ── COMPACT MODE ─────────────────────────────────────────────── */
.persona-card {
  flex: 1;
  min-width: 140px;
  border: 1px solid #E0E0E0;
  border-radius: 4px;
  padding: 12px;
  background: #FAFAFA;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.persona-card.interested { border-left: 3px solid #4CAF50; }
.persona-card.neutral    { border-left: 3px solid #FF9800; }
.persona-card.objection  { border-left: 3px solid #E53935; }

.persona-name { font-weight: 700; font-size: 13px; color: #111; }
.persona-role { font-size: 11px; color: #555; font-family: 'JetBrains Mono', monospace; }
.persona-company { font-size: 10px; color: #888; }

.persona-reaction-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 2px;
  width: fit-content;
  margin-top: 4px;
}
.persona-reaction-badge.interested { background: #E8F5E9; color: #2E7D32; }
.persona-reaction-badge.neutral    { background: #FFF3E0; color: #E65100; }
.persona-reaction-badge.objection  { background: #FFEBEE; color: #C62828; }

.persona-quote {
  font-size: 11px;
  color: #555;
  font-style: italic;
  margin-top: 6px;
  line-height: 1.4;
  border-top: 1px solid #EEE;
  padding-top: 6px;
}

/* ── FULL MODE ───────────────────────────────────────────────── */
.persona-card-full {
  background: #fff;
  border: 1px solid #E5E5E5;
  border-radius: 5px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: box-shadow 0.15s;
}

.persona-card-full:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.07);
}

.persona-card-full.interested { border-left: 4px solid #4CAF50; }
.persona-card-full.neutral    { border-left: 4px solid #FF9800; }
.persona-card-full.objection  { border-left: 4px solid #E53935; }

/* Header */
.pcf-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
}

.pcf-identity { flex: 1; min-width: 0; }

.pcf-name {
  font-weight: 700;
  font-size: 14px;
  color: #111;
  line-height: 1.2;
}

.pcf-title {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #444;
  margin-top: 2px;
}

.pcf-company {
  font-size: 10px;
  color: #888;
  margin-top: 2px;
}

/* Badges */
.pcf-badges {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
  flex-shrink: 0;
}

.reaction-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 2px;
  white-space: nowrap;
}
.reaction-badge.interested { background: #E8F5E9; color: #2E7D32; }
.reaction-badge.neutral    { background: #FFF3E0; color: #E65100; }
.reaction-badge.objection  { background: #FFEBEE; color: #C62828; }

.skep-badge {
  font-size: 9px;
  color: #BBB;
  letter-spacing: 1px;
  cursor: help;
}

/* Info rows */
.pcf-row {
  display: flex;
  gap: 8px;
  font-size: 11px;
  line-height: 1.4;
}

.pcf-row-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  font-weight: 700;
  color: #999;
  letter-spacing: 0.8px;
  white-space: nowrap;
  padding-top: 1px;
  min-width: 56px;
}

.pcf-row-value { color: #333; }

.objection-text { font-style: italic; color: #555; }

/* Divider */
.pcf-divider {
  height: 1px;
  background: #F0F0F0;
  margin: 2px 0;
}

/* Meta row */
.pcf-meta-row {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  color: #666;
  flex-wrap: wrap;
}

.pcf-meta-sep { color: #CCC; }

.pcf-meta-item strong {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 9px;
}

.sens-low, .risk-low   { color: #2E7D32; }
.sens-medium, .risk-medium { color: #E65100; }
.sens-high, .risk-high  { color: #C62828; }

/* Summary quote */
.pcf-summary {
  font-size: 11px;
  font-style: italic;
  color: #555;
  line-height: 1.4;
  border-top: 1px solid #F0F0F0;
  padding-top: 8px;
  margin-top: 2px;
}
</style>
