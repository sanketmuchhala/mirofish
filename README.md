# GTM Simulation Lab

> **Simulate your GTM before launching outreach.**

An open-source AI simulation engine for B2B founders. Enter your product brief, ICP, and messaging strategy. Get back AI-generated buyer personas, message reaction simulations, ranked objections, and a ready-to-execute 7-day outbound experiment — before you send a single real email.

---

## What It Does

Most GTM failures happen because founders never tested their assumptions. This tool simulates what happens when your message hits real buyer types — at zero cost, in minutes.

| Step | What Happens |
|------|-------------|
| 1. **GTM Brief** | Describe your product, ICP, pricing, pain point, and GTM goal |
| 2. **Buyer Personas** | AI generates 12 distinct buyer archetypes from your ICP |
| 3. **Message Testing** | 3 outreach variants (pain-first, ROI-first, curiosity-first) tested against each persona |
| 4. **Buyer Reactions** | Each of 36 persona × message pairs generates interest scores, objections, and simulated replies |
| 5. **GTM Report** | Winner analysis, best ICP segment, top objections with rebuttals, risk signals, recommended workflow, and 7-day outbound experiment |

---

## Demo

Click **"⚡ Load Example Simulation"** on the home page to instantly pre-fill the form with a realistic AI SDR product scenario. No signup required.

The full flow runs in under 2 minutes (LLM-dependent). In mock mode, it runs instantly.

---

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- OpenAI-compatible LLM API key (or run in mock mode without one)

### Run with Docker

```bash
git clone https://github.com/sanketmuchhala/GTM-SImulator.git
cd GTM-SImulator
cp .env.example .env  # Add your LLM API key
docker compose up
```

Open [http://localhost:5173](http://localhost:5173)

### Run Manually

```bash
# Backend
cd backend
pip install -r requirements.txt
python run.py

# Frontend (separate terminal)
cd frontend
npm install
npm run dev
```

### Mock Mode (no LLM required)

```bash
MOCK_MODE=true docker compose up
```

Or append `?mock=true` to any API endpoint URL.
All GTM endpoints return pre-generated realistic data from `backend/mock_data/`.

---

## Architecture

```
GTM Brief
  → POST /api/gtm/brief           (persisted to uploads/)
  → POST /api/gtm/personas        (LLM → 12 buyer personas)
  → POST /api/gtm/messages        (LLM → 3 message variants)
  → POST /api/gtm/reactions       (LLM → 36 buyer reactions)
  → POST /api/gtm/report          (LLM + deterministic → GTM report)
  → Download .md                  (client-side markdown export)
```

All resources are cached per `brief_id` in `uploads/gtm_briefs/<brief_id>/`.
No database required. No auth required.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Vue 3 (Composition API), Vue Router, no Pinia |
| Backend | Flask, Python 3.11 |
| LLM | OpenAI-compatible API via `LLMClient` (`utils/llm_client.py`) |
| Persistence | File system (`uploads/gtm_briefs/`) |
| Mock data | `backend/mock_data/` JSON files |
| Simulation engine | OASIS (camel-ai) — underlying framework, not used in GTM flow |
| Memory layer | Zep Cloud — underlying framework, not used in GTM flow |

---

## Simulation Methodology

- All personas, reactions, and scores are **AI-generated**, not real buyer responses.
- The simulation is **directional signal** — useful for testing message angles and identifying likely objections before real outreach.
- Results should be **validated with real outbound** before making major GTM decisions.
- Each simulation run is deterministic per brief (idempotent API endpoints, cached results).

---

## Project Structure

```
frontend/src/
  views/          ← GTMPersonasView, GTMMessageTestingView, GTMReportView + 4 legacy views
  components/     ← GTMBriefForm, PersonaCard + legacy components
  mock/           ← gtm_preview, gtm_messages, gtm_report, gtm_demo (offline fallbacks)
  api/            ← gtm.js (API client), index.js (axios setup with retry)
  store/          ← gtmSimulation.js (reactive singleton session state)
  utils/          ← gtmFormatter.js, downloadMarkdown.js

backend/app/
  api/            ← gtm.py (all GTM routes), legacy blueprints
  services/       ← gtm_persona_generator, gtm_message_generator,
                     gtm_reaction_simulator, gtm_aggregator, gtm_report_generator
  models/         ← gtm_brief.py (GTMBrief dataclass + GTMBriefManager)
  utils/          ← llm_client.py, retry.py, logger.py

backend/mock_data/
  gtm_personas_full.json, gtm_messages.json, gtm_reactions.json, gtm_report.json
```

---

## FAQ

**How long does generation take?**
With an LLM: 30–90 seconds total (personas ~15s, messages ~10s, reactions ~30s, report ~20s). With `MOCK_MODE=true`: instant.

**Can I use my own LLM endpoint?**
Yes. Set `OPENAI_API_BASE` and `OPENAI_API_KEY` in your `.env` to point at any OpenAI-compatible API (Ollama, Azure OpenAI, Groq, etc.).

**Is this real buyer data?**
No. All personas, reactions, and scores are AI-generated. This is a simulation tool for testing GTM hypotheses, not a source of real market research.

**Can I export reports?**
Yes. The "Download GTM Report" button exports a complete `.md` file including all sections, the 7-day experiment, and a simulation disclaimer.

**Does it work offline?**
In mock mode, yes. The full UI renders with pre-generated data from `backend/mock_data/` and `frontend/src/mock/`.

---

## Roadmap

- [x] Phase 1 — Rebrand + copy cleanup
- [x] Phase 2 — GTM brief input form
- [x] Phase 3 — AI buyer persona generation
- [x] Phase 4 — Message testing + buyer reaction simulation
- [x] Phase 5 — GTM report + 7-day outbound experiment
- [x] Phase 6 — Demo polish + UX refinement
- [ ] Phase 7 — History view: browse past simulations by brief
- [ ] Phase 8 — Side-by-side brief comparison (A/B test two ICPs)
- [ ] Phase 9 — Real reply ingestion (paste actual replies, update simulation hypothesis)
- [ ] Phase 10 — Team workspace + shareable report links

---

## License

MIT
