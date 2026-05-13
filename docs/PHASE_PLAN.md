# Phase Plan

## Phase 0: Repo Audit + Documentation
**Goal:** Establish implementation foundation; document intent and architecture.
**Files affected:** `docs/` (new), `CLAUDE.md` (new)
**Acceptance criteria:**
- All docs created
- CLAUDE.md at repo root
- Existing app still runs unchanged
- Repo audit summary exists
**Do not:** Touch any existing Vue, Python, or config files.

---

## Phase 1: Rebrand and Copy Cleanup
**Goal:** Replace MiroFish identity with GTM Simulation Lab identity throughout the UI.
**Files likely affected:**
- `frontend/src/views/Home.vue`
- `frontend/index.html`
- `locales/en.json`
- `README.md`
- `package.json` (name/description)
**Acceptance criteria:**
- All visible UI text reflects GTM Simulation Lab branding
- "MiroFish", "swarm intelligence", "parallel digital world" copy replaced
- No functional code changes
**Do not:** Change routing, component structure, or backend.

---

## Phase 2: GTM Input Form
**Goal:** Replace the Step 1 file-upload flow with a structured GTM Brief input form.
**Files likely affected:**
- `frontend/src/components/Step1GraphBuild.vue` (replace upload with form)
- `frontend/src/views/Home.vue` (new hero CTA)
- `frontend/src/api/graph.js` (add `/api/gtm/brief` endpoint)
- `backend/app/api/gtm.py` (new blueprint, POST `/api/gtm/brief`)
- `locales/en.json` (new form field keys)

**Input fields:**
`product_description`, `icp`, `pricing`, `target_market`, `sales_channel`,
`main_pain_point`, `competitors`, `gtm_goal`

**Acceptance criteria:**
- User can fill form and submit
- Brief is stored as project context (file-system)
- Graph Build step replaced by Brief Review step
**Do not:** Remove the existing graph building logic — keep it intact alongside the new flow.

---

## Phase 3: Persona Generation
**Goal:** Generate 12 buyer persona types from the GTM brief.
**Files likely affected:**
- `backend/app/services/gtm_persona_generator.py` (new, adapts `oasis_profile_generator.py`)
- `backend/app/api/gtm.py` (add POST `/api/gtm/personas`)
- `frontend/src/components/Step2EnvSetup.vue` (show persona cards)
- `locales/en.json`
**Acceptance criteria:**
- 12 buyer personas generated with name, role, company size, pain point, skepticism level
- Personas displayed in Step 2 as review cards
- Fallback mock personas available if LLM unavailable
**Do not:** Change the existing OASIS profile format — add a GTM variant alongside it.

---

## Phase 4: Message Testing
**Goal:** Generate 3 outreach message variants and simulate buyer reactions per persona.
**Files likely affected:**
- `backend/app/services/gtm_message_generator.py` (new)
- `backend/app/services/gtm_reaction_simulator.py` (new)
- `backend/app/api/gtm.py` (add POST `/api/gtm/messages`, POST `/api/gtm/simulate`)
- `frontend/src/components/Step3Simulation.vue` (show message × persona matrix)
- `locales/en.json`
**Acceptance criteria:**
- 3 message angles: pain-led, ROI-led, social-proof-led
- Each persona reacts: interested / neutral / objection
- Objections captured as strings
- Matrix displayed in Step 3
**Do not:** Run OASIS social simulation — pure LLM generation is sufficient for MVP.

---

## Phase 5: Simulation Results
**Goal:** Surface aggregated results — response rates, top objections, segment readiness.
**Files likely affected:**
- `backend/app/api/gtm.py` (add GET `/api/gtm/results/<id>`)
- `frontend/src/views/SimulationRunView.vue` (replace action log with results dashboard)
- `locales/en.json`
**Acceptance criteria:**
- Estimated open/reply rate per message angle
- Top 3 objections ranked by frequency
- Segment readiness score (0–100) per persona group
- Data is JSON-first; UI renders from JSON
**Do not:** Add charts or data visualization libraries in this phase.

---

## Phase 6: GTM Report
**Goal:** Use existing `report_agent.py` ReACT pattern to generate a structured GTM recommendation.
**Files likely affected:**
- `backend/app/services/report_agent.py` (add GTM report mode / new prompt)
- `backend/app/api/gtm.py` (add POST `/api/gtm/report`, GET `/api/gtm/report/<id>`)
- `frontend/src/components/Step4Report.vue` (GTM report layout)
- `locales/en.json`

**Output sections:**
1. ICP Validation
2. Best Message Angle
3. Top 3 Objections + Rebuttals
4. Segment Readiness Summary
5. 7-Day Outbound Experiment

**Acceptance criteria:**
- Report renders in Step 4
- Markdown download works (reuse existing `/api/report/<id>/download`)
- Report can be generated from mock data (no live simulation required)
**Do not:** Change the existing report agent's graph-retrieval tools.

---

## Phase 7: Demo Polish
**Goal:** Make the end-to-end demo clean, fast, and credible enough for a live founder pitch.
**Files likely affected:**
- `frontend/src/views/Home.vue` (demo CTA, social proof)
- All Step components (loading states, progress indicators)
- `README.md` (updated setup instructions)
- `locales/en.json`
**Acceptance criteria:**
- Full demo flow under 3 minutes
- Graceful fallback to mock data if APIs unavailable
- Mobile-readable (not necessarily responsive, just not broken)
- README updated with demo quickstart
**Do not:** Add auth, billing, database, or deployment config.
