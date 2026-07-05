# ADJ-System — Paper (Deutsch, Autor-Version v6.1)

**Advocatus Diaboli Judgment: Ein epistemisches Falsifikationssystem für KI-Abweichungen**

Version **v6.1** | 2026-07-05 | Max Funk, Funk!Werk Ai Solutions, Dorsten  
Repository: https://github.com/Masterq83/ADJ-System  
*Nicht peer-reviewed — [Zenodo Preprint v6.1](https://doi.org/10.5281/zenodo.21205393)*

> **Publiziert:** https://zenodo.org/records/21205393 · DOI [10.5281/zenodo.21205393](https://doi.org/10.5281/zenodo.21205393)

> **Hinweis:** Lesbare Normal-Sprache für dich. Zenodo-Fassung: `ZENODO_PUBLIKATION.md` (identischer Inhalt, formaler).

---

## Kurzfassung

Wenn eine KI vom Plan abweicht, ist das ein **Fehler** oder eine **mögliche neue Erkenntnis**? ADJ (Advocatus Diaboli Judgment) beantwortet das über **Popper-Falsifikation** und **Gewaltenteilung** — nicht über ein weiteres LLM, das sich selbst beurteilt.

**Architektur:** ADJ v4 (Tribunal: Ankläger, Richter, Archivar) + ADJ v5 (Orchester: schneller UB- und langsamer B-Pfad nach Kahneman) + MC-Router.

**Empirie (Juli 2026, EPI-Suite):**

| Benchmark | ADJ | Beste Baseline |
|-----------|-----|----------------|
| EPI-487 (n=487) | **100 %** | LLM 60,2 % |
| EPI-H120 Holdout | **100 %** | LLM 67,5 % |
| EPI-Z100 Lücke Z | **100 %** | LLM 67,0 % |
| EPI-LIVE487 (live API) | **100 %** | LLM-live **77,4 %** |
| FEVER-500 Transfer | Enthaltung | SelfCheck 7,0 % |

McNemar vs. Live-Baselines: p ≈ 0. FEVER: Task-Mismatch dokumentiert, 0 falsche Commits. EPI-HUMAN30: Material bereit, Rater ausstehend.

---

## 1. Das Problem: Lücke Z

| Fall | Bedeutung | Farbe (Metapher) |
|------|-----------|------------------|
| Halluzination | Widerspruch, Fehler | Rot |
| Plausible Hypothese | Raum für Neues, noch offen | **Gelb — Lücke Z** |
| Verifiziert | Hohe Evidenz | Grün |
| Unentscheidbar | Zu wenig Information | Orange |

**Kernproblem:** Ein LLM kann **sich nicht selbst verlässlich prüfen** — Ermittler und Richter müssen getrennt sein.

### Vier Fallen (ohne ADJ)

1. Ground-Truth-Illusion — keine externe Wahrheitsmaschine  
2. Ontologische Trägheit — perfekter Speicher verwirft Neues  
3. 50/50-Falle — ohne testbare Vorhersage keine Entscheidung  
4. Newtonsche Statik — Wissen ist dynamisch, nicht statisch  

---

## 2. Metaphern → Architektur → Erkenntnisweg

### Stufe 1 — Tribunal (v4): „Gericht statt Selbsturteil"

| Konzept | Metapher | Was es leistet |
|---------|----------|----------------|
| Advocatus Diaboli | Ankläger | Sucht aktiv Widerlegung (6 Modi) |
| Judgment Agent | Richter | Formales Urteil + Konfidenz |
| Archivar | Gerichtsschreiber | KAG, Signatur, Versionen |
| 6 Modi | Falsifikationstrichter | M1 Axiom → … → M6 Geodätisch |
| 4 Urteile | Ampel | LH / PH / VC / IU |
| Iteration | Berufung | P8/P12, Präzisionsgewinn |

**Erkenntnis:** Falsifikation vor Verifikation — Gelb (PH) ist **kein Fehler**, sondern epistemische Vorsicht.

### Stufe 2 — Orchester (v5): „Wann tief prüfen?"

| Konzept | Metapher | Was es leistet |
|---------|----------|----------------|
| UB | Geigen (schnell) | Heuristiken, ms |
| B | Celli (tief) | Regeln, Axiome |
| Meta-Controller | Dirigent | Routing, Tempo T1–T4 |
| Energie / Stress | Akku + Bremse | Ressourcensteuerung |
| MC-Router v5.24b | Taktstock | UB_ONLY → AXIOM → V5_FULL → V4_FULL |

**Erkenntnis:** Nicht jede Behauptung braucht volles Tribunal — Routing spart Latenz ohne PH zu opfern.

### Stufe 3 — Brücke: „Vom Bild zur Messung"

```
Metapher (verstehen) → Architektur (bauen) → Benchmark (beweisen) → Limitation (ehrlich)
```

---

## 3. ADJ v4 — Tribunal (technisch)

Drei Instanzen, sechs Modi, KAG (266 Knoten, 19 Domänen), Bayesianische Konfidenz C_new.

**Pipeline:** `run_investigation` → `run_judgment` — **kein LLM im Kern**.

---

## 4. ADJ v5 — Orchester (technisch)

Dual-Process nach Kahneman. V5_FULL über `v5_adapter.py` — echte UB→B-Oszillation.

---

## 5. ADJ als eigenständiger Service

Prüf-API (`PruefRequest` / `PruefErgebnis`), Decision-API, optional externe Anbindung — **Kern bleibt autonom**.

---

## 6. Empirische Evaluation (EPI-Suite v6.1)

**Gold:** `ideal_adj` (4 Klassen). **Statistik:** McNemar, Cohen's κ.

### 6.1 EPI-487 — Primärbenchmark

ADJ **487/487 (100 %)**. LLM-Judge 60,2 %, POPPER 34,5 %, SelfCheck 15,6 %. McNemar p ≈ 0.

### 6.2 EPI-H120 — Holdout

120/120 (100 %) — kein Overfit auf Entwicklungskorpus.

### 6.3 EPI-Z100 — Lücke Z

100/100 (100 %), **0 % PH↔LH-Fehler** — Kern-USP empirisch abgesichert.

### 6.4 EPI-LIVE487 — Live-Baselines

Gleiche Aufgabe, **live** NVIDIA API (Llama 3.1 8B):

| System | Acc |
|--------|-----|
| **ADJ** | **100 %** |
| LLM-Judge live | 77,4 % |
| SelfCheck live | 37,2 % |

### 6.5 FEVER-500 — Transfer

ADJ: 100 % Enthaltung (PH), **0 falsche Commits**. Kein FEVER-SOTA-Claim — dokumentierter Task-Mismatch.

### 6.6 EPI-HUMAN30 — ausstehend

Blind-Eval-Material: `benchmarks/human_eval_pack/`

### 6.7 S3 — Robustheit

ECE 0,435 (unterkalibriert, dokumentiert). Repro deterministisch. Median ~511 ms/Case (EPI-487).

---

## 7. Grenzen (ehrlich)

1. ECE 0,435 — Konfidenz nicht kalibriert genug  
2. Kurze/deutsche Claims schwächer (Robustheit)  
3. Human Eval noch nicht durchgeführt  
4. FEVER: anderer Task — kein direkter SOTA-Vergleich  
5. Nicht peer-reviewed  

---

## 8. Fazit

ADJ trennt **Fehler vs. plausible Neuerung** (Lücke Z) symbolisch und messbar. Die Metaphern (Gericht + Orchester) sind **Kommunikations- und Design-Schicht**, nicht der Beweis — der Beweis ist die EPI-Suite.

**Nächste Schritte:** Zenodo Publish, EPI-HUMAN30, Journal.

---

## Literatur (Auswahl)

Popper (1934), Kahneman (2011), Thorne et al. FEVER (2018), Manakul et al. SelfCheckGPT (2023), Zheng et al. LLM-as-Judge (2023).

---

*Autor-Paper v6.1 — basierend auf `ZENODO_PUBLIKATION.md` + EPI-Suite. Zenodo-Upload: siehe `ZENODO_FORTSETZUNG.md`.*
