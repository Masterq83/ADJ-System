# ADJ Paper Benchmark Suite — Spezifikation

**Version:** 1.0 | **Stand:** 2026-07-05 | **Ziel:** Ernsthafte wissenschaftliche Evidenz fuer das ADJ-Paper

---

## 1. Forschungsfrage und Domäne

ADJ ist **kein Fact-Checker** (FEVER), sondern ein **epistemisches Tribunal**:

| ADJ-Kern | Was es misst | Was andere messen |
|----------|--------------|-------------------|
| 4 Urteile (Rot/Gelb/Gruen/Orange) | Fehler vs. Idee vs. verifiziert vs. unsicher | Binär oder 3-Klassen |
| **Luecke Z** | Plausible Hypothese = potenzielle Neuerkenntnis | Nicht vorgesehen |
| Symbolische Falsifikation | Popper, KAG, Gewaltenteilung | LLM-as-Judge, Konsistenz |

**Paper-These:** ADJ trennt epistemische Kategorien praeziser als gaengige Halluzinations-Detektoren und vermeidet Overcommitment.

---

## 2. Benchmark-Uebersicht

| ID | n | Status | Paper-§ | Belegt |
|----|---|--------|---------|--------|
| **EPI-487** | 487 | ✅ done | 9.1 | 4-Klassen 100 %, McNemar vs Proxies |
| **EPI-H120** | 120 | 🔧 prepared | 9.2 | Generalisierung (Holdout) |
| **EPI-Z100** | 100 | 🔧 prepared | 9.3 | Gap-Z (PH vs LH/VC) |
| **EPI-LIVE487** | 487 | 🔧 prepared | 9.4 | Live-Baselines (NVIDIA) |
| **TRANSFER-FEVER500** | 500 | ✅ done | 9.5 | Transfer-Grenzen, Safety |
| **EPI-HUMAN30** | 30 | 📋 protocol | 9.6 | Experten-Validierung |

Spezifikation maschinenlesbar: `benchmarks/specs/epi_suite.json`

---

## 3. Metriken (paper-tauglich)

### Primaer (Kern-Domäne)

| Metrik | Definition | Paper-Nutzen |
|--------|------------|--------------|
| **multiclass_accuracy_4** | Exakter Match ideal_adj | Haupt-Accuracy |
| **macro_f1_4** | Macro-F1 ueber 4 Klassen | Ausgewogen bei Klassen-Ungleichgewicht |
| **ph_recall** | PH korrekt / PH gold | **Gap-Z Kernmetrik** |
| **gap_z_error_rate** | (PH→LH + LH→PH) / (PH+LH) | Verwechslung Fehler vs. Idee |
| **mcnemar_p** | Paarvergleich ADJ vs Baseline | Signifikanz |

### Sekundaer

| Metrik | Definition |
|--------|------------|
| binary_f1_hallucination | LH vs Rest (Abstention=Fehler) |
| abstention_rate | PH+IU / n |
| false_commit_rate | Falsche VC/LH-Commits |
| cohens_kappa | ADJ vs Gold / vs Baseline |
| bootstrap_ci_f1 | 95%-CI |

### Transfer (FEVER)

| Metrik | Definition |
|--------|------------|
| fever_3_acc | 3-Klassen nach Mapping |
| false_supports / false_refutes | Fehl-Commits |

---

## 4. Literatur-Vergleich (Quellenbezug)

| System | Quelle | Was ADJ anders/besser belegen kann |
|--------|--------|-------------------------------------|
| **SelfCheckGPT** | Manakul et al. 2023 | Weniger FP-Overcommitment; EPI-487 F1/P/R; FEVER false-commits |
| **LLM-as-Judge** | Zheng et al. 2023 | Kein Self-Reference; deterministisch; +40pp auf EPI-487 |
| **Popper/Falsifikation** | Popper 1934 | Regelbasiert vs. epistemisches Tribunal; +65pp |
| **FEVER** | Thorne et al. 2018 | Task-Mismatch dokumentiert; nicht vergleichbar ohne Adaption |
| **TruthfulQA** | Lin et al. 2022 | Kein PH/IU; optional Phase 2 |
| **HaluEval** | Li et al. 2023 | Binär; kein Gap-Z |
| **RefChecker** | KnowHalBench 2024 | Braucht Referenz; optional 100-Case-Subset |
| **Metriken-Kritik** | EMNLP 2025 Mirage | Eigene epistemische Metriken rechtfertigen |

---

## 5. Was benoetigt wird

### Software (vorhanden)

- Python 3.11+, `adj-prototype`, `benchmarks/scripts/`
- Corpora: `build_epi_corpora.py` einmal ausfuehren

### API (optional, fuer EPI-LIVE487)

- Umgebungsvariable `NVIDIA_API_KEY` (NVIDIA Integrate API)
- Geschaetzt: ~2 h Laufzeit, ~0 EUR Free Tier

### Human Eval (EPI-HUMAN30)

- 2–3 Rater mit wissenschaftlichem Hintergrund
- ~2–3 h pro Rater
- Protokoll: `benchmarks/protocols/HUMAN_EVAL_PROTOCOL.md`

### Peer Review (extern)

- Zenodo-Preprint → Journal (ACL/EMNLP Workshop, AI & Society)
- Nicht durch Benchmarks ersetzbar

---

## 6. Ausfuehrung

### Schritt 0 — Corpora bauen (einmalig)

```powershell
cd <repo-root>
python benchmarks\scripts\build_epi_corpora.py
```

Erzeugt:
- `benchmarks/corpora/epi_holdout_h120.json`
- `benchmarks/corpora/epi_gap_z_z100.json`
- `benchmarks/corpora/epi_human_sample_h30.json`
- `benchmarks/corpora/epi_manifest.json`

### Schritt 1 — Holdout (Generalisierung)

```powershell
python benchmarks\scripts\epi_benchmark_eval.py --benchmark EPI-H120 --systems adj,popper,llm_heuristic
```

### Schritt 2 — Gap-Z (Kern-USP)

```powershell
python benchmarks\scripts\epi_benchmark_eval.py --benchmark EPI-Z100 --systems adj,popper,llm_heuristic
```

### Schritt 3 — Live-Baselines (optional, ~2 h)

```powershell
powershell -File benchmarks\scripts\Run-EpiBenchmark.ps1 -Benchmark EPI-LIVE487 -Live
```

### Schritt 4 — Human Eval (manuell)

Siehe `benchmarks/protocols/HUMAN_EVAL_PROTOCOL.md`

### Bereits erledigt

- EPI-487: `python benchmarks/scripts/comparison_report.py`
- FEVER-500: `Run-FeverPhase2.ps1`

---

## 7. Paper-Abschnitte (empfohlen)

```
§9.1  EPI-487    — Primaerevidenz (4-Klassen, McNemar, Confusion)
§9.2  EPI-H120   — Holdout-Generalisierung
§9.3  EPI-Z100   — Gap-Z / Luecke Z (novel metric)
§9.4  EPI-LIVE   — Live-Baselines (fair comparison)
§9.5  FEVER-500 — Transfer & Safety (Abstention, false commits)
§9.6  EPI-HUMAN — Experten-Validierung (optional)
§9.7  Limitationen — ECE, Peer Review, FEVER≠Kern-Domäne
```

---

## 8. Erfolgskriterien (wissenschaftlich)

| Benchmark | Mindest-Erfolg fuer Paper |
|-----------|---------------------------|
| EPI-487 | ADJ ≥ 95 % (aktuell 100 %) |
| EPI-H120 | ADJ ≥ 90 %, signifikant vs Baselines |
| EPI-Z100 | PH-recall ≥ 85 %, gap_z_error ≤ 10 % |
| EPI-LIVE487 | ADJ ≥ Proxies (auch live) |
| FEVER-500 | 0 false commits dokumentiert |
| EPI-HUMAN30 | ADJ mean ≥ 1,5/2, +0,3 vs Baseline |

---

## 9. Artefakte

| Pfad | Inhalt |
|------|--------|
| `benchmarks/specs/epi_suite.json` | Maschinenlesbare Spec |
| `benchmarks/scripts/epi_benchmark_eval.py` | Unified Runner |
| `benchmarks/scripts/epi_metrics.py` | Metriken |
| `benchmarks/scripts/build_epi_corpora.py` | Corpora-Generator |
| `benchmarks/scripts/Run-EpiBenchmark.ps1` | Starter + Log |
| `docs/PAPER_EVIDENCE_MATRIX_CAVEMAN.md` | Evidenz-Entscheidungen |

---

*Fuer Peer Review: EPI-H120 + EPI-Z100 + EPI-LIVE487 + optional EPI-HUMAN30 sind der kritische Pfad.*
