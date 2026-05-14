/**
 * GTM simulation session state.
 * Reactive singleton — same pattern as store/pendingUpload.js.
 * Holds the brief, quick preview, and full persona set between views.
 */
import { reactive } from 'vue'

const state = reactive({
  /** @type {object|null} Raw normalized form data */
  brief: null,
  /** @type {string|null} brief_id returned from POST /api/gtm/brief */
  briefId: null,
  /** @type {'idle'|'submitting'|'preview'|'error'} */
  status: 'idle',
  /** @type {object|null} Quick 3-persona preview from GET /api/gtm/brief/<id>/preview */
  preview: null,
  /**
   * Full 12-persona array from POST/GET /api/gtm/personas/<id>.
   * @type {Array<{
   *   id: string, name: string, title: string, company_type: string,
   *   company_stage: string, persona_type: string, primary_goal: string,
   *   pain_points: string[], buying_triggers: string[], objections: string[],
   *   communication_style: string, budget_sensitivity: 'low'|'medium'|'high',
   *   risk_tolerance: 'low'|'medium'|'high', preferred_channels: string[],
   *   likely_message_angle: string, summary: string,
   *   reaction: 'interested'|'neutral'|'objection', skepticism_level: number,
   *   likely_response: string, objection_category: string|null
   * }>|null}
   */
  personas: null,
  /** @type {string|null} */
  error: null,
})

export function setGTMBrief(briefData) {
  state.brief = briefData
  state.status = 'submitting'
  state.error = null
}

export function setSimulationPreview(briefId, previewData) {
  state.briefId = briefId
  state.preview = previewData
  state.status = 'preview'
}

export function setPersonas(personasArray) {
  state.personas = personasArray
}

export function getPersonas() {
  return state.personas
}

export function setGTMError(message) {
  state.error = message
  state.status = 'error'
}

export function getGTMState() {
  return {
    brief: state.brief,
    briefId: state.briefId,
    status: state.status,
    preview: state.preview,
    personas: state.personas,
    error: state.error,
  }
}

export function resetGTMState() {
  state.brief = null
  state.briefId = null
  state.status = 'idle'
  state.preview = null
  state.personas = null
  state.error = null
}

export default state
