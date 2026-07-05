# ADJ-System — Metaphor Architecture

## v4: Tribunal (Judicial Metaphor)

| Concept | Metaphor | Implementation |
|---------|----------|---------------|
| AD (Advocatus Diaboli) | Prosecutor / Investigator | 6 epistemic modes (M1-M6) |
| J (Judgment Agent) | Judge | Formal consistency check, ruling, confidence |
| A (Archivar) | Court Clerk | KAG management, signature verification |
| KAG | Law library + Case files | Versioned knowledge graph |
| 6 Modes | Falsification funnel | Axiom → Isomorphy → Minimal assumption → Tempo → Triangulation → Geodesic |
| 4 Verdicts | Guilt/Innocence spectrum | VERIFIED (green) → PLAUSIBLE (yellow) → INDETERMINATE (orange) → LIKELY_HALLUCINATION (red) |
| Iteration | Appeal / Revision | P8/P12 config, Resolution_Gain precision check |
| HITL | Supreme Court | Human-in-the-loop as final instance |
| Pre-Validation | Clerk's pre-screening | Similarity > 0.95 → REJECTED, direct axiom conflict → release |

## v5: Orchestra (Cognitive Architecture)

| Concept | Metaphor | Implementation |
|---------|----------|---------------|
| UB (Fast) | Violins (quick, light) | 15 heuristics, millisecond confidence |
| B (Slow) | Cellos (deep, resonant) | Core + situational axioms, rule-based |
| MC | Conductor | Decides UB vs B, threshold, timer |
| Energy | Battery / Stamina | Resource consumption per action |
| Stress | Fight-or-flight | Threshold drops at <20% energy |
| Hysteresis | Thermostat deadband | Deactivates at 35% (not 20%) to prevent oscillation |
| Inhibition (GABA) | Brake system | B-cooling (200ms), B-rate-limit (3/10s), UB-interval (100ms) |
| Core Axioms | Main melody (Leitmotif) | Max 5 immutable principles, base confidence 1.0 |
| Situational Axioms | Fleeting notes | Transactional, deleted after decision, exponential decay (half-life 1 day) |
| Lucy | Time dilation | Global speed factor 0.1–10.0, scales all time constants |
| 6 Voices | Bach fugue | Hash → FAISS → UB rules → Isomorphy → Assumption → MC |
| MC Router (v5.24) | Conductor routing | `mc_router.py`: UB_ONLY / AXIOM_CHECK / V4_FULL via Classifier v2 |
| EEG / Frequencies | Brain waves of the system | FFT on decision logs, Delta (50ms), Theta (200ms), Beta (1s) |

## Bridge: HEIMDALL

| Concept | Metaphor |
|---------|----------|
| HEIMDALL | Gatekeeper / Watchman |
| Scan | Security checkpoint |
| Findings | Suspicious items |
| Verdict | BLOCK / ALLOW / REVIEW |

## v5 as Pre-Conscious

ADJ v5 is not a full consciousness model — it is a **pre-conscious cognitive architecture**:

- **Reactive, not reflective**: UB reacts (System 1), B deliberates (System 2), but neither has self-awareness
- **Orchestrated, not autonomous**: MC conducts but does not *choose* to conduct
- **Energy-driven, not intentional**: Behavior follows resource budgets, not goals
- **Analogy**: An orchestra playing from a score — beautiful, coordinated, but not aware of itself

The step from v5 (pre-conscious) to true AGI would require:
1. Meta-cognition (self-model)
2. Long-term intention formation
3. Cross-session learning (Phase 3 Step 11 — partial)
4. Theory of Mind (other-agent modeling)

## Design Origins (internal terms, not in publication)

| Term | Origin | Meaning |
|------|--------|---------|
| Lucy | Lucy experiment (invisible car between frames) | The gap between two decisions |
| Spock | Star Trek | Minimal assumption protocol (Holmes-Spock) |
| Soap bubble | Surface tension metaphor | Epistemic bubble of minimal assumptions |
| Franklin | Benjamin Franklin's moral algebra | Pros/cons weighting in decision |
| Wooden sticks | Children's construction toy | Building complex logic from simple primitives |
