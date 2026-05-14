<template>
  <div class="home-container">

    <!-- ── Navbar ─────────────────────────────────────────────── -->
    <nav class="navbar">
      <div class="nav-brand">GTM SIM LAB</div>
      <div class="nav-links">
        <a href="https://github.com/sanketmuchhala/GTM-SImulator" target="_blank" class="github-link">
          GitHub <span class="arrow">↗</span>
        </a>
      </div>
    </nav>

    <div class="main-content">

      <!-- ── Hero ──────────────────────────────────────────────── -->
      <section class="hero-section">
        <div class="hero-eyebrow">
          <span class="hero-badge">AI-Powered GTM Lab</span>
          <span class="hero-version">v0.1 Preview</span>
        </div>

        <h1 class="hero-title">
          Simulate your GTM<br>
          <span class="hero-title-accent">before you launch outreach.</span>
        </h1>

        <p class="hero-sub">
          Enter a product brief. Get 12 AI buyer personas, 3 tested message angles,
          36 simulated reactions, and a ready-to-run 7-day outbound experiment —
          in under 2 minutes.
        </p>

        <div class="hero-stats">
          <div class="hero-stat">
            <span class="hero-stat-num">12</span>
            <span class="hero-stat-label">Buyer Personas</span>
          </div>
          <div class="hero-stat-sep"></div>
          <div class="hero-stat">
            <span class="hero-stat-num">36</span>
            <span class="hero-stat-label">Simulated Reactions</span>
          </div>
          <div class="hero-stat-sep"></div>
          <div class="hero-stat">
            <span class="hero-stat-num">~$5</span>
            <span class="hero-stat-label">Per Simulation</span>
          </div>
          <div class="hero-stat-sep"></div>
          <div class="hero-stat">
            <span class="hero-stat-num">&lt;2 min</span>
            <span class="hero-stat-label">End to End</span>
          </div>
        </div>
      </section>

      <!-- ── Main: Workflow + Form ─────────────────────────────── -->
      <section class="main-section">

        <!-- Left: How it works -->
        <div class="how-it-works">
          <div class="hiw-header">How it works</div>
          <div class="hiw-steps">
            <div class="hiw-step" v-for="(step, i) in steps" :key="i">
              <div class="hiw-step-left">
                <div class="hiw-step-num">{{ String(i + 1).padStart(2, '0') }}</div>
                <div class="hiw-step-line" v-if="i < steps.length - 1"></div>
              </div>
              <div class="hiw-step-content">
                <div class="hiw-step-title">{{ step.title }}</div>
                <div class="hiw-step-desc">{{ step.desc }}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Form card -->
        <div class="form-panel">

          <!-- Form header -->
          <div class="form-panel-header">
            <div class="form-panel-title">GTM Brief</div>
            <button class="demo-pill" @click="loadDemoScenario">
              ⚡ Try example
            </button>
          </div>

          <!-- States -->
          <div class="form-panel-body">

            <!-- form -->
            <div v-if="homeState === 'form'">
              <GTMBriefForm :loading="loading" :initialData="demoData" @submit="handleBriefSubmit" />
            </div>

            <!-- submitting -->
            <div v-else-if="homeState === 'submitting'" class="state-loading">
              <div class="state-spinner"></div>
              <div class="state-loading-steps">
                <div class="sls-step sls-done">✓ Brief validated</div>
                <div class="sls-step sls-active">◉ Generating persona preview…</div>
                <div class="sls-step sls-pending">○ Preparing simulation</div>
              </div>
            </div>

            <!-- preview -->
            <div v-else-if="homeState === 'preview'" class="state-preview">
              <div class="state-preview-header">
                <span class="state-dot state-dot--ready"></span>
                <span class="state-preview-title">Simulation ready</span>
              </div>

              <div class="preview-section-label">Buyer persona preview</div>
              <div class="preview-personas">
                <div
                  v-for="persona in previewPersonas"
                  :key="persona.id"
                  class="preview-persona"
                  :class="persona.reaction"
                >
                  <div class="pp-header">
                    <span class="pp-name">{{ persona.name }}</span>
                    <span class="pp-badge" :class="persona.reaction">{{ reactionLabel(persona.reaction) }}</span>
                  </div>
                  <div class="pp-role">{{ persona.role }}</div>
                  <div class="pp-quote">"{{ persona.likely_response }}"</div>
                </div>
              </div>

              <div v-if="previewTeasers.length" class="preview-teasers">
                <div class="preview-section-label">Message angle signals</div>
                <div v-for="teaser in previewTeasers" :key="teaser.angle" class="teaser-item">
                  <span class="teaser-angle">{{ teaser.label }}</span>
                  <span class="teaser-preview">{{ teaser.preview }}</span>
                </div>
              </div>

              <div class="preview-actions">
                <button class="btn-primary" @click="continueToSimulation">
                  Run Full Simulation →
                </button>
                <button class="btn-ghost" @click="resetForm">← Edit Brief</button>
              </div>
            </div>

            <!-- error -->
            <div v-else-if="homeState === 'error'" class="state-error">
              <div class="state-error-icon">⚠</div>
              <div class="state-error-msg">{{ submitError || 'Brief submission failed. Check your connection and try again.' }}</div>
              <button class="btn-ghost" @click="resetForm">← Edit Brief</button>
            </div>

          </div>
        </div>
      </section>

      <!-- ── Footer ─────────────────────────────────────────────── -->
      <footer class="home-footer">
        <span>GTM Simulation Lab — open source</span>
        <span class="home-footer-sep">·</span>
        <a href="https://github.com/sanketmuchhala/GTM-SImulator" target="_blank" rel="noopener" class="home-footer-link">GitHub ↗</a>
        <span class="home-footer-sep">·</span>
        <span>Forked from <a href="https://github.com/666ghj/MiroFish" target="_blank" rel="noopener" class="home-footer-link">MiroFish ↗</a></span>
      </footer>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import GTMBriefForm from '../components/GTMBriefForm.vue'
import { submitGTMBrief, getGTMPreview } from '../api/gtm.js'
import { setGTMBrief, setSimulationPreview, resetGTMState, getGTMState } from '../store/gtmSimulation.js'
import { MOCK_GTM_PREVIEW } from '../mock/gtm_preview.js'
import { DEMO_BRIEF } from '../mock/gtm_demo.js'

const router = useRouter()

const steps = [
  { title: 'Input Brief',      desc: 'Describe your product, ICP, pricing, and GTM goal.' },
  { title: 'Buyer Personas',   desc: 'AI generates 12 distinct buyer archetypes from your ICP.' },
  { title: 'Message Testing',  desc: '3 outreach angles (pain-first, ROI-first, curiosity-first) tested against each persona.' },
  { title: 'Buyer Reactions',  desc: 'Each persona responds with interest scores, objections, and a simulated reply.' },
  { title: 'GTM Report',       desc: 'Best angle, top objections with rebuttals, and a 7-day outbound experiment plan.' },
]

// 'form' | 'submitting' | 'preview' | 'error'
const homeState = ref('form')
const loading = ref(false)
const submitError = ref('')
const previewPersonas = ref([])
const previewTeasers = ref([])
const demoData = ref(null)

function loadDemoScenario() {
  demoData.value = { ...DEMO_BRIEF }
}

const scrollToBottom = () => {
  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })
}

function reactionLabel(reaction) {
  return { interested: '✓ Interested', neutral: '→ Neutral', objection: '⚠ Objection' }[reaction] ?? reaction
}

async function handleBriefSubmit(payload) {
  loading.value = true
  homeState.value = 'submitting'
  submitError.value = ''

  try {
    setGTMBrief(payload)
    const res = await submitGTMBrief(payload)

    if (!res.success) {
      throw new Error(res.error || 'Submission failed')
    }

    const briefId = res.data.brief_id

    // Fetch preview (fall back to mock if unavailable)
    let preview = MOCK_GTM_PREVIEW
    try {
      const previewRes = await getGTMPreview(briefId)
      if (previewRes.success && previewRes.data) preview = previewRes.data
    } catch (_) { /* use mock */ }

    setSimulationPreview(briefId, preview)
    previewPersonas.value = preview.personas ?? []
    previewTeasers.value = preview.message_angle_teasers ?? []
    homeState.value = 'preview'
  } catch (err) {
    submitError.value = err.message || 'Something went wrong. Please try again.'
    homeState.value = 'error'
  } finally {
    loading.value = false
  }
}

function continueToSimulation() {
  const { briefId } = getGTMState()
  if (briefId) {
    router.push({ name: 'GTMPersonas', params: { briefId } })
  } else {
    // Fallback: if briefId was lost somehow, go back to form
    homeState.value = 'form'
  }
}

function resetForm() {
  resetGTMState()
  previewPersonas.value = []
  previewTeasers.value = []
  demoData.value = null
  homeState.value = 'form'
  submitError.value = ''
}
</script>

<style scoped>
/* ── Shell ───────────────────────────────────────────────────── */
.home-container {
  min-height: 100vh;
  background: #fff;
  font-family: var(--font-sans);
  color: #111;
}

/* ── Navbar ──────────────────────────────────────────────────── */
.navbar {
  height: 56px;
  background: #fff;
  border-bottom: 1px solid #ebebeb;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  position: sticky;
  top: 0;
  z-index: 20;
}

.nav-brand {
  font-family: var(--font-mono);
  font-weight: 800;
  letter-spacing: 0.1em;
  font-size: 13px;
  color: #111;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 16px;
}

.github-link {
  color: #555;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: color 0.15s;
}

.github-link:hover { color: #111; }
.arrow { font-size: 11px; }

/* ── Main content wrapper ────────────────────────────────────── */
.main-content {
  max-width: 1160px;
  margin: 0 auto;
  padding: 64px 40px 0;
}

/* ── Hero ────────────────────────────────────────────────────── */
.hero-section {
  margin-bottom: 64px;
  max-width: 760px;
}

.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.hero-badge {
  background: #f0f0f8;
  color: #6366f1;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 20px;
}

.hero-version {
  font-size: 12px;
  color: #aaa;
  font-family: var(--font-mono);
}

.hero-title {
  font-size: 3.2rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  line-height: 1.15;
  color: #111;
  margin: 0 0 20px;
}

.hero-title-accent {
  color: #6366f1;
}

.hero-sub {
  font-size: 1rem;
  line-height: 1.7;
  color: #555;
  max-width: 600px;
  margin: 0 0 32px;
}

.hero-stats {
  display: flex;
  align-items: center;
  gap: 0;
  border: 1px solid #ebebeb;
  border-radius: 10px;
  padding: 0;
  overflow: hidden;
  width: fit-content;
}

.hero-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 14px 28px;
  gap: 3px;
}

.hero-stat-sep {
  width: 1px;
  height: 36px;
  background: #ebebeb;
  flex-shrink: 0;
}

.hero-stat-num {
  font-size: 20px;
  font-weight: 700;
  color: #111;
  letter-spacing: -0.02em;
}

.hero-stat-label {
  font-size: 11px;
  color: #aaa;
  white-space: nowrap;
}

/* ── Main section: How it works + Form ───────────────────────── */
.main-section {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 48px;
  align-items: start;
  border-top: 1px solid #ebebeb;
  padding-top: 48px;
}

/* ── Left: How it works ─────────────────────────────────────── */
.how-it-works {
  position: sticky;
  top: 80px;
}

.hiw-header {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 24px;
}

.hiw-steps {
  display: flex;
  flex-direction: column;
}

.hiw-step {
  display: flex;
  gap: 16px;
}

.hiw-step-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 28px;
  flex-shrink: 0;
}

.hiw-step-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #f4f4f8;
  border: 1px solid #e8e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  color: #6366f1;
  flex-shrink: 0;
}

.hiw-step-line {
  width: 1px;
  flex: 1;
  min-height: 20px;
  background: #ebebeb;
  margin: 4px 0;
}

.hiw-step-content {
  padding-bottom: 20px;
}

.hiw-step-title {
  font-size: 14px;
  font-weight: 600;
  color: #111;
  margin-bottom: 4px;
}

.hiw-step-desc {
  font-size: 12px;
  color: #888;
  line-height: 1.6;
}

/* ── Right: Form panel ──────────────────────────────────────── */
.form-panel {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

.form-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  border-bottom: 1px solid #ebebeb;
  background: #fafafa;
}

.form-panel-title {
  font-size: 13px;
  font-weight: 700;
  color: #111;
  letter-spacing: 0.02em;
}

.demo-pill {
  background: #f0f0f8;
  color: #6366f1;
  border: 1px solid rgba(99,102,241,0.25);
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.demo-pill:hover {
  background: rgba(99,102,241,0.12);
}

.form-panel-body {
  background: #fff;
}

/* ── Submitting state ───────────────────────────────────────── */
.state-loading {
  padding: 40px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.state-spinner {
  width: 32px;
  height: 32px;
  border: 2px solid #ebebeb;
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }
@keyframes pulse { 50% { opacity: 0.4; } }

.state-loading-steps {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-start;
}

.sls-step {
  font-size: 13px;
  font-family: var(--font-mono);
}

.sls-done    { color: #16a34a; }
.sls-active  { color: #111; animation: pulse 1.2s ease-in-out infinite; }
.sls-pending { color: #ccc; }

/* ── Preview state ──────────────────────────────────────────── */
.state-preview {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.state-preview-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: #111;
}

.state-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.state-dot--ready { background: #16a34a; }

.state-preview-title { font-size: 13px; font-weight: 600; }

.preview-section-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 8px;
}

.preview-personas {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.preview-persona {
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 14px;
  background: #fafafa;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.preview-persona.interested { border-left: 3px solid #16a34a; }
.preview-persona.neutral    { border-left: 3px solid #ea580c; }
.preview-persona.objection  { border-left: 3px solid #dc2626; }

.pp-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 6px;
}

.pp-name {
  font-size: 13px;
  font-weight: 700;
  color: #111;
  line-height: 1.2;
}

.pp-badge {
  font-size: 9px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 3px;
  white-space: nowrap;
  flex-shrink: 0;
}

.pp-badge.interested { background: #dcfce7; color: #15803d; }
.pp-badge.neutral    { background: #ffedd5; color: #c2410c; }
.pp-badge.objection  { background: #fee2e2; color: #b91c1c; }

.pp-role {
  font-size: 11px;
  color: #777;
}

.pp-quote {
  font-size: 11px;
  color: #666;
  font-style: italic;
  line-height: 1.5;
  border-top: 1px solid #eee;
  padding-top: 6px;
  margin-top: 2px;
}

.preview-teasers {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.teaser-item {
  display: flex;
  gap: 10px;
  font-size: 12px;
  align-items: baseline;
}

.teaser-angle {
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 700;
  color: #6366f1;
  min-width: 70px;
}

.teaser-preview {
  color: #555;
  line-height: 1.4;
}

.preview-actions {
  display: flex;
  gap: 10px;
  align-items: center;
  padding-top: 4px;
}

/* ── Error state ────────────────────────────────────────────── */
.state-error {
  padding: 32px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  text-align: center;
}

.state-error-icon { font-size: 28px; }

.state-error-msg {
  font-size: 13px;
  color: #666;
  max-width: 360px;
  line-height: 1.6;
}

/* ── Buttons ────────────────────────────────────────────────── */
.btn-primary {
  flex: 1;
  padding: 11px 18px;
  background: #111;
  color: #fff;
  border: none;
  border-radius: 7px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
  text-align: center;
}

.btn-primary:hover { background: #6366f1; }

.btn-ghost {
  padding: 11px 14px;
  background: transparent;
  color: #666;
  border: 1px solid #d5d5d5;
  border-radius: 7px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
  white-space: nowrap;
}

.btn-ghost:hover { border-color: #999; color: #111; }

/* ── Footer ─────────────────────────────────────────────────── */
.home-footer {
  margin-top: 64px;
  padding: 20px 0 32px;
  border-top: 1px solid #ebebeb;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  color: #aaa;
}

.home-footer-sep { color: #ddd; }

.home-footer-link {
  color: #888;
  text-decoration: none;
  transition: color 0.15s;
}

.home-footer-link:hover { color: #111; }

/* ── Responsive ─────────────────────────────────────────────── */
@media (max-width: 900px) {
  .main-section { grid-template-columns: 1fr; }
  .how-it-works { position: static; }
  .hero-title { font-size: 2.4rem; }
  .hero-stats { flex-wrap: wrap; width: 100%; }
  .preview-personas { grid-template-columns: 1fr; }
  .main-content { padding: 40px 20px 0; }
  .navbar { padding: 0 20px; }
}
</style>
