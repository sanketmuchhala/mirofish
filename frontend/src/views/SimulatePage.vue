<template>
  <div class="sim-page">

    <!-- Navbar -->
    <nav class="sim-nav">
      <router-link to="/" class="sim-nav-brand">GTM SIM LAB</router-link>
      <div class="sim-nav-right">
        <span class="sim-nav-step">New Simulation</span>
      </div>
    </nav>

    <!-- Two-panel layout -->
    <div class="sim-layout">

      <!-- Left: Form -->
      <div class="sim-left">
        <div class="sim-left-header">
          <h1 class="sim-title">GTM Simulation Brief</h1>
          <p class="sim-subtitle">
            Describe your product and buyer — the AI will generate buyer personas,
            test outreach angles, simulate reactions, and produce a GTM report.
          </p>
        </div>

        <div class="sim-form-wrap">
          <GTMBriefForm
            :loading="loading"
            :initialData="demoData"
            :hideParams="true"
            @submit="handleSubmit"
          />
        </div>
      </div>

      <!-- Right: Sticky parameters + viz -->
      <div class="sim-right">
        <div class="sim-right-inner">

          <!-- Parameters block -->
          <div class="sim-params">
            <div class="sim-params-label">Simulation Scale</div>

            <!-- Persona count -->
            <div class="sim-param-row">
              <div class="sim-param-header">
                <span class="sim-param-name">Buyer Personas</span>
                <span class="sim-param-val">{{ numPersonas }}</span>
              </div>
              <input
                v-model.number="numPersonas"
                type="range"
                class="sim-slider"
                min="6" max="500" step="1"
              />
              <div class="sim-slider-ticks">
                <span>6</span><span>50</span><span>100</span><span>200</span><span>500</span>
              </div>
            </div>

            <!-- Message variants -->
            <div class="sim-param-row">
              <div class="sim-param-header">
                <span class="sim-param-name">Message Angles</span>
              </div>
              <div class="sim-pills">
                <button
                  v-for="n in [2, 3, 4, 5]"
                  :key="n"
                  class="sim-pill"
                  :class="{ active: numMessages === n }"
                  @click="numMessages = n"
                  type="button"
                >{{ n }}</button>
              </div>
            </div>

            <!-- Live math -->
            <div class="sim-math">
              <div class="sim-math-row">
                <span class="sim-math-label">Reactions simulated</span>
                <span class="sim-math-val">{{ numPersonas }} × {{ numMessages }} = <strong>{{ numPersonas * numMessages }}</strong></span>
              </div>
              <div class="sim-math-row">
                <span class="sim-math-label">Estimated time</span>
                <span class="sim-math-val">{{ timeEstimate }}</span>
              </div>
              <div class="sim-math-row">
                <span class="sim-math-label">Approx. LLM cost</span>
                <span class="sim-math-val">~${{ costEstimate }}</span>
              </div>
            </div>
          </div>

          <!-- Demo fill button -->
          <button class="sim-demo-btn" @click="loadDemo" type="button">
            Load example brief (AI SDR)
          </button>

          <!-- HeroViz -->
          <div class="sim-viz-wrap">
            <div class="sim-viz-label">Agent simulation preview</div>
            <HeroViz />
          </div>

          <!-- What you'll get -->
          <div class="sim-what">
            <div class="sim-what-item">
              <span class="sim-what-num">{{ numPersonas }}</span>
              <span class="sim-what-label">Buyer Personas</span>
            </div>
            <div class="sim-what-sep"></div>
            <div class="sim-what-item">
              <span class="sim-what-num">{{ numMessages }}</span>
              <span class="sim-what-label">Message Angles</span>
            </div>
            <div class="sim-what-sep"></div>
            <div class="sim-what-item">
              <span class="sim-what-num">{{ numPersonas * numMessages }}</span>
              <span class="sim-what-label">Reactions</span>
            </div>
            <div class="sim-what-sep"></div>
            <div class="sim-what-item">
              <span class="sim-what-num">1</span>
              <span class="sim-what-label">GTM Report</span>
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- Error toast -->
    <div v-if="submitError" class="sim-error-toast">
      {{ submitError }}
      <button @click="submitError = ''" class="sim-error-close">×</button>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import GTMBriefForm from '../components/GTMBriefForm.vue'
import HeroViz from '../components/HeroViz.vue'
import { submitGTMBrief, getGTMPreview } from '../api/gtm.js'
import { setGTMBrief, setSimulationPreview } from '../store/gtmSimulation.js'
import { MOCK_GTM_PREVIEW } from '../mock/gtm_preview.js'
import { DEMO_BRIEF } from '../mock/gtm_demo.js'

const router = useRouter()

const loading = ref(false)
const submitError = ref('')
const demoData = ref(null)
const numPersonas = ref(12)
const numMessages = ref(3)

const timeEstimate = computed(() => {
  const n = numPersonas.value
  if (n <= 12)  return '~1 min'
  if (n <= 50)  return '~2–4 min'
  if (n <= 100) return '~5–10 min'
  if (n <= 200) return '~15–25 min'
  return '~30–60 min'
})

const costEstimate = computed(() => {
  return (numPersonas.value * 0.008 * numMessages.value).toFixed(2)
})

function loadDemo() {
  demoData.value = { ...DEMO_BRIEF }
}

async function handleSubmit(payload) {
  loading.value = true
  submitError.value = ''

  // Inject simulation params from the right panel
  const fullPayload = {
    ...payload,
    num_personas: numPersonas.value,
    num_messages: numMessages.value,
  }

  try {
    setGTMBrief(fullPayload)
    const res = await submitGTMBrief(fullPayload)

    if (!res.success) throw new Error(res.error || 'Submission failed')

    const briefId = res.data.brief_id

    let preview = MOCK_GTM_PREVIEW
    try {
      const previewRes = await getGTMPreview(briefId)
      if (previewRes.success && previewRes.data) preview = previewRes.data
    } catch (_) {}

    setSimulationPreview(briefId, preview)
    router.push({ name: 'GTMPersonas', params: { briefId } })
  } catch (err) {
    submitError.value = err.message || 'Submission failed. Check your connection and try again.'
    loading.value = false
  }
}
</script>

<style scoped>
/* ── Shell ──────────────────────────────────────────────── */
.sim-page {
  min-height: 100vh;
  background: var(--bg-base);
  color: var(--text-primary);
  font-family: var(--font-sans);
  display: flex;
  flex-direction: column;
}

/* ── Navbar ─────────────────────────────────────────────── */
.sim-nav {
  height: 56px;
  background: rgba(0,0,0,0.8);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  position: sticky;
  top: 0;
  z-index: 20;
  flex-shrink: 0;
}

.sim-nav-brand {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: var(--text-primary);
  text-decoration: none;
}

.sim-nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.sim-nav-step {
  font-size: 12px;
  color: var(--text-tertiary);
  font-family: var(--font-mono);
}

/* ── Layout ─────────────────────────────────────────────── */
.sim-layout {
  display: grid;
  grid-template-columns: 1fr 420px;
  flex: 1;
  min-height: 0;
}

/* ── Left panel ─────────────────────────────────────────── */
.sim-left {
  border-right: 1px solid var(--border-subtle);
  overflow-y: auto;
  padding: 40px 48px 80px;
}

.sim-left-header {
  margin-bottom: 28px;
}

.sim-title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.sim-subtitle {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.65;
  max-width: 520px;
}

.sim-form-wrap {
  max-width: 600px;
}

/* ── Right panel ────────────────────────────────────────── */
.sim-right {
  background: var(--bg-surface);
  overflow-y: auto;
}

.sim-right-inner {
  position: sticky;
  top: 0;
  padding: 24px 24px 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-height: calc(100vh - 56px);
  overflow-y: auto;
}

/* ── Parameters ─────────────────────────────────────────── */
.sim-params {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sim-params-label {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.sim-param-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sim-param-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sim-param-name {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-primary);
}

.sim-param-val {
  font-family: var(--font-mono);
  font-size: 20px;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: -0.03em;
}

/* Slider */
.sim-slider {
  width: 100%;
  height: 4px;
  -webkit-appearance: none;
  appearance: none;
  background: var(--border-muted);
  border-radius: 2px;
  outline: none;
  cursor: pointer;
  border: none;
  padding: 0;
}
.sim-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--accent);
  cursor: pointer;
  border: 2px solid var(--bg-card);
  box-shadow: 0 0 6px rgba(59,130,246,0.4);
}
.sim-slider::-moz-range-thumb {
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--bg-card);
}

.sim-slider-ticks {
  display: flex;
  justify-content: space-between;
  font-size: 9px;
  color: var(--text-tertiary);
  font-family: var(--font-mono);
}

/* Pills */
.sim-pills {
  display: flex;
  gap: 6px;
}

.sim-pill {
  flex: 1;
  padding: 7px;
  border: 1px solid var(--border-muted);
  border-radius: 6px;
  background: transparent;
  color: var(--text-secondary);
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
  text-align: center;
}
.sim-pill.active {
  border-color: var(--accent);
  background: var(--accent-dim);
  color: var(--accent);
}

/* Math display */
.sim-math {
  background: var(--bg-elevated);
  border-radius: 6px;
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sim-math-row {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
}

.sim-math-label { color: var(--text-tertiary); }
.sim-math-val   { color: var(--text-secondary); }
.sim-math-val strong { color: var(--text-primary); }

/* Demo btn */
.sim-demo-btn {
  width: 100%;
  padding: 10px;
  background: transparent;
  border: 1px dashed var(--border-muted);
  border-radius: 8px;
  color: var(--text-secondary);
  font-size: 12px;
  font-family: var(--font-sans);
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
  text-align: center;
}
.sim-demo-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

/* Viz */
.sim-viz-wrap {
  position: relative;
  height: 220px;
  border-radius: 10px;
  overflow: hidden;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  flex-shrink: 0;
}

.sim-viz-label {
  position: absolute;
  top: 8px;
  left: 12px;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-tertiary);
  z-index: 10;
  font-family: var(--font-mono);
  opacity: 0.7;
}

/* What you'll get strip */
.sim-what {
  display: flex;
  align-items: center;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  overflow: hidden;
}

.sim-what-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 8px;
  gap: 2px;
}

.sim-what-sep {
  width: 1px;
  height: 32px;
  background: var(--border-subtle);
  flex-shrink: 0;
}

.sim-what-num {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.02em;
  font-family: var(--font-mono);
}

.sim-what-label {
  font-size: 9px;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* Error toast */
.sim-error-toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(248,113,113,0.12);
  border: 1px solid rgba(248,113,113,0.3);
  border-radius: 8px;
  padding: 12px 20px;
  font-size: 13px;
  color: var(--red);
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 100;
  max-width: 480px;
}

.sim-error-close {
  background: none;
  border: none;
  color: var(--red);
  font-size: 16px;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

/* ── Responsive ─────────────────────────────────────────── */
@media (max-width: 900px) {
  .sim-layout { grid-template-columns: 1fr; }
  .sim-right  { position: static; border-top: 1px solid var(--border-subtle); }
  .sim-right-inner { position: static; max-height: none; }
  .sim-left   { padding: 24px 20px 60px; border-right: none; }
}
</style>
