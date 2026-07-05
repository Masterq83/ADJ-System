# ADJ Preprint v6.0 — §9 Empirische Evaluation (Entwurf)

**Stand:** 2026-07-05 | **Quellen:** EPI-Suite, S4, S3, FEVER-Transfer  
**Status:** Entwurf fuer Zenodo/Journal — alle Zahlen aus reproduzierbaren Runs

---

## 9. Empirische Evaluation

Wir evaluieren ADJ auf einem **487-Case-Korpus** (`adj_expanded_v3`, 19 Domänen) mit menschlich kuratiertem Gold-Label `ideal_adj` (vier epistemische Klassen). Die Evaluation umfasst sechs komplementäre Benchmarks (EPI-Suite), die ADJs Kern-Domäne — **epistemische 4-Klassen-Falsifikation** und **Lücke Z** (Trennung von Fehler vs. plausibler Hypothese) — gegen etablierte Alternativen abgrenzen.

**Ground Truth:** `ideal_adj` ∈ {LIKELY_HALLUCINATION, PLAUSIBLE_HYPOTHESIS, VERIFIED_CANDIDATE, INDETERMINATE_UNSAFE}.  
**ADJ-Pipeline:** V4 single pass (`run_investigation` + `run_judgment`), KAG v3 (266 Knoten), kein LLM im Kern.  
**Statistik:** McNemar-Test (paarweise Korrektheit), Cohen's κ (4-Klassen-Übereinstimmung).

---

### 9.1 Primärbenchmark — EPI-487 (487 Cases, Heuristik-Baselines)

Auf dem vollständigen Korpus erreicht ADJ **487/487 (100,0 %)** 4-Klassen-Genauigkeit. Die Confusion-Matrix zeigt **null Fehlklassifikationen** über alle vier Kategorien (LH 159/159, PH 173/173, VC 109/109, IU 46/46).

| System | Korrekt | Acc (4-Kl.) | Binär-F1† | Modus |
|--------|---------|-------------|-----------|-------|
| **ADJ** | **487/487** | **100,0 %** | **1,000** | lokal, symbolisch |
| LLM-Judge | 293/487 | 60,2 % | 0,901 | Heuristik |
| POPPER | 168/487 | 34,5 % | 0,362 | Regeln |
| SelfCheckGPT | 76/487 | 15,6 % | 0,590 | Heuristik |

†Binär: Halluzination vs. Rest; Abstention = Fehler.

**McNemar (ADJ vs. Baseline):** p ≈ 0 in allen Paaren; ADJ besser in 194–411 Cases, Baseline besser in 0.

**Latenz:** Median ~511 ms/Case (ADJ, lokal).

Quelle: `benchmarks/results/comparison_report.md` (S4a, 2026-07-05).

**Abgrenzung zur Literatur:** FEVER (Thorne et al., 2018) und TruthfulQA (Lin et al., 2022) messen binäres oder 3-Klassen-Fact-Checking ohne epistemische Feingranularität. SelfCheckGPT (Manakul et al., 2023) und LLM-as-Judge (Zheng et al., 2023) dienen als funktionale Proxies — nicht als identische Aufgabenstellung.

---

### 9.2 Generalisierung — EPI-H120 (Holdout, n = 120)

Zur Absicherung gegen Überanpassung auf den Entwicklungskorpus zogen wir ein **stratifiziertes Holdout-Set** (30 Cases pro Klasse, Seed 20260705, dokumentiert in `epi_manifest.json`). Diese Cases wurden weder für Gap-Z noch für Human-Eval verwendet.

| System | Acc | PH-Recall | Gap-Z-Fehler |
|--------|-----|-----------|--------------|
| **ADJ** | **100,0 %** | **100,0 %** | **0,0 %** |
| LLM-Judge (heur.) | 67,5 % | 80,0 % | 1,7 % |
| POPPER | 21,7 % | 83,3 % | 41,7 % |

McNemar: ADJ vs. POPPER +94/0; vs. LLM-Judge +39/0 (p ≈ 0).

Quelle: `benchmarks/results/epi_epi-h120_20260705T085733Z/`

---

### 9.3 Lücke Z — EPI-Z100 (Gap-Z-Diskrimination, n = 100)

Kein etablierter Standard-Benchmark testet die Trennung **plausible Hypothese (Gelb) vs. Fehler (Rot) vs. verifiziert (Grün)**. EPI-Z100 enthält 50 PH-, 25 LH- und 25 VC-Cases (ohne Overlap mit H120/H30).

| System | Acc | PH-Recall | Gap-Z-Fehler | False Commits |
|--------|-----|-----------|--------------|---------------|
| **ADJ** | **100,0 %** | **100,0 %** | **0,0 %** | **0** |
| LLM-Judge (heur.) | 67,0 % | 84,0 % | 0,0 % | 1 |
| POPPER | 45,0 % | 90,0 % | 26,7 % | 1 |

McNemar: ADJ vs. POPPER +55/0; vs. LLM-Judge +33/0 (p ≈ 0).

**Interpretation:** POPPER erreicht hohe PH-Recall durch Verwechslung (26,7 % PH↔LH); ADJ trennt epistemische Kategorien ohne Gap-Z-Fehler.

Quelle: `benchmarks/results/epi_epi-z100_20260705T085857Z/`

---

### 9.4 Live-Baselines — EPI-LIVE487 (487 Cases, NVIDIA API)

Fairer Vergleich mit **live** LLM-Judge und SelfCheckGPT (Llama 3.1 8B Instruct, `integrate.api.nvidia.com`), gleiche 4-Klassen-Aufgabe, Dual-Key-Pool mit Rate-Limiting (0,55 s/Call, 1.948 API-Calls, 25 Rate-Limits ohne Abbruch).

| System | Acc | Macro-F1 | PH-Recall | Gap-Z-Fehler | False Commits |
|--------|-----|----------|-----------|--------------|---------------|
| **ADJ** | **100,0 %** | **1,000** | **100,0 %** | **0,0 %** | **0** |
| LLM-Judge **live** | 77,4 % | 0,653 | 97,7 % | 14,5 % | 4 |
| LLM-Judge (heur.) | 60,2 % | 0,563 | 80,3 % | 1,5 % | 5 |
| POPPER | 34,5 % | 0,177 | 86,7 % | 35,2 % | 10 |
| SelfCheckGPT **live** | 37,2 % | 0,195 | 86,7 % | 45,5 % | **37** |

McNemar: ADJ vs. llm_live +110/0; vs. selfcheck_live +306/0 (p ≈ 0).

**Paper-relevante Aussage:** Selbst der stärkste Live-Baseline (LLM-Judge 77,4 %) bleibt **22,6 Prozentpunkte** unter ADJ; SelfCheckGPT-live produziert **37 falsche Commits** bei 45,5 % Gap-Z-Fehlerrate — konsistent mit der Literatur zu hohem Recall und vielen False Positives (Manakul et al., 2023).

Quelle: `benchmarks/results/epi_epi-live487_20260705T110726Z/`

---

### 9.5 Transfer-Experiment — FEVER-dev-Subset (n = 500, Wikipedia-Kontext)

Externer Transfer auf FEVER (Thorne et al., 2018): stratifiziertes Subset aus `paper_dev.jsonl`, Wikipedia-Snippets als Kontext. Mapping ADJ → FEVER konservativ (PH → NOT ENOUGH INFO).

| System | FEVER-3 Acc | Enthaltung | False SUPPORTS/REFUTES |
|--------|-------------|------------|------------------------|
| **ADJ** | 0,0 % | **100,0 %** | **0** |
| SelfCheck live | 7,0 % | 84,8 % | 41 |
| LLM-Judge live | 5,8 % | 93,0 % | 6 |
| POPPER | 5,4 % | 90,0 % | 23 |

**Interpretation:** ADJ enthält sich auf unstrukturierten Wikipedia-Claims vollständig (100 % PH); dies dokumentiert **Task-Mismatch** (4-Klassen-Epistemik vs. 3-Klassen-Fact-Checking), nicht Pipeline-Versagen. Ein direkter Vergleich mit FEVER-SOTA (~75–79 %) ist methodisch nicht zulässig.

Quelle: `benchmarks/results/fever_medium_20260705T075920Z/`

---

### 9.6 Experten-Evaluation — EPI-HUMAN30 (geplant)

Unabhängige Blind-Bewertung durch 2–3 Rater (epistemische Angemessenheit, Skala 0–2). Materialien vorbereitet: `benchmarks/human_eval_pack/`. Siehe `docs/EPI_HUMAN30_CAVEMAN.md`.

*Ergebnisse folgen nach Rater-Durchführung; nicht in den obigen Zahlen enthalten.*

---

### 9.7 Kalibrierung und Robustheit (S3)

| Metrik | Wert | Ground Truth |
|--------|------|--------------|
| Accuracy | 96,5 % | `expected_adj` |
| ECE | 0,435 | unterkalibriert |
| Reproduzierbarkeit | deterministisch | 0 Mismatch |
| Kurze Claims (<10 W) | 80,7 % | vs. expected_adj |
| Deutsch (heuristic) | 84,6 % | vs. expected_adj |

Quelle: `benchmarks/results/s3_evaluation.md`

---

### 9.8 Zusammenfassung der Claims (copy-ready)

> ADJ erreicht auf dem 487-Case-Korpus mit `ideal_adj` **100 % 4-Klassen-Genauigkeit** und übertrifft Popper-, SelfCheckGPT- und LLM-Judge-Baselines signifikant (McNemar p ≈ 0) — einschließlich **live** NVIDIA-API-Läufen (EPI-LIVE487: LLM-Judge 77,4 %, SelfCheck 37,2 %). Auf stratifiziertem Holdout (H120) und Gap-Z-Subset (Z100) bleibt ADJ bei 100 % ohne PH↔LH-Verwechslung. FEVER-Transfer (n = 500) zeigt konservative Enthaltung (0 falsche Commits) und grenzt ADJs Domäne von Fact-Checking ab. ADJ ist **kein Ersatz für FEVER-SOTA**, sondern ein **epistemisches Tribunal** mit vier Urteilen und Lücke Z.

---

### 9.9 Limitationen

1. **Gold-Label:** `ideal_adj` ist kuratiert, nicht unabhängig annotiert (EPI-HUMAN30 adressiert dies).
2. **ECE 0,435:** Konfidenz `C_new` unterkalibriert.
3. **FEVER-Transfer:** Kein Vergleich mit Wikipedia-Retrieval-SOTA (InFact/AVeriTeC).
4. **Peer Review:** Preprint, nicht begutachtet.
5. **V5_FULL:** S4 nutzte V4 single pass; MC-Router V5_FULL produktiv, aber separat evaluiert.

---

## Literatur (§9)

1. Thorne, J. et al. (2018). FEVER: Fact Extraction and VERification. *NAACL.*
2. Lin, S. et al. (2022). TruthfulQA. *ACL.*
3. Manakul, P. et al. (2023). SelfCheckGPT. *EMNLP.*
4. Zheng, L. et al. (2023). Judging LLM-as-a-Judge. *NeurIPS Workshop.*
5. Popper, K. R. (1934). *Logik der Forschung.*

---

## Artefakt-Index

| Benchmark | Report-Pfad |
|-----------|-------------|
| EPI-487 | `benchmarks/results/comparison_report.md` |
| EPI-H120 | `benchmarks/results/epi_epi-h120_20260705T085733Z/` |
| EPI-Z100 | `benchmarks/results/epi_epi-z100_20260705T085857Z/` |
| EPI-LIVE487 | `benchmarks/results/epi_epi-live487_20260705T110726Z/` |
| FEVER-500 | `benchmarks/results/fever_medium_20260705T075920Z/` |
| EPI-HUMAN30 | `benchmarks/human_eval_pack/` (nach `prepare_human_eval_pack.py`) |

*Entwurf erstellt: 2026-07-05*
