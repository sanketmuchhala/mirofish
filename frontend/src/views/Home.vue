<template>
  <div class="home-container">

    <!-- ── Navbar ─────────────────────────────────────────────── -->
    <nav class="navbar">
      <div class="nav-brand">GTM SIM LAB</div>
      <div class="nav-links">
        <a href="#simulate" class="nav-cta">Start Simulation</a>
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
          <span class="hero-version">v0.1 · Open Source</span>
        </div>

        <h1 class="hero-title">
          Simulate your GTM<br>
          <span class="hero-title-accent">before you launch outreach.</span>
        </h1>

        <p class="hero-sub">
          Enter a product brief. Get 12 AI-generated buyer personas, 3 outreach angles
          tested against each one, 36 simulated reactions with scores and objections,
          and a GTM report with a 7-day outbound experiment plan — in under 2 minutes.
        </p>

        <div class="hero-actions">
          <a href="#simulate" class="btn-hero-primary">Run a Simulation →</a>
          <a href="https://github.com/sanketmuchhala/GTM-SImulator" target="_blank" class="btn-hero-ghost">View on GitHub ↗</a>
        </div>

        <div class="hero-stats">
          <div class="hero-stat">
            <span class="hero-stat-num">12</span>
            <span class="hero-stat-label">Buyer Personas</span>
          </div>
          <div class="hero-stat-sep"></div>
          <div class="hero-stat">
            <span class="hero-stat-num">3</span>
            <span class="hero-stat-label">Message Angles</span>
          </div>
          <div class="hero-stat-sep"></div>
          <div class="hero-stat">
            <span class="hero-stat-num">36</span>
            <span class="hero-stat-label">Buyer Reactions</span>
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

      <!-- ── Problem ────────────────────────────────────────────── -->
      <section class="problem-section">
        <div class="problem-inner">
          <div class="problem-label">The problem</div>
          <h2 class="problem-title">Founders test their GTM assumptions on real customers.</h2>
          <p class="problem-body">
            Most B2B founders spend weeks crafting cold outreach, only to discover the hard way that
            their ICP doesn't respond, their messaging misses the core objection, or they're
            targeting the wrong segment entirely. By the time real reply data comes in, the damage
            is done — wasted sends, lost time, and no clear direction on what to fix.
          </p>
          <p class="problem-body">
            GTM Simulation Lab gives you signal before you send. Run a full simulation of how your
            target buyers would respond to your outreach — before you spend a single credit on
            an email sequence.
          </p>
        </div>
      </section>

      <!-- ── What you get ──────────────────────────────────────── -->
      <section class="features-section">
        <div class="section-eyebrow">What the simulation produces</div>
        <div class="features-grid">

          <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">12 AI Buyer Personas</div>
            <div class="feature-desc">
              ICP-specific archetypes generated from your brief — each with distinct goals,
              pain points, buying triggers, objections, budget sensitivity, and skepticism level.
              Covers the full spectrum from eager early adopters to skeptical CFOs.
            </div>
            <div class="feature-tag">Founder Sellers · VP Sales · CFOs · SDR Managers · 8 more</div>
          </div>

          <div class="feature-card">
            <div class="feature-icon">💬</div>
            <div class="feature-title">3 Outreach Angles Tested</div>
            <div class="feature-desc">
              Pain-first, ROI-first, and Curiosity-first message variants — written by the AI
              against your product context and tested simultaneously against all 12 personas.
              Each message is under 80 words, founder-style, no buzzwords.
            </div>
            <div class="feature-tag">Pain-First · ROI-First · Curiosity-First</div>
          </div>

          <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">36 Simulated Buyer Reactions</div>
            <div class="feature-desc">
              Every persona × message combination generates an interest score, clarity score,
              trust score, likely objection, buying trigger, and a realistic simulated reply —
              so you know exactly where each angle lands.
            </div>
            <div class="feature-tag">Interest · Clarity · Trust · Objection · Simulated Reply</div>
          </div>

          <div class="feature-card feature-card--accent">
            <div class="feature-icon">📊</div>
            <div class="feature-title">GTM Report + 7-Day Experiment</div>
            <div class="feature-desc">
              Winning angle with reasoning, top objections with suggested rebuttals, best-fit ICP
              segment, risk signals, a recommended agentic workflow, and a day-by-day 7-day
              outbound execution plan you can run immediately.
            </div>
            <div class="feature-tag">Winner Analysis · Rebuttals · Risk Signals · 7-Day Plan</div>
          </div>

        </div>
      </section>

      <!-- ── How it works ──────────────────────────────────────── -->
      <section class="hiw-section">
        <div class="section-eyebrow">How it works</div>
        <h2 class="section-title">Five steps from brief to outbound plan.</h2>

        <div class="hiw-steps-full">
          <div class="hiw-step-full" v-for="(step, i) in steps" :key="i">
            <div class="hiw-sf-num">{{ String(i + 1).padStart(2, '0') }}</div>
            <div class="hiw-sf-title">{{ step.title }}</div>
            <div class="hiw-sf-desc">{{ step.desc }}</div>
          </div>
        </div>

        <div class="hiw-note">
          The simulation runs in under 2 minutes with a connected LLM API. No account required.
          Runs instantly in mock mode without an API key.
        </div>
      </section>

      <!-- ── Who it's for ──────────────────────────────────────── -->
      <section class="for-section">
        <div class="section-eyebrow">Built for</div>
        <h2 class="section-title">GTM-focused founders and sales teams.</h2>

        <div class="for-grid">
          <div class="for-card">
            <div class="for-icon">🚀</div>
            <div class="for-title">B2B Founders (1–25 employees)</div>
            <div class="for-desc">
              Doing founder-led cold outbound and looking for their first 10 customers.
              Use the simulation to validate ICP assumptions and find the message that
              actually gets replies — before launching a full sequence.
            </div>
            <ul class="for-list">
              <li>Which personas are most likely to convert</li>
              <li>Which message angle opens the most doors</li>
              <li>What objections to expect and how to handle them</li>
            </ul>
          </div>

          <div class="for-card">
            <div class="for-icon">🎯</div>
            <div class="for-title">GTM Teams Entering a New Segment</div>
            <div class="for-desc">
              Launching a new product line or moving upmarket. Use the simulation to
              pressure-test your new ICP before committing your outbound motion and
              SDR headcount to the wrong hypothesis.
            </div>
            <ul class="for-list">
              <li>Buyer readiness scoring for the new segment</li>
              <li>Side-by-side angle comparison across different personas</li>
              <li>Risk signals that could derail the new market entry</li>
            </ul>
          </div>

          <div class="for-card">
            <div class="for-icon">📈</div>
            <div class="for-title">Sales Leaders Building a Playbook</div>
            <div class="for-desc">
              Building a repeatable cold outbound process before scaling the team.
              Use the simulation to create a documented, data-backed playbook so new
              SDRs and AEs ramp faster on the right message.
            </div>
            <ul class="for-list">
              <li>Objection handling scripts derived from simulated reactions</li>
              <li>ICP prioritization based on buyer readiness scores</li>
              <li>Structured 7-day experiment to validate before scaling</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- ── Sample output ─────────────────────────────────────── -->
      <section class="sample-section">
        <div class="section-eyebrow">Sample output</div>
        <h2 class="section-title">Here's what you'll see after a simulation.</h2>

        <div class="sample-grid">

          <!-- Sample persona card -->
          <div class="sample-block">
            <div class="sample-block-label">Buyer Persona</div>
            <div class="sample-persona-card">
              <div class="spc-header">
                <div>
                  <div class="spc-name">Marcus Rivera</div>
                  <div class="spc-title">VP Sales · Series A SaaS · 45 employees</div>
                </div>
                <span class="spc-badge spc-badge--interested">✓ Interested</span>
              </div>
              <div class="spc-row">
                <span class="spc-label">GOAL</span>
                <span class="spc-val">Hit $2M ARR this year by scaling SDR outbound from 3 to 7 reps.</span>
              </div>
              <div class="spc-row">
                <span class="spc-label">OBJECTION</span>
                <span class="spc-chip">⚠ What's the actual meeting booking lift vs. our current process?</span>
              </div>
              <div class="spc-row">
                <span class="spc-label">SKEPTICISM</span>
                <div class="spc-skep">
                  <div class="spc-seg spc-seg--filled"></div>
                  <div class="spc-seg spc-seg--filled"></div>
                  <div class="spc-seg spc-seg--filled"></div>
                  <div class="spc-seg"></div>
                  <div class="spc-seg"></div>
                  <span class="spc-skep-label">3 / 5</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Sample reaction row -->
          <div class="sample-block">
            <div class="sample-block-label">Simulated Reaction (ROI-First angle)</div>
            <div class="sample-reaction-card">
              <div class="src-scores">
                <div class="src-score">
                  <span class="src-score-num src-green">8.2</span>
                  <span class="src-score-label">Interest</span>
                </div>
                <div class="src-score">
                  <span class="src-score-num src-amber">6.8</span>
                  <span class="src-score-label">Trust</span>
                </div>
                <div class="src-score">
                  <span class="src-score-num src-green">7.5</span>
                  <span class="src-score-label">Clarity</span>
                </div>
                <div class="src-verdict src-verdict--interested">✓ Interested</div>
              </div>
              <div class="src-reply">
                "40% more meetings is a strong claim. Was that team at our stage?
                Share the case study and I'll loop in my ops lead."
              </div>
              <div class="src-trigger">
                <span class="src-trigger-label">Buying trigger:</span>
                Peer-validated case study from a similarly sized team with the same sales motion.
              </div>
            </div>
          </div>

          <!-- Sample report snippet -->
          <div class="sample-block sample-block--wide">
            <div class="sample-block-label">GTM Report — Winner + Top Objections</div>
            <div class="sample-report-card">
              <div class="srep-winner">
                <span class="srep-star">★</span>
                <div>
                  <div class="srep-winner-label">WINNING ANGLE</div>
                  <div class="srep-winner-angle">ROI-First</div>
                  <div class="srep-winner-stats">7.1 avg interest · 8 interested · 3 neutral · 1 objection</div>
                </div>
              </div>
              <div class="srep-divider"></div>
              <div class="srep-objections">
                <div class="srep-obj-label">TOP OBJECTIONS</div>
                <div class="srep-obj-item">
                  <span class="srep-obj-freq">×4</span>
                  <span class="srep-obj-text">Show me the methodology — sounds like vendor math</span>
                </div>
                <div class="srep-obj-item">
                  <span class="srep-obj-freq">×3</span>
                  <span class="srep-obj-text">We already have a sales engagement tool for this</span>
                </div>
                <div class="srep-obj-item">
                  <span class="srep-obj-freq">×3</span>
                  <span class="srep-obj-text">What's the payback period and total cost?</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- ── Simulate Now ──────────────────────────────────────── -->
      <section class="simulate-section" id="simulate">
        <div class="simulate-header">
          <div class="section-eyebrow">Run your simulation</div>
          <h2 class="section-title">Fill in your GTM brief to get started.</h2>
          <p class="simulate-sub">
            Takes about 2 minutes. Uses your own LLM API key (OpenAI-compatible).
            No API key? Load the example simulation to see the full output in mock mode.
          </p>
        </div>

        <div class="simulate-layout">

          <!-- Left: quick checklist -->
          <div class="simulate-checklist">
            <div class="scl-header">What you'll need</div>
            <div class="scl-item">
              <span class="scl-check">✓</span>
              <span>Product name + one-paragraph description</span>
            </div>
            <div class="scl-item">
              <span class="scl-check">✓</span>
              <span>Ideal customer profile (company size, role, stage)</span>
            </div>
            <div class="scl-item">
              <span class="scl-check">✓</span>
              <span>Pricing model (even approximate)</span>
            </div>
            <div class="scl-item">
              <span class="scl-check">✓</span>
              <span>Primary pain point you're solving</span>
            </div>
            <div class="scl-item">
              <span class="scl-check">✓</span>
              <span>GTM goal (e.g. first 10 customers)</span>
            </div>
            <div class="scl-divider"></div>
            <div class="scl-note">
              Not sure where to start?
              <button class="scl-demo-link" @click="loadDemoScenario; scrollToForm()">
                Load the AI SDR example →
              </button>
            </div>
          </div>

          <!-- Right: Form panel -->
          <div class="form-panel" ref="formPanelRef">

            <div class="form-panel-header">
              <div class="form-panel-title">GTM Brief</div>
              <button class="demo-pill" @click="loadDemoScenario">
                ⚡ Try example
              </button>
            </div>

            <div class="form-panel-body">

              <div v-if="homeState === 'form'">
                <GTMBriefForm :loading="loading" :initialData="demoData" @submit="handleBriefSubmit" />
              </div>

              <div v-else-if="homeState === 'submitting'" class="state-loading">
                <div class="state-spinner"></div>
                <div class="state-loading-steps">
                  <div class="sls-step sls-done">✓ Brief validated</div>
                  <div class="sls-step sls-active">◉ Generating persona preview…</div>
                  <div class="sls-step sls-pending">○ Preparing simulation</div>
                </div>
              </div>

              <div v-else-if="homeState === 'preview'" class="state-preview">
                <div class="state-preview-header">
                  <span class="state-dot state-dot--ready"></span>
                  <span class="state-preview-title">Simulation ready — 3 personas generated</span>
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

              <div v-else-if="homeState === 'error'" class="state-error">
                <div class="state-error-icon">⚠</div>
                <div class="state-error-msg">{{ submitError || 'Submission failed. Check your connection and try again.' }}</div>
                <button class="btn-ghost" @click="resetForm">← Edit Brief</button>
              </div>

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
import { ref } from 'vue'
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
const formPanelRef = ref(null)

function loadDemoScenario() {
  demoData.value = { ...DEMO_BRIEF }
}

function scrollToForm() {
  const el = document.getElementById('simulate')
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
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

/* ── Navbar CTA ─────────────────────────────────────────────── */
.nav-cta {
  background: #111;
  color: #fff;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  padding: 7px 16px;
  border-radius: 7px;
  transition: background 0.15s;
}
.nav-cta:hover { background: #6366f1; }

/* ── Hero actions ───────────────────────────────────────────── */
.hero-actions {
  display: flex;
  gap: 12px;
  margin-bottom: 36px;
}

.btn-hero-primary {
  background: #111;
  color: #fff;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: 8px;
  transition: background 0.15s;
}
.btn-hero-primary:hover { background: #6366f1; }

.btn-hero-ghost {
  background: transparent;
  color: #555;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  padding: 12px 20px;
  border-radius: 8px;
  border: 1px solid #d5d5d5;
  transition: color 0.15s, border-color 0.15s;
}
.btn-hero-ghost:hover { color: #111; border-color: #999; }

/* ── Shared section structure ───────────────────────────────── */
.section-eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #6366f1;
  margin-bottom: 12px;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #111;
  margin: 0 0 40px;
  line-height: 1.2;
}

/* ── Problem section ────────────────────────────────────────── */
.problem-section {
  padding: 72px 0;
  border-top: 1px solid #ebebeb;
}

.problem-inner {
  max-width: 680px;
}

.problem-label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 16px;
}

.problem-title {
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #111;
  margin: 0 0 20px;
  line-height: 1.25;
}

.problem-body {
  font-size: 1rem;
  line-height: 1.75;
  color: #555;
  margin-bottom: 16px;
}

/* ── Feature cards ──────────────────────────────────────────── */
.features-section {
  padding: 72px 0;
  border-top: 1px solid #ebebeb;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.feature-card {
  border: 1px solid #e8e8e8;
  border-radius: 12px;
  padding: 24px;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.feature-card--accent {
  background: #f8f8ff;
  border-color: rgba(99,102,241,0.2);
}

.feature-icon { font-size: 24px; }

.feature-title {
  font-size: 14px;
  font-weight: 700;
  color: #111;
  line-height: 1.3;
}

.feature-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.65;
  flex: 1;
}

.feature-tag {
  font-size: 11px;
  color: #888;
  background: #f4f4f4;
  border-radius: 4px;
  padding: 4px 8px;
  line-height: 1.4;
}

/* ── How it works (full) ────────────────────────────────────── */
.hiw-section {
  padding: 72px 0;
  border-top: 1px solid #ebebeb;
}

.hiw-steps-full {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0;
  margin-bottom: 28px;
  position: relative;
}

.hiw-steps-full::before {
  content: '';
  position: absolute;
  top: 18px;
  left: 5%;
  right: 5%;
  height: 1px;
  background: #e0e0e0;
  z-index: 0;
}

.hiw-step-full {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0 12px;
  position: relative;
  z-index: 1;
}

.hiw-sf-num {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #fff;
  border: 2px solid #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: #6366f1;
  margin-bottom: 14px;
  flex-shrink: 0;
}

.hiw-sf-title {
  font-size: 13px;
  font-weight: 700;
  color: #111;
  margin-bottom: 8px;
}

.hiw-sf-desc {
  font-size: 12px;
  color: #888;
  line-height: 1.5;
}

.hiw-note {
  font-size: 13px;
  color: #aaa;
  text-align: center;
  padding-top: 16px;
  border-top: 1px solid #f0f0f0;
}

/* ── Who it's for ───────────────────────────────────────────── */
.for-section {
  padding: 72px 0;
  border-top: 1px solid #ebebeb;
}

.for-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.for-card {
  border: 1px solid #e8e8e8;
  border-radius: 12px;
  padding: 28px;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.for-icon { font-size: 24px; }

.for-title {
  font-size: 14px;
  font-weight: 700;
  color: #111;
  line-height: 1.3;
}

.for-desc {
  font-size: 13px;
  color: #666;
  line-height: 1.65;
}

.for-list {
  list-style: none;
  padding: 0;
  margin: 0;
  border-top: 1px solid #f0f0f0;
  padding-top: 12px;
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.for-list li {
  font-size: 12px;
  color: #555;
  padding-left: 14px;
  position: relative;
  line-height: 1.5;
}

.for-list li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: #6366f1;
  font-size: 11px;
}

/* ── Sample output ──────────────────────────────────────────── */
.sample-section {
  padding: 72px 0;
  border-top: 1px solid #ebebeb;
}

.sample-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.sample-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sample-block--wide {
  grid-column: 1 / -1;
}

.sample-block-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
}

/* Sample persona card */
.sample-persona-card {
  border: 1px solid #e8e8e8;
  border-left: 3px solid #4ade80;
  border-radius: 10px;
  padding: 18px;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.spc-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 10px;
}

.spc-name { font-size: 14px; font-weight: 700; color: #111; }
.spc-title { font-size: 11px; color: #888; margin-top: 2px; }

.spc-badge {
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
  flex-shrink: 0;
}

.spc-badge--interested { background: #dcfce7; color: #15803d; }

.spc-row {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  font-size: 12px;
}

.spc-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #aaa;
  text-transform: uppercase;
  min-width: 70px;
  padding-top: 2px;
}

.spc-val { color: #333; line-height: 1.5; }

.spc-chip {
  font-size: 11px;
  color: #b91c1c;
  background: #fee2e2;
  border: 1px solid #fecaca;
  border-radius: 4px;
  padding: 2px 8px;
  line-height: 1.5;
}

.spc-skep { display: flex; align-items: center; gap: 3px; }

.spc-seg {
  width: 10px;
  height: 4px;
  border-radius: 2px;
  background: #e8e8e8;
}

.spc-seg--filled { background: #ea580c; }

.spc-skep-label { font-size: 11px; color: #888; margin-left: 6px; }

/* Sample reaction card */
.sample-reaction-card {
  border: 1px solid #e8e8e8;
  border-left: 3px solid #6366f1;
  border-radius: 10px;
  padding: 18px;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.src-scores {
  display: flex;
  gap: 16px;
  align-items: center;
}

.src-score {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.src-score-num {
  font-size: 20px;
  font-weight: 700;
  line-height: 1;
}

.src-score-label { font-size: 10px; color: #aaa; }

.src-green  { color: #16a34a; }
.src-amber  { color: #d97706; }

.src-verdict {
  margin-left: auto;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 4px;
}

.src-verdict--interested { background: #dcfce7; color: #15803d; }

.src-reply {
  font-size: 13px;
  font-style: italic;
  color: #444;
  line-height: 1.6;
  padding: 10px 14px;
  background: #f8f8f8;
  border-radius: 6px;
  border-left: 2px solid #e0e0e0;
}

.src-trigger {
  font-size: 12px;
  color: #888;
  line-height: 1.5;
}

.src-trigger-label { font-weight: 700; color: #555; }

/* Sample report card */
.sample-report-card {
  border: 1px solid #e8e8e8;
  border-left: 3px solid #6366f1;
  border-radius: 10px;
  padding: 20px;
  background: #fff;
  display: flex;
  gap: 24px;
}

.srep-winner {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  flex: 1;
}

.srep-star { font-size: 20px; color: #d97706; }

.srep-winner-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #6366f1;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.srep-winner-angle { font-size: 16px; font-weight: 700; color: #111; }

.srep-winner-stats { font-size: 12px; color: #888; margin-top: 4px; }

.srep-divider { width: 1px; background: #ebebeb; flex-shrink: 0; }

.srep-objections { flex: 1; }

.srep-obj-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #aaa;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.srep-obj-item {
  display: flex;
  gap: 10px;
  align-items: baseline;
  margin-bottom: 8px;
}

.srep-obj-freq {
  font-size: 11px;
  font-weight: 700;
  color: #d97706;
  background: #fef3c7;
  padding: 1px 6px;
  border-radius: 3px;
  white-space: nowrap;
}

.srep-obj-text { font-size: 12px; color: #444; line-height: 1.4; }

/* ── Simulate section ───────────────────────────────────────── */
.simulate-section {
  padding: 72px 0 80px;
  border-top: 1px solid #ebebeb;
}

.simulate-header { margin-bottom: 40px; max-width: 600px; }

.simulate-sub {
  font-size: 14px;
  color: #666;
  line-height: 1.65;
  margin: -24px 0 0;
}

.simulate-layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 40px;
  align-items: start;
}

.simulate-checklist {
  position: sticky;
  top: 80px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.scl-header {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 4px;
}

.scl-item {
  display: flex;
  gap: 10px;
  font-size: 13px;
  color: #444;
  line-height: 1.5;
}

.scl-check {
  color: #16a34a;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 1px;
}

.scl-divider {
  height: 1px;
  background: #ebebeb;
  margin: 4px 0;
}

.scl-note {
  font-size: 12px;
  color: #888;
  line-height: 1.5;
}

.scl-demo-link {
  background: none;
  border: none;
  color: #6366f1;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  padding: 0;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.scl-demo-link:hover { color: #4f46e5; }

/* ── Responsive ─────────────────────────────────────────────── */
@media (max-width: 1100px) {
  .features-grid { grid-template-columns: repeat(2, 1fr); }
  .hiw-steps-full { grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .hiw-steps-full::before { display: none; }
}

@media (max-width: 900px) {
  .main-section { grid-template-columns: 1fr; }
  .how-it-works { position: static; }
  .hero-title { font-size: 2.2rem; }
  .hero-stats { flex-wrap: wrap; width: 100%; }
  .preview-personas { grid-template-columns: 1fr; }
  .main-content { padding: 40px 20px 0; }
  .navbar { padding: 0 20px; }
  .features-grid { grid-template-columns: 1fr; }
  .hiw-steps-full { grid-template-columns: 1fr; }
  .for-grid { grid-template-columns: 1fr; }
  .sample-grid { grid-template-columns: 1fr; }
  .sample-block--wide { grid-column: auto; }
  .sample-report-card { flex-direction: column; }
  .srep-divider { width: 100%; height: 1px; }
  .simulate-layout { grid-template-columns: 1fr; }
  .simulate-checklist { position: static; }
  .hero-actions { flex-direction: column; align-items: flex-start; }
  .section-title { font-size: 1.6rem; }
  .nav-cta { display: none; }
}
</style>
