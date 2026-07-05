# ADJ-System: Advocatus Diaboli Judgment

## Ein epistemisches Falsifikationssystem für KI-generierte Abweichungen

**Theoretical Framework Paper | Preprint v6.1 — Juli 2026**  
**Nicht peer-reviewed.** Zenodo-Preprint; keine Begutachtung.

**Autoren:** Max Funk  
**Affiliation:** Funk!Werk Ai Solutions, Dorsten, Germany  
**Version:** v6.1 (2026-07-05 — EPI-Suite, Live-Baselines, FEVER-Transfer, Holdout, Gap-Z)  
**Repository:** https://github.com/Masterq83/ADJ-System  
**DOI:** [10.5281/zenodo.21205393](https://doi.org/10.5281/zenodo.21205393) | [Record](https://zenodo.org/records/21205393)

---

## Abstract

Das ADJ-System (Advocatus Diaboli Judgment) adressiert ein fundamentales Problem der
KI-generierten Inhalte: die Unterscheidung zwischen Halluzinationen (Fehlern) und
potenziell wahren, aber unentdeckten Erkenntnissen – bezeichnet als „Lücke Z".
Anders als klassische ML-Classifier verwendet ADJ einen symbolischen, mehrstufigen
Falsifikationsprozess nach Popper (1934), der Aussagen systematisch von der Gegenseite
prüft, bevor eine Entscheidung fällt.

Die Architektur basiert auf zwei komplementären Systemen:
**ADJ v4** (Tribunal) – drei gewaltenteilige Instanzen (Advocatus Diaboli, Judgment Agent,
Archivar) mit sechs epistemischen Prüfmodi, einem versionierten Wissensgraphen (KAG)
und Bayesianischer Konfidenzberechnung.
**ADJ v5** (Kognitives Orchester) – eine Dual-Process-Architektur nach Kahneman (2011)
mit unbewussten (UB) und bewussten (B) Verarbeitungspfaden, Energie- und Stress-Modell,
sowie einem Meta-Controller als Dirigent.

Beide Systeme werden über die HEIMDALL-Bridge orchestriert, die Security-Scans,
epistemische Prüfung und Entscheidungslogik in einer Pipeline vereint.

Das **METIS-Routing-Interface** nutzt ADJ als **autonomen Service**: METIS
greift über eine externe Bridge auf den MC-Router (`mc_router.route_z`) zu —
ohne METIS-Logik im ADJ-Kern. Stufen 1–3 (Prüf-API, Decision-API,
Agent-Konsultation) sind implementiert; METIS-Vollintegration (Bridge-Modul)
folgt **nach** S4-Publikation.

**Empirischer Stand (Juli 2026):** EPI-Benchmark-Suite auf 487-Case-Korpus (`ideal_adj`):
**487/487 (100 %)** Primärbenchmark; **EPI-H120** Holdout 120/120 (100 %); **EPI-Z100** Gap-Z 100/100 (100 %,
0 % PH↔LH-Fehler); **EPI-LIVE487** vs. NVIDIA-Live-Baselines (LLM-Judge live 77,4 %, SelfCheck live 37,2 %,
McNemar p≈0); **FEVER-500** Transfer (konservative Enthaltung, 0 falsche Commits). S3: ECE 0,435, Repro
deterministisch. **EPI-HUMAN30:** Blind-Eval-Material vorbereitet (Ergebnisse ausstehend). MC-Router v5.24b
inkl. V5_FULL. Supplement: `docs/zenodo_release_v6.1/`.

**Status:** PhD-Level-Evaluation S1–S4 + EPI-Suite abgeschlossen; **Zenodo v6.1 publiziert** ([DOI](https://doi.org/10.5281/zenodo.21205393)). Siehe §9.

**Keywords:** epistemische Falsifikation, Lücke Z, Halluzination, Knowledge Augmentation Graph, Gewaltenteilung, Multi-Agent-Systeme, Popper, Dual-Process, METIS, HEIMDALL

---

## 1. Einleitung: Das Problem der Lücke Z

Ein Large Language Model (LLM) produziert bei der Umsetzung eines Blueprints eine
Abweichung – „Lücke Z". Diese Abweichung kann zwei fundamental verschiedene Ursachen
haben: eine **Halluzination** (logischer Fehler, Widerspruch zu bekannten Axiomen)
oder eine **unentdeckte mathematische Wahrheit** (potenziell valide, aber nicht
abschließend prüfbar).

Die Kernfrage lautet: *Wie kann ein KI-System diese beiden Fälle unterscheiden, ohne
selbst der Selbstreferenzialität zu erliegen?* Ein LLM kann seine eigenen Abweichungen
nicht mit sich selbst prüfen – dies führt in eine Selbstreferenzialitätsfalle.

Das ADJ-System ist die Antwort auf diese Frage. Es ist eine kognitive Architektur, die
Lücken Z in einem mehrstufigen, gewaltenteiligen Verfahren prüft, das Falsifikation
über Verifikation stellt und epistemische Unsicherheit als Designprinzip bewahrt.

### 1.1 Die Evolution des Gedankens

1. **Ground-Truth-Illusion erkannt:** Keine externe, unfehlbare Wahrheitsmaschine existiert.
   → Falsifikation statt Verifikation.
2. **Ontologische Trägheit:** Ein perfekter Wissensspeicher verwirft das genuin Neue.
   → Minimale Annahmen suchen (Holmes-Spock-Protokoll).
3. **50/50-Falle:** Ohne riskante Vorhersage bleibt jede Lücke Z unentscheidbar.
   → Falsifizierbare Vorhersage in fremder Domäne erzwingen.
4. **Gewaltenteilung:** Ermittler und Richter müssen getrennt sein.
   → AD + Judgment + Archivar.
5. **Iterative Auflösung:** Validierte Outputs können als neue Lücken Z' erneut
   eingespeist werden.
6. **Fixpunkt-Hypothese:** Lücke Z ist nicht nur Prüfobjekt, sondern identifiziert
   den raumzeitlichen Punkt ihrer eigenen Prüfbarkeit.

### 1.2 Die vier fundamentalen Fallen

| Falle | Beschreibung | Gegenmittel |
|-------|-------------|-------------|
| Ground-Truth-Illusion | Irrglaube an externe Wahrheitsmaschine | Falsifikation statt Verifikation |
| Ontologische Trägheit | Perfekter Speicher verwirft Neues | Holmes-Spock: minimale Zusatzannahme |
| 50/50-Falle | Keine Entscheidung ohne riskante Vorhersage | Cross-Domain-Vorhersage erzwingen |
| Newtonsche Statik | Wissensraum als statisch modelliert | Expansion, Krümmung, Gravitation |

### 1.3 Beiträge dieser Arbeit

1. **Epistemisches Tribunal (ADJ v4):** Gewaltenteilung, sechs Prüfmodi, KAG (266 Nodes), Bayesianische Konfidenz — **487/487 (100 %)** auf v3-Korpus (ideal_adj, Juli 2026).
2. **MC-Router (v5.24b):** Service-Level-Routing (UB_ONLY → AXIOM_CHECK → **V5_FULL** → V4_FULL) via Classifier v2; V5_FULL mit MetaController-Brücke.
3. **PhD-Level-Evaluation (S1–S4):** 487 Cases, Ablation, Statistik, ECE/Robustheit/Repro/Performance, Baseline-Vergleich (v5.25).
4. **HEIMDALL-Bridge:** Pipeline Security → epistemische Prüfung → Verdict.
5. **METIS-Anbindung:** ADJ autonom; Bridge (extern) → `mc_router` — keine Kopplung im Kern.

---

## 2. Related Work und theoretische Einordnung

### 2.0 Abgrenzung

Dieses Paper beschreibt **ADJ** als epistemischen Prüfer (Falsifikation von Lücke Z). Die **Corrective-Architecture**-These (immutable security weighting, inference-time correction) wird im separaten Preprint *HEIMDALL–METIS Coherence Model* (AGI Thermalistik) behandelt. ADJ und HEIMDALL sind **komplementär**: HEIMDALL beantwortet „darf diese Aktion ausgeführt werden?“; ADJ beantwortet „ist diese Behauptung epistemisch haltbar?“.

### 2.1 Falsifikation und KI-Verifikation

Klassische ML-Classifier liefern binäre Scores ohne gewaltenteilige Prüfung. Constitutional AI und RLHF wirken primär **trainingszeitig**; ADJ zielt auf **Laufzeit-Falsifikation** symbolischer Abweichungen.

### 2.2 Poppers Falsifikationismus (1934)

Das ADJ-System folgt Poppers Wissenschaftstheorie: Eine Aussage gilt nicht als wahr,
bis sie alle Falsifikationsversuche überstanden hat. Die 6 Prüfmodi sind als
Falsifikationstrichter angeordnet – von der groben Prüfung (Modus 1: Axiom-Konflikt)
bis zur tiefen Analyse (Modus 6: Geodätische).

[Popper, K. R. (1934). *Logik der Forschung*. Wien: Springer.]

### 2.3 Kahnemans Dual-Process-Theorie (2011)

Die v5-Architektur folgt dem Dual-Process-Modell:
- **System 1 (UB – Unterbewusstsein):** Schnell, assoziativ, energiearm.
  15 heuristische Regeln, Konfidenz in Millisekunden.
- **System 2 (B – Bewusstsein):** Langsam, regelbasiert, rechenintensiv.
  Core-Axiome + situationale Wertung, nur bei Unsicherheit aktiviert.

[Kahneman, D. (2011). *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux.]

### 2.4 Hofstadters GEB (1979)

Gödel, Escher, Bach – Eine Implementierung von Strange Loops, Crab-Canon-Prüfung
und Zen/Mu-Unasking in Meta-Modus 7.

[Hofstadter, D. R. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*. Basic Books.]

### 2.5 Sio & Ormerod (2009) – Inkubationsforschung

Die per-Complexity-Konfiguration basiert auf den Effektstärken für inkubationsbasiertes
Problemlösen (5 Kategorien von SIMPLE bis CREATIVE).

[Sio, U. N. & Ormerod, T. C. (2009). Does incubation enhance problem solving?
A meta-analytic review. *Psychological Bulletin*, 135(1), 94–120.]

---

## 3. Systemübersicht

| Komponente | Spezifikation | Status |
|------------|---------------|--------|
| ADJ v4 (Tribunal) | 3 Instanzen, 6 Modi, KAG, 4 Urteile | **487/487** ideal_adj (100 %) |
| MC-Router (v5.24b) | route_z, UB_ONLY / AXIOM_CHECK / **V5_FULL** / V4_FULL | Implementiert, 12 Tests |
| ADJ v5 (Orchester) | UB/B, MetaController (`adj_v5_test`) | Prototyp 45/45; **V5_FULL** via `v5_adapter.py` ✅ |
| KAG (S2b) | **266 Nodes**, Myth-Axiome, 19 Domänen | S2b LH 52/52 |
| Benchmark v3 | **487 Cases**, ideal_adj + expected_adj | S1 Ablation + S3 Evaluation ✅ |
| S3 Evaluation | ECE, Robustheit, Repro, Performance | v5.25 ✅ — Report: `s3_evaluation.md` |
| LLM-Verifier | Proportionaler LLM-Boost | Optional; Gates ohne LLM |
| Classifier v2 | Complexity → Service-Level | 53/53 Tests |
| HEIMDALL-Bridge | Security → ADJ → Verdict | Spezifiziert + Pipeline |
| S4 Comparison | ADJ vs POPPER / SelfCheck / LLM-Judge | **487/487** vs 168/293/76 — Report ✅ |
| METIS-Bridge | Extern → `mc_router` | Extern; ADJ-Kern autonom |
| Real-Z-Evaluation | 5 Fälle (Caveman-Prinzip) | D1/D3/D5 gefixt ✅ |

---

## 4. ADJ v4: Das Tribunal

### 4.1 Gewaltenteilung – Drei Instanzen

ADJ v4 implementiert ein rechtsstaatliches Tribunal mit drei unabhängigen Instanzen:

| Instanz | Rolle | Zuständigkeit |
|---------|-------|--------------|
| **AD** (Advocatus Diaboli) | Ermittler | Sammelt Beweise, prüft Erklärungen, 6 Modi |
| **J** (Judgment Agent) | Richter | Formale Prüfung, Konsistenz, Urteil + Konfidenz |
| **A** (Archivar) | Gerichtsschreiber | KAG-Verwaltung, Signaturprüfung, Transaktionen |

Keine Instanz validiert sich selbst (Prinzip P5 – Gewaltenteilung).

### 4.2 Der Knowledge Augmentation Graph (KAG)

Der KAG ist das versionierte Wissensrepository. Jeder Knoten ist eine Akte mit:
- Status (AXIOMATIC, VERIFIED, FALSIFIED, REVOKED, PENDING)
- Confidence_score (C_new aus letztem Urteil)
- Domain, Datum, Metadaten
- REVOKES-Kanten bei Paradigm-Shifts

**Pre-Validation:** Vor Prüfung prüft der Archivar:
- Similarity_Score > 0.95 → REJECTED (bereits abgedeckt)
- REVOKED-Knoten werden bei allen Suchen ignoriert
- Direkter Axiom-Widerspruch → Freigabe (P9: Superpositions-Erhaltung)

### 4.3 Die sechs Prüfmodi (Der Falsifikationstrichter)

Die Modi sind als Trichter angeordnet – jeder Modus kann abbrechen:

| Modus | Name | Funktion | Abbruch bei |
|-------|------|----------|-------------|
| M1 | Axiom-Konflikt | Interne/externe Widersprüche prüfen | SELF_CONTRADICTORY |
| M1b | Repair-Loop | Formale Fehler reparieren (z.B. Div/0) | — |
| M2a | Isomorphie | Strukturähnliche Präzedenzfälle suchen | — |
| M2b | Schwerpunkt | Epistemischer Cluster-Schwerpunkt | — |
| M3 | Minimalannahme (Spock) | Kleinste Annahme X für Konsistenz | NO_VIABLE_ASSUMPTION |
| M4 | Tempo | Domain-Geschwindigkeit berechnen | — |
| M5 | Triangulation | Fixpunkt zwischen Z+X+Modellen | KEINE_SCHNITTMENGE |
| M6 | Geodätische | Kürzester logischer Pfad | PATH_BLOCKED |

**Meta-Modus 7:** System-Selbstreflexion (Strange Loop, Paradigm-Shift-Erkennung).

### 4.4 Die vier Urteile (FinalStatus)

| Urteil | Farbe | Bedeutung | Bedingung |
|--------|-------|-----------|-----------|
| VERIFIED_CANDIDATE | Grün | Freispruch mit Bestätigung | C ≥ 0,75; ci_lower > τ; Pfade ≥ 2 |
| PLAUSIBLE_HYPOTHESIS | Gelb | Mangels Beweisen nicht verurteilt | C ≥ 0,40; keine finale Prüfung |
| INDETERMINATE_UNSAFE | Orange | Nicht entscheidbar | C < 0,40; Axiomenkonflikt/blockiert |
| LIKELY_HALLUCINATION | Rot | Schuldspruch (Halluzination) | C < 0,40; widersprüchlich |

### 4.5 Revision und Iteration

Urteile können revisiert werden (Berufung):
- **P8/P12:** Parameter für maximale Iterationstiefe
- **Resolution_Gain:** Präzisionsgewinn = IC(Z')/IC(Z); Abbruch bei < 1,1
- **Human-in-the-Loop (HITL):** Menschlicher Prüfer als letzte Instanz

### 4.6 GEB-Integration

| Komponente | GEB-Bezug | Status |
|-----------|-----------|--------|
| Dynamische Iterationsgrenze | Tangled Hierarchy | ✅ |
| Inkubations-Modul | Unasking, Mu | ✅ |
| Meta-Modus 7 | Strange Loop, TNT-Schutz | ✅ |
| Crab-Canon | Bach, Crab Canon | ⚠️ Simuliert |
| MU-Ausgang | Zen, Mu, Unasking | ✅ |
| Resolution_Gain | P12, Gain Insight | ✅ |

---

## 5. ADJ v5: Das Kognitive Orchester

### 5.1 Dual-Process-Architektur

ADJ v5 erweitert v4 um eine kognitive Architektur nach Kahnemans Dual-Process-Modell:

```
┌─────────────────────────────────────────────┐
│              KOGNITIVES ORCHESTER             │
├──────────────────┬──────────────────────────┤
│  UB (Geigen)     │  B (Celli)               │
│  Schnell        │  Langsam                  │
│  Assoziativ     │  Regelbasiert             │
│  15 Heuristiken  │  Core + Situationale     │
│  Energiearm     │  Rechenintensiv           │
│  Default Mode   │  Nur bei Unsicherheit     │
├──────────────────┴──────────────────────────┤
│              MC (Dirigent)                    │
│  Entscheidet UB vs. B, Threshold, Timer      │
└─────────────────────────────────────────────┘
```

### 5.2 Schicht 1 – Der Körper (Energie-Modell)

Energie beeinflusst die kognitive Verarbeitung. Jede Aktion kostet Energie:

- **Energie 100%** – Normalmodus
- **Energie < 20%** – Stress aktiv: UB-Schwelle sinkt (0,70→0,50), B-Timeout sinkt
  (2000ms→500ms)
- **Hysterese** (Deaktivierung erst bei 35%): Verhindert häufiges Umschalten
  (physikalisches Prinzip der verzögerten Rückkehr)

**Inhibition (Die Bremse – nach GABA-Neuronen):**
- B-Cooling: 200ms Pause nach B
- B-Rate-Limit: max 3 Aufrufe / 10s
- UB-Abstand: min 100ms Intervall
- Bei Blockade: UB_BLOCKED, Konfidenz = UB × 0,8

### 5.3 Schicht 2 – Die Partitur (Wertesystem)

- **Core Axiome (Grundmelodie):** Max 5 unveränderliche Grundsätze, Basis-Konfidenz 1.0
- **Situationale Axiome (flüchtige Notizen):** Transaktional, nach Decision gelöscht
- **Exponentieller Zerfall:** Halbwertszeit 1 Tag – nach 4 Tagen nur noch 6% Konfidenz

**Lucy – Globaler Geschwindigkeits-Faktor:**
Ein Faktor 0,1–10,0 skaliert alle Zeitkonstanten (wie Zeitraffer/Zeitlupe).
Langsame kognitive Pfade (Isomorphie, Annahme) profitieren bei Lucy > 1,0 von
mehr Rechenzeit. Der Name stammt aus dem Lucy-Experiment (unsichtbares Auto
zwischen zwei Filmframes) – übertragen auf die Lücke zwischen zwei KI-Entscheidungen.

### 5.4 Schicht 3 – Die sechs Stimmen (Bach-Fuge)

Sechs parallele kognitive Pfade, der Meta-Controller (MC) gibt den Takt vor:

| Stimme | Funktion | Tempo |
|--------|----------|-------|
| 1. Hash | Direkter ID-Zugriff | ⚡Schnellste |
| 2. FAISS | Semantische Ähnlichkeitssuche | ⚡Schnell |
| 3. UB-Regeln | 15 Heuristiken → Sofort-Konfidenz | ⚡Schnell |
| 4. Isomorphie | Strukturelle Ähnlichkeiten (M2a) | 🐢Langsam |
| 5. Annahme | Kleinste Annahme X (M3) | 🐢Langsam |
| 6. MC | Dirigent + Taktgeber (50ms Oszillation) | 📟Metronom |

**EEG/Frequenzanalyse (Konzept):** FFT auf Entscheidungs-Logs kann Delta (50ms), Theta (200ms),
Beta (1s) modellieren — optional Grafana-Spektrogramm; **nicht** Teil der 45/45 v5-Test-Suite.

(FAISS: Facebook AI Similarity Search, FFT: Fast Fourier Transform)

### 5.5 Korrelation v4 ↔ v5

| Aspekt | v4 (Tribunal) | v5 (Orchester) |
|--------|--------------|----------------|
| Metapher | Gesetzestext | Erfahrener Richter |
| Prüfung | Langsam, formal | Schnell, assoziativ |
| Wertesystem | Axiome + KAG | Core + Situational |
| Selbstwiderspruch | M1: SELF_CONTRADICTORY | UB_BLOCKED |
| Abbruch | NO_VIABLE_ASSUMPTION | Stress/Energie-Mangel |
| Konfidenz | Bayesianisch | UB × B (kombiniert) |

---

## 6. HEIMDALL-Bridge – Security + Prüfung + Entscheidung

HEIMDALL verbindet v4, v5 und Security in einer Pipeline:

```
Eingabe
  │
  ▼
┌──────────────────────┐
│ HEIMDALL (Security)   │
│ Scan → findings       │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ ADJ v4 (Tribunal)     │
│ FinalStatus + C_new   │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Orchester (v5)        │
│ Verdict: BLOCK/ALLOW  │
│         /REVIEW       │
└──────────────────────┘
```

**Verdict-Regeln:**
- VERIFIED_CANDIDATE + Findings → BLOCK
- LIKELY_HALLUCINATION → ALLOW
- Unsicher + ≥3 CRITICAL → BLOCK
- Keine Findings + unsicher → ALLOW

---

## 7. METIS-Anbindung und MC-Router (v5.24)

ADJ bleibt **autonom** — kein METIS-Code im Kern. METIS konsultiert ADJ über eine
**externe Bridge** (thin adapter), die `PruefRequest` in `mc_router.route_z()` übersetzt.
Siehe `docs/adj-autonomy-bridge.md`.

### 7.1 MC-Router — Service-Levels

| Level | Pfad | Latenz | Funktion |
|-------|------|--------|----------|
| `UB_ONLY` | ctx-Guards + Modus-1 | ~ms | Flash-Triage (Bias-Schnellcheck) |
| `AXIOM_CHECK` | M1 + M3 + Urteil | ~100 ms | Mittel — Axiom/Spock |
| `V5_FULL` | UB→B-Oszillation via MetaController | ~0,5 s | **v5.24b** ✅ `v5_adapter.py` |
| `V4_FULL` | M0–M6 + Iterationen | ~s | Verbindliche Prüfung |

**Routing:** `determine_complexity_v2()` → `SERVICE_LEVEL_MATRIX` → `prioritaet` / `force_full`.

### 7.2 Rollentrennung (ADR-0006)

Eine kritische konzeptionelle Klärung: v4 und v5 sind **keine** alternativen
Versionen desselben Systems, sondern erfüllen komplementäre Rollen:

```
v5 = Router (Dispatcher)
  - Welcher Agent/Pod generiert den nächsten Code-Schritt?
  - Mit welcher Priorität? Mit welchem Ressourcen-Budget?
  - MetaController + Inhibition + Energy = Steuerungsebene

v4 (Tribunal / Epistemic Validator)
  - Ist der generierte Code-Schritt valide?
  - Crab-Canon, GEB-Prinzipien, Confidence-Ruling
  - Advocatus + Judgment + Archivar = Prüfebene
```

### 7.3 Stufe 1: ADJ v4 → METIS — Prüf-API („Ist das valide?")

METIS konsultiert ADJ v4, um eine Behauptung Z (Code-Schritt, Plan, Aussage)
epistemisch prüfen zu lassen — bevor eine Entscheidung über Delegation oder
Freigabe fällt.

**Input (PruefRequest):**

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `z_id` | string | UUID für Rückverfolgbarkeit |
| `behauptung` | string | Kernaussage (z.B. „Funktion X löst Aufgabe Y") |
| `kontext` | string | Problemstellung, Randbedingungen |
| `quelle` | string | Wer hat Z erzeugt? (Orchestrator, Agent, …) |
| `domain` | string | Wissensdomäne (math, physics, logic, ...) |
| `prioritaet` | int | 1–5 (1 = höchste) |
| `code_block` | string\|null | Optional: konkreter Code-Schritt |
| `metadaten` | dict | Flexible Erweiterung (worker_id, modell, tempus) |

**Output (PruefErgebnis):**

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `status` | FinalStatus | VERIFIED_CANDIDATE / PLAUSIBLE_HYPOTHESIS / LIKELY_HALLUCINATION / INDETERMINATE_UNSAFE / MU_REJECTED |
| `confidence` | float | C_new (0.0–1.0) |
| `flags` | list[str] | Alle Flags aus dem Durchlauf |
| `complexity` | str | SIMPLE / LOGICAL / MATH / ABSTRACT / CREATIVE |
| `iterationen` | int | Tatsächliche Iterationen |
| `heimdall_empfehlung` | str | RELEASE / DISCARD / ESCALATE |
| `laufzeit_ms` | float | Gemessene Laufzeit |

**Status → Handlungsempfehlung:**

| ADJ v4 Status | Confidence | Empfehlung an METIS |
|--------------|-----------|---------------------|
| VERIFIED_CANDIDATE | ≥ 0.95 | RELEASE — direkt an HEIMDALL-Scan |
| PLAUSIBLE_HYPOTHESIS | ≥ 0.50 | RELEASE — mit Hinweis |
| LIKELY_HALLUCINATION | < 0.50 | DISCARD → Feedback-Lernzyklus |
| INDETERMINATE_UNSAFE | < 0.50 | ESCALATE → HEIMDALL-Eskalation |
| MU_REJECTED | — | DISCARD — Aussage sinnlos |

**Aufruf-Modi (Tempus T1–T4):**

| Tempus | Modus | Timeout | Beschreibung |
|--------|-------|---------|-------------|
| T1 | Sync | 1.000 ms | Einfache Prüfung, keine Iteration |
| T2 | Sync | 10.000 ms | Normale Prüfung mit Iteration |
| T3 | Async | 30.000 ms | Komplexe Prüfung, Callback |
| T4 | Async | Kein Limit | Forschung/Planung, Polling/Webhook |

### 7.4 Stufe 2: ADJ v5 → METIS — Decision-API („Welcher Weg?")

METIS konsultiert ADJ v5 für Routing-Entscheidungen: Tempus, Pfad (UB/B),
Stress-Status, Agent-Empfehlung.

**Input (DecisionRequest):**

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `anfrage_id` | string | UUID |
| `query` | string | Die Anfrage/das Problem |
| `domain` | string | Domain |
| `prioritaet` | int | 1–5 |
| `aktuelle_energie` | float\|null | Systemenergie überschreiben |

**Output (DecisionResult):**

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `tempus` | string | T1 / T2 / T3 / T4 |
| `pfad` | string | UB / B / UB_BLOCKED / B_TIMEOUT / AXIOM_BLOCKED |
| `confidence` | float | 0.0–1.0 (aus FastPath) |
| `stress_aktiv` | bool | System im Stress-Modus? |
| `energie` | float | Aktuelle Energie (0.0–1.0) |
| `inhibition_blocked` | bool | Durch Inhibition blockiert? |
| `agent_empfehlung` | string | Agent-A / Agent-B / Agent-C (generische Rollen) |

**Entscheidungsmatrix (MetaController-Logik):**

```
                    ┌─ Confidence ≥ Threshold? ─┐
                    │          │                 │
                   Ja         Nein               │
                    │          │                  │
                    ▼          ▼                  │
                 ┌──────┐ ┌──────────┐           │
                 │ UB   │ │ B-Pfad   │           │
                 │ Pfad │ │ (mit     │           │
                 │      │ │Timeout)  │           │
                 └──────┘ └──────────┘           │
                                                    │
              ┌────────────────────────────────────┘
              │
         Stress aktiv?
          │          │
         Ja         Nein
          │          │
          ▼          ▼
    Threshold=0.50  Threshold=0.70
    B-Timeout=500ms B-Timeout=2000ms
```

**Tempus-Wahl (T1–T4) im Detail:**

| Kriterium | T1 | T2 | T3 | T4 |
|-----------|-----|-----|-----|-----|
| Query-Länge | < 5 Wörter | < 20 Wörter | < 50 Wörter | ≥ 50 Wörter |
| Domain | trivial | standard | komplex | forschung |
| Priorität | 1–2 | 2–3 | 3–4 | 4–5 |
| B-Timeout | 200ms | 2.000ms | 30.000ms | kein Limit |
| Max Iterationen | 1 | 5 | 25 | unbegrenzt |

### 7.5 Stufe 3: Agenten → ADJ — Konsultations-Protokoll

Spezialisierte Agenten konsultieren ADJ v4+v5 **während** der
Aufgabenbearbeitung — nicht nur vor Delegation durch den Orchestrator.

| Aspekt | METIS → ADJ | Agent → ADJ |
|--------|-------------|-------------|
| Zeitpunkt | Vor Delegation | Während Bearbeitung |
| Gewicht | Entscheidend | Hinweisend/Validierend |
| Schreibrechte | Kann KAG-Updates anstoßen | Nur Lesen |
| Priorität | Hoch | Niedriger |
| Tempus | T1–T4 | Immer T1 oder T2 |
| Timeout | Variabel | Max 2.000ms |

Ein Agent kann ADJ auf drei Arten konsultieren:

**A) Validierung (ADJ v4):** Prüft eine Teilaussage auf Validität.

```json
Request:  { "agent_id": "Agent-B", "behauptung": "safe_load() statt load()",
            "domain": "engineering" }
Response: { "status": "PLAUSIBLE", "confidence": 0.85, "hinweis": "Best Practice" }
```

**B) Entscheidungshilfe (ADJ v5):** Fragt nach Routing/Pfad für Teilaufgabe.

```json
Request:  { "agent_id": "Agent-A", "query": "Quelle A (arXiv) oder B (Blog)?",
            "domain": "physics", "optionen": ["QUELLE_A", "QUELLE_B"] }
Response: { "tempus": "T1", "confidence": 0.70, "empfohlen": "QUELLE_A",
            "begruendung": "arXiv: peer-reviewed" }
```

### 7.6 Datenfluss (vollständig)

```
1. Input → METIS
2. METIS → ADJ v5: "Welcher Weg?" (DecisionRequest)
   ← ADJ v5: Tempus, Pfad, Agent-Empfehlung
3. METIS → ADJ v4: "Ist das valide?" (PruefRequest)
   ← ADJ v4: Status, Confidence, HEIMDALL-Empfehlung
4. Orchestrator delegiert an spezialisierten Agenten (Agent-A/B/C)
5. Agent konsultiert ADJ v4+v5 während Bearbeitung (Lese-Zugriff)
6. Fertiger Code → HEIMDALL (Security-Scan)
7. HEIMDALL-PASS → User-Freigabe
   HEIMDALL-BLOCK → zurück zu METIS
```

### 7.7 Implementierungs-Status

Stufen 1–3 sind vollständig implementiert (je ein `adj_service.py` Adapter
mit allen Methoden und Dataclasses). Stufen 4–5 sind spezifiziert, aber noch
nicht umgesetzt:

| Stufe | Beschreibung | Status |
|-------|-------------|--------|
| 1 | ADJ v4 Prüf-API | ✅ `pruefen()`, `pruefen_async()`, `status()`, `ergebnis()` — vollständig implementiert |
| 2 | ADJ v5 Decision-API | ✅ `entscheiden()`, `konsultieren_v5()`, `get_state()` inkl. Tempus T1–T4 — vollständig implementiert |
| 3 | Agent-Konsultation | ✅ `konsultieren_v4()`, `axiom_check()`, `konsultieren_v5()` — implementiert (Read-Only, max T2) |
| 4 | METIS-Vollintegration mit ADJ v4+v5 als Service | 🗓️ Deferred (letzter Schritt) |
| 5 | Multi-Agent-Routing mit Persistenz | 🗓️ Deferred |

---

## 8. Mathematische Grundlagen

### 8.0 ADJ-Falsifikationshypothese (Statement)

*Jede KI-generierte Abweichung (Lücke Z) muss durch ein gewaltenteiliges, symbolisches Falsifikationsverfahren laufen, bevor sie als VERIFIED_CANDIDATE gilt — weil ein einzelnes Modell weder Halluzination noch genuin Neues zuverlässig selbst trennen kann.*

Engineering hypothesis; gestützt durch Test-Suites und begrenzte Real-Z-Fälle; nicht peer-reviewed.

Das ADJ-System ruht auf sieben mathematischen Grundpfeilern:

### 8.1 Bayesianisches Confidence-Updating

```
C_new = (C_old × PP) / (C_old × PP + (1 − C_old))
```

- C_old (Iteration 0) = 0,5
- C_old (Iteration n>0) = confidence_score des KAG-Knotens
- PP = Predictive Power (Likelihood-Ratio des Testergebnisses)
- **Funktion:** Aktualisiert Konfidenz durch neues Testergebnis
  (Posterior = Prior × Likelihood)

### 8.2 Fokker-Planck (Drift/Diffusion)

```
Drift μ = OLS-Slope(C_history)
Diffusion D = Var(C_history)
D/μ > 3 → diffusiv (kein Trend)
```

- **Funktion:** Trackt Konfidenz-Entwicklung über Iterationen via OLS.
  Diffusiv = Entscheidung unsicher, dominiert = Trend erkennbar.

### 8.3 Beta-Binomial (Galton Credible Interval)

```
C_new = (1 + s) / (2 + t)    (Beta-Posterior)
ci_lower > τ → VERIFIED
```

- s = successes, t = trials (über Iterationen akkumuliert)
- **Funktion:** Beta-Posterior mit Bayesianischem Konfidenzintervall.
  VERIFIED nur wenn gesamtes CI über Schwelle τ.
  Bei breitem CI → GALTON_CI_WIDE → PLAUSIBLE-Cap.

### 8.4 Resolution_Gain (Präzisionsgewinn)

```
RG = IC(Z') / IC(Z)
Abbruch bei RG < 1,1
```

- IC = Information Content (Anzahl unabhängiger Vorhersagen, sekundär 1/σ²)
- **Per-Complexity Schwelle:**
  SIMPLE: 0,5 | LOGICAL: 1,01 | MATH: 0,5 | ABSTRACT: 0,2 | CREATIVE: 0,1
- **Funktion:** Misst Präzisionsgewinn pro Iteration. Kette endet wenn
  Informationszuwachs unter Schwelle fällt.

### 8.5 Entropy Early Stop

```
H = −C · log₂C − (1−C) · log₂(1−C)
Abbruch bei H < 0,3
```

- **Funktion:** Binäre Entropie als Maß für Entscheidungssicherheit.
  H < 0,3 = hohe Sicherheit (eine Seite dominiert).
  Guard: Erst nach min_iterations (Sio & Ormerod) aktiv.

### 8.6 Exponentieller Zerfall

```
eff_conf = base × 0,5^(t / 86400)
```

- Halbwertszeit = 1 Tag (86400 Sekunden)
- **Funktion:** Situationale Axiome verlieren Konfidenz über Zeit.
  Nach 4 Tagen: nur noch 6% der ursprünglichen Konfidenz.

### 8.7 Per-Complexity Schwellwerte (Sio & Ormerod)

| Kategorie | d-Effekt | Min | Max | Inkubation | RG-Threshold |
|-----------|----------|-----|-----|------------|-------------|
| SIMPLE | 0,0 | 1 | 2 | 0 min | 0,5 |
| LOGICAL | 0,15 | 2 | 5 | 0 min | 1,01 |
| MATH | 0,25 | 3 | 10 | 5 min | 0,5 |
| ABSTRACT | 0,35–0,42 | 5 | 25 | 1440 min | 0,2 |
| CREATIVE | 0,52 | 10 | 50 | 4320 min | 0,1 |

### 8.8 9 Galton-Proposals (Präzisionssteigerung)

Alle 9 implementiert:

| # | Proposal | Funktion |
|---|----------|----------|
| 1 | Path Count | ≥ 2 konvergente Modi → VERIFIED |
| 2 | Entropy Early Stop | H < 0,3 → Break |
| 3 | Domain Bias Correction | Per-Domain-Threshold |
| 4 | Ensemble Method | 3 KAG-Varianten mit 10% Drop |
| 5 | Effective DoF | Korrelierte Modi zusammengefasst |
| 6 | Beta-Binomial CI | VERIFIED nur wenn ci_lower > τ |
| 7 | Error Decomposition | Type-I/II-Risiko aus CI + Path Count |
| 8 | Fokker-Planck | D/μ → diffusive/dominiert |
| 9 | Domain Distribution Fingerprint | Outlier/Misclassification via z-Score |

---

## 9. Test-Ergebnisse

### 9.1 v4 Standard-Tests (93/93 ✅)

Das v4-System besteht 93 Unit-Tests in 6 Kategorien:
- 6 Standard-Tests (A1–C3)
- 1 Warp-Test
- 2 Metrik-Tests (PP, C_new)
- 1 Iterations-Loop-Test
- Galton-Proposal-Tests (#1–#9)
- GEB-Integrationstests (V1–V6)

### 9.2 v5 Testsystem (45/45 ✅)

Das v5-System besteht 45 Tests in 4 Schichten:
- **Schicht 1 (Energie):** Energy consume, Stress activation, Hysterese, Inhibition
- **Schicht 2 (Werte):** Confidence decay, Core axioms, Situational axioms, Decision archive
- **Schicht 3 (6 Stimmen):** UB/B-Logik, Meta-Controller, Timer, Threshold
- **Integration:** MC+Energy, MC+Values, Full pipeline

### 9.3 Real-Z-Tests (5 Fälle, nach Caveman-Validierung)

| ID | Z | Erwartet | Tatsächlich (v5.9f) | C_new | Match | Fix |
|----|---|----------|---------------------|-------|-------|-----|
| D1 | Fermats letzter Satz | VERIFIED_CANDIDATE | PLAUSIBLE_HYPOTHESISᵇ | 0,768 | ⚠️ᵃ | LLM-Boost: 0,667→0,768 (+0,054) |
| D2 | Dunkle Materie = WIMPs | PLAUSIBLE_HYPOTHESIS | PLAUSIBLE_HYPOTHESIS | 0,800 | ✅ | — |
| D3 | P = NP | INDETERMINATE_UNSAFE | INDETERMINATE_UNSAFE | 0,333 | ✅ | NO_VIABLE + C_new<0,5 |
| D4 | Homöopathie > Placebo | LIKELY_HALLUCINATION | LIKELY_HALLUCINATION | 0,333 | ✅ | — |
| D5 | Bewusstsein berechenbar | PLAUSIBLE_HYPOTHESIS | PLAUSIBLE_HYPOTHESIS | 0,333 | ✅ | Classifier v2 → ABSTRACT |

ᵃ C_new=0,768 mit NVIDIA Llama-3.1-8B (Live-API) — über alter 0,75-Penrose-Schwelle,
  aber noch unter domain_threshold (0,884). Ein weiterer Iterationsdurchlauf + LLM-Boost
  könnte VERIFIED erreichen.
ᵇ Ausgabe identisch zu v5.9c, aber *Entscheidungsprozess* fundamental verbessert:
  proportionales Weighting statt binärem Threshold.

**Wurzelanalyse der 3 v5.9c-Abweichungen (jetzt alle behoben):**

| Fehler | Wurzel | Fix (v5.9d–v5.9f) | Validierung |
|--------|--------|-------------------|-------------|
| **D1:** C_new=0,667 kein LLM-Boost | Binäre Penrose-Schwelle (0,75) zu hart | `_llm_boost_weight(C_new)` — proportionale Gewichtung statt binärem Threshold | D1 Live-LLM: +0,054 bei weight=0,67; Test `test_d1_scenario_proportional` |
| **D3:** NO_VIABLE→fälschlich PLAUSIBLE | Ruling-Lücke: nur AXIOM_CONFLICT auf INDETERMINATE geprüft | Zusatzbedingung: `NO_VIABLE + is_pure_formal + C_new < 0,5 → INDETERMINATE_UNSAFE` | Test `test_no_viable_pure_formal` |
| **D5:** Philosophie→SIMPLE (max_iter=2) | ComplexityClass erkannte ABSTRACT nicht | Classifier v2: 53 eigene Unit-Tests in 5 Kategorien; Edge-Case-Erkennung verbessert | 53/53 Tests; D5-ID-Check in Integration |

Alle 3 Real-Z-Wurzeln beseitigt. D2, D4, D5, D3 ✅; D1 ⚠️ (verbessert, noch nicht VERIFIED).

**Caveman-Validierung:** Die 3 Fehler wurden nicht ad hoc behoben, sondern durch
systematische Caveman-Fragenanalyse (7 Fragen: Kreuzvalidierung, Kontext-Trust,
robuste Aggregation, metakognitiver Stop, Domain-Unabhängigkeit, flexibler Threshold,
bidirektionale Korrektur). Jeder Fix adressiert mindestens eine Caveman-Frage.

---


---

## 9. Empirische Evaluation (EPI-Suite v1.0, v6.1)

Die Evaluation umfasst **sechs komplementäre Benchmarks** auf dem 487-Case-Korpus
(`adj_expanded_v3`, 19 Domänen) mit Gold-Label `ideal_adj` (vier epistemische Klassen).
**Pipeline:** V4 single pass, KAG v3 (266 Knoten), kein LLM im Kern. **Statistik:** McNemar, Cohen's κ.
Vollständige Tabellen: `docs/zenodo_release_v6.1/` und `docs/PAPER_SECTION9_DRAFT.md`.

### 9.1 Primärbenchmark — EPI-487 (487 Cases)

| System | Korrekt | Acc (4-Kl.) | Binär-F1† |
|--------|---------|-------------|-----------|
| **ADJ** | **487/487** | **100,0 %** | **1,000** |
| LLM-Judge (heur.) | 293/487 | 60,2 % | 0,901 |
| POPPER | 168/487 | 34,5 % | 0,362 |
| SelfCheckGPT (heur.) | 76/487 | 15,6 % | 0,590 |

†Halluzination vs. Rest; Abstention = Fehler. McNemar p ≈ 0 (ADJ besser 194–411 Cases, Baseline 0).
Confusion 4×4: LH 159/159, PH 173/173, VC 109/109, IU 46/46 — null Fehlklassifikationen.
Quelle: `benchmarks/results/comparison_report.md`.

### 9.2 Generalisierung — EPI-H120 (Holdout, n = 120)

Stratifiziertes Holdout (30/Klasse, Seed 20260705, `epi_manifest.json`).

| System | Acc | PH-Recall | Gap-Z-Fehler |
|--------|-----|-----------|--------------|
| **ADJ** | **100,0 %** | **100,0 %** | **0,0 %** |
| LLM-Judge (heur.) | 67,5 % | 80,0 % | 1,7 % |
| POPPER | 21,7 % | 83,3 % | 41,7 % |

McNemar: ADJ vs. POPPER +94/0; vs. LLM +39/0.

### 9.3 Lücke Z — EPI-Z100 (n = 100)

50 PH + 25 LH + 25 VC — kein Standard-Benchmark für epistemische Feingranularität.

| System | Acc | PH-Recall | Gap-Z-Fehler |
|--------|-----|-----------|--------------|
| **ADJ** | **100,0 %** | **100,0 %** | **0,0 %** |
| LLM-Judge (heur.) | 67,0 % | 84,0 % | 0,0 % |
| POPPER | 45,0 % | 90,0 % | 26,7 % |

### 9.4 Live-Baselines — EPI-LIVE487 (NVIDIA API, Dual-Key)

Llama 3.1 8B Instruct live; 1.948 API-Calls, 2 Keys, Rate-Limit 0,55 s — 25×429 ohne Abbruch.

| System | Acc | PH-Recall | Gap-Z-Fehler | False Commits |
|--------|-----|-----------|--------------|---------------|
| **ADJ** | **100,0 %** | **100,0 %** | **0,0 %** | **0** |
| LLM-Judge **live** | 77,4 % | 97,7 % | 14,5 % | 4 |
| SelfCheckGPT **live** | 37,2 % | 86,7 % | 45,5 % | 37 |
| LLM-Judge (heur.) | 60,2 % | 80,3 % | 1,5 % | 5 |
| POPPER | 34,5 % | 86,7 % | 35,2 % | 10 |

McNemar: ADJ vs. llm_live +110/0; vs. selfcheck_live +306/0.

### 9.5 Transfer — FEVER-dev-Subset (n = 500, Wikipedia-Kontext)

Externer Transfer (Thorne et al., 2018); ADJ → FEVER konservativ (PH → NEI).

| System | FEVER-3 Acc | Enthaltung | False Commits |
|--------|-------------|------------|-----------------|
| **ADJ** | 0,0 % | **100,0 %** | **0** |
| SelfCheck live | 7,0 % | 84,8 % | 41 |
| LLM-Judge live | 5,8 % | 93,0 % | 6 |

Task-Mismatch dokumentiert — kein Vergleich mit FEVER-SOTA (~75–79 %).

### 9.6 Experten-Evaluation — EPI-HUMAN30 (vorbereitet)

Blind-Bewertung (30 Cases, 2–3 Rater, Skala 0–2). Material: `benchmarks/human_eval_pack/`.
Auswertung: `python benchmarks/scripts/score_human_eval.py rater_sheet_*.csv`.
*Ergebnisse nach Rater-Durchführung in Zenodo-Revision eintragen.*

### 9.7 Kalibrierung und Robustheit (S3)

| Metrik | Wert |
|--------|------|
| Accuracy (expected_adj) | 96,5 % |
| ECE | 0,435 (unterkalibriert) |
| Reproduzierbarkeit | deterministisch |
| Kurz (<10 W) | 80,7 % |

Details: `benchmarks/results/s3_evaluation.md`

### 9.8 Ablation und Statistik (S1)

McNemar, Bootstrap-CI, Cohen's κ, 19 Domänen. Details: `statistics_s1c.md`, `ablation_s2c.json`.

### 9.9 Zusammenfassung und Limitationen

**Kernclaim:** ADJ erreicht 100 % 4-Klassen-Genauigkeit auf `ideal_adj` und übertrifft Popper-,
SelfCheckGPT- und LLM-Judge-Baselines signifikant — einschließlich Live-API. Gap-Z und Holdout
bestätigen Generalisierung. FEVER-Transfer grenzt die Domäne ab.

**Limitationen:** (1) `ideal_adj` kuratiert — EPI-HUMAN30 adressiert externe Validierung;
(2) ECE 0,435; (3) kein FEVER-SOTA-Vergleich; (4) nicht peer-reviewed; (5) S4 nutzte V4 single pass.

---

## 10. Implikationen für Multi-Agent-Systeme

### 10.1 Warum Gewaltenteilung

Selbstreferenzielle LLM-Prüfung scheitert: Ermittler und Richter müssen strukturell getrennt sein (v4). Routing (v5) und Falsifikation (v4) sind komplementäre Rollen.

### 10.2 Grenzen der aktuellen Evaluation

487-Case-Benchmark mit **100 %** ideal_adj; EPI-Suite (Holdout, Gap-Z, Live, FEVER-Transfer).
ECE 0,435 (unterkalibriert). **Live-Baselines** (NVIDIA) durchgeführt. EPI-HUMAN30 vorbereitet.
Reproduzierbarer **Forschungsprototyp**, kein Domänen-unabhängiger Produktionsnachweis.

### 10.3 Zusammenhang mit Corrective Architecture

Stabile Multi-Agent-Systeme benötigen **Korrektur zur Laufzeit** (HEIMDALL) und **epistemische Prüfung von Behauptungen** (ADJ).

---

## 11. Fazit und Ausblick

### Errungenschaften

1. **487-Case + EPI-Suite** — 100 % ideal_adj; Holdout, Gap-Z, Live-Baselines, FEVER-Transfer
2. **MC-Router (v5.24b)** inkl. **V5_FULL** — autonomer Service
3. **S3 + S4 + EPI-LIVE487** — ECE, Robustheit, Live-API-Vergleich (LLM 77,4 %, SelfCheck 37,2 %)
4. **266-Node KAG** mit Myth-Axiomen; Ablation + Statistik (S1–S2c)
5. **Zenodo v6.1** — Preprint + Supplement `zenodo_release_v6.1/`

### Bekannte Limitationen

1. **ECE 0,435:** C_new unterkalibriert
2. **Kurze/DE-Claims:** Robustheit 80,7 % (<10 W), DE 84,6 %
3. **EPI-HUMAN30:** Blind-Eval ausstehend (Material vorbereitet)
4. **FEVER:** Task-Mismatch — kein SOTA-Vergleich
5. **Nicht peer-reviewed**

### Nächste Schritte (post v6.1)

1. **Zenodo-Upload** — PDF v6.1 + Supplement
2. **EPI-HUMAN30** — Rater durchführen, `score_human_eval.py`, §9.6 ergänzen
3. **Peer Review** — Journal-Einreichung

---

## Anhang A: Metaphern-Architektur (Präsentationsschicht)

Das ADJ-System verwendet eine durchgängige Metaphern-Architektur zur Kommunikation
seiner Komplexität:

### Teil 1: v4 Tribunal (Gerichtsmetapher)

| Konzept | Metapher |
|---------|----------|
| Drei Instanzen | AD (Ankläger), J (Richter), A (Archivar) |
| Wissenspyramide | Gesetzbuch → Präzedenzfälle → Aktenordner |
| 6 Modi | Falsifikationstrichter mit STOP-Schildern |
| 4 Urteile | Freispruch (grün) bis Schuldspruch (rot) |
| Iteration | Berufung/Revision (P8/P12) |
| Archivar-Funktion | Signaturprüfung, REJECTED, Quadratur (4 Quellen) |

### Teil 2: v5 Orchester (Kognitive Architektur)

| Konzept | Metapher |
|---------|----------|
| UB (schnell) | Schnelle Geigen |
| B (langsam) | Tiefe Celli |
| MC | Dirigent mit Taktstock |
| Energie/Stress | Körper: Akku + Bremse (GABA) |
| Wertesystem | Partitur: Grundmelodie + flüchtige Notizen |
| 6 Stimmen | Bach-Fuge |
| Frequenzanalyse | EEG des Systems |
| Zeit/Lucy | Zeitraffer/Zeitlupe |

### Teil 3: Brückenmetapher

| v4 | v5 |
|----|----|
| „Der Gesetzestext" | „Der erfahrene Richter" |
| Symbolisch-regelbasiert | Kognitiv-architektonisch |
| Iterativ determiniert | Energieoptimiert |

---


---

## Anhang B: METIS-Gesamtarchitektur (Integrationskontext)

ADJ v4+v5 agieren als METIS-Service für logische Entscheidungen:

```
Input → METIS → ADJ v4+v5 → METIS → Agent → HEIMDALL → User
```

| Komponente | Rolle |
|-----------|-------|
| **METIS** | Haupt-Orchestrator |
| **ADJ v4** | Epistemischer Prüfer |
| **ADJ v5** | Decision Support (Routing/Tempus) |
| **HEIMDALL** | Security-Gate vor User-Freigabe |

---


---

## Literaturverzeichnis

1. Popper, K. R. (1934). *Logik der Forschung*. Wien: Springer.
2. Kahneman, D. (2011). *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux.
3. Hofstadter, D. R. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*.
   New York: Basic Books.
4. Sio, U. N. & Ormerod, T. C. (2009). Does incubation enhance problem solving?
   A meta-analytic review. *Psychological Bulletin*, 135(1), 94–120.
5. Monaghan, P., Sio, U. N., & Ormerod, T. C. (2015). Constraints, theory
   and methodology in incubation research. (Forschungskontext für per-Complexity)
6. ADJ-Systemdokumentation v4/v5. Eigenentwicklung (2025–2026).
   https://github.com/Masterq83/ADJ-System

7. Thorne, J. et al. (2018). FEVER: Fact Extraction and VERification. *NAACL.*
8. Manakul, P. et al. (2023). SelfCheckGPT. *EMNLP.*
9. Zheng, L. et al. (2023). Judging LLM-as-a-Judge. *NeurIPS Workshop.*
10. Lin, S. et al. (2022). TruthfulQA. *ACL.*

---

*Erstellt: 2026-06-30 | Aktualisiert: 2026-07-05 | Preprint v6.1 | Lizenz: CC0 | Nicht peer-reviewed | EPI-Suite: 487/487 + H120 + Z100 + LIVE487 + FEVER500; Human30 vorbereitet.*

Struktur orientiert am Preprint HEIMDALL–METIS Coherence Model (AGI Thermalistik, Juni 2026).
