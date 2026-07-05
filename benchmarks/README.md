# ADJ Benchmark Suite

**Zenodo v6.1:** https://doi.org/10.5281/zenodo.21205393

## Paper Benchmarks (EPI Suite v1.0)

Siehe **`docs/BENCHMARK_SUITE_PAPER.md`** fuer vollstaendige Spezifikation.

| Benchmark | n | Befehl |
|-----------|---|--------|
| EPI-487 | 487 | `python benchmarks/scripts/comparison_report.py` |
| EPI-H120 Holdout | 120 | `python benchmarks/scripts/epi_benchmark_eval.py --benchmark EPI-H120` |
| EPI-Z100 Gap-Z | 100 | `python benchmarks/scripts/epi_benchmark_eval.py --benchmark EPI-Z100` |
| EPI-LIVE487 | 487 | `Run-EpiBenchmark.ps1 -Benchmark EPI-LIVE487 -Live` |
| FEVER Transfer | 500 | `Run-FeverPhase2.ps1` |
| **EPI-HUMAN30** | 30 | `benchmarks/human_eval_pack/` — Rater-Paket |

### EPI-HUMAN30 (Human Eval)

Rater können blind bewerten und Ergebnisse einsenden:

```
benchmarks/human_eval_pack/
  README.md
  ANLEITUNG_RATER_DE.md
  SUBMIT_RESULTS.md
  rater_sheet.csv
  submissions/          ← Abgabe per PR
```

Auswertung (Autor): `python benchmarks/scripts/score_human_eval.py`

```powershell
# Corpora einmal bauen
python benchmarks/scripts/build_epi_corpora.py

# Holdout + Gap-Z
python benchmarks/scripts/epi_benchmark_eval.py --benchmark EPI-H120
python benchmarks/scripts/epi_benchmark_eval.py --benchmark EPI-Z100
```

Spec: `benchmarks/specs/epi_suite.json`

## Legacy-Struktur

```
benchmarks/
├── README.md              # Diese Datei
├── corpora/               # Testfälle als JSON
│   ├── adj_real_z_v1.json
│   ├── adj_test_cases_v1.json
│   └── adj_expanded_v2.json
├── results/               # Gespeicherte Benchmark-Ergebnisse
│   ├── adj_v5.9f.json
│   ├── selfcheckgpt_proxy.json
│   └── llm_as_judge.json
├── scripts/               # Benchmark-Runner + Vergleich
│   ├── run_benchmark.py
│   └── compare_baselines.py
└── metrics/               # Metrik-Berechnung
    └── precision_recall_f1.py
```

## Nutzung

```powershell
# Benchmark laufen
python benchmarks/scripts/run_benchmark.py

# Baseline-Vergleich
python benchmarks/scripts/compare_baselines.py
```

## Testfälle

- **v1**: D1-D5 Real-Z + A1-C3 Test Cases (15 Fälle)
- **v2**: Erweiterung auf 52 Fälle (10 Domänen)

## Metriken

- Precision/Recall/F1 für Halluzinations-Erkennung
- Vergleich ADJ vs. SelfCheckGPT vs. POPPER vs. LLM-as-Judge
