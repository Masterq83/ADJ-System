# ADJ vs Baselines — v3 Corpus (487 Cases)

**Generated:** 2026-07-05T05:49:35.009652+00:00 | **Phase:** A (S4a)

## Setup

- **Ground truth:** `ideal_adj` (4-class ADJ labels)
- **Corpus:** adj_expanded_v3.py — 487 cases, 19 domains
- **KAG:** make_seed_kag_v3() — 266 nodes
- **ADJ:** V4 single pass (run_investigation + run_judgment, no LLM)
- **POPPER:** rule-based proxy (`popper_proxy.py`)
- **SelfCheckGPT / LLM-Judge:** heuristic fallback (no API key required)

## Ergebnisse — 4-Klassen-Genauigkeit (ideal_adj)

| System | Korrekt | Acc (4-class) | Ø Latenz | API/Modus |
|--------|---------|---------------|----------|-----------|
| ADJ | 487/487 | 100.0% | 511ms | local |
| POPPER | 168/487 | 34.5% | — | local |
| SelfCheckGPT | 76/487 | 15.6% | — | heuristic |
| LLM-Judge | 293/487 | 60.2% | — | heuristic |

## Binär-Metriken (Halluzination vs. Rest)

### Variante A — Abstention = Fehler

| System | Prec | Recall | F1 | Acc | n |
|--------|------|--------|----|-----|---|
| ADJ | 1.000 | 1.000 | 1.000 | 1.000 | 487 |
| POPPER | 0.662 | 0.249 | 0.362 | 0.630 | 487 |
| SelfCheckGPT | 0.430 | 0.942 | 0.590 | 0.450 | 487 |
| LLM-Judge | 0.837 | 0.976 | 0.901 | 0.910 | 487 |

### Variante B — Abstention ausgeschlossen

| System | Prec | Recall | F1 | Acc | n |
|--------|------|--------|----|-----|---|
| ADJ | 1.000 | 1.000 | 1.000 | 1.000 | 441 |
| POPPER | 0.692 | 0.141 | 0.234 | 0.699 | 392 |
| SelfCheckGPT | 0.708 | 0.895 | 0.791 | 0.827 | 52 |
| LLM-Judge | 0.889 | 0.615 | 0.727 | 0.977 | 257 |

## Confusion Matrix (ADJ, 4×4)

| ideal \ pred | LIKELY_HALLUCINATION | PLAUSIBLE_HYPOTHESIS | VERIFIED_CANDIDATE | INDETERMINATE_UNSAFE |
|---|---|---|---|---|
| **LH** | 159 | 0 | 0 | 0 |
| **PH** | 0 | 173 | 0 | 0 |
| **VC** | 0 | 0 | 109 | 0 |
| **IU** | 0 | 0 | 0 | 46 |

## Statistik — ADJ vs Baselines

| Vergleich | McNemar χ² | p≈ | ADJ besser | Baseline besser |
|-----------|------------|----|------------|-----------------|
| ADJ vs POPPER | 317.003 | 0.0000 | 319 | 0 |
| ADJ vs SelfCheckGPT | 409.002 | 0.0000 | 411 | 0 |
| ADJ vs LLM-Judge | 192.005 | 0.0000 | 194 | 0 |

## Cohen's Kappa (4-Klassen, ADJ vs Baseline)

- **ADJ vs POPPER:** κ=0.026, agreement=0.345, n=487
- **ADJ vs SelfCheckGPT:** κ=0.033, agreement=0.156, n=487
- **ADJ vs LLM-Judge:** κ=0.499, agreement=0.602, n=487

## Top-Fehler nach Domäne (ADJ)

**0** Fehler gesamt.

## Limitationen

- SelfCheckGPT/LLM-Judge: heuristic mode (kein Live-API-Lauf in Phase A)
- ADJ: V4 single pass — V5_FULL (UB→B-Oszillation) folgt Phase D
- ECE/Brier: siehe `s3_evaluation.md`
- PH-Bucket: 156/173 ideal (17 label_mismatch vs expected_adj)

## Artefakte

- `benchmarks/results/comparison_stats.json`
- `benchmarks/results/comparison_confusion.json`
- `benchmarks/results/adj_v3.json` (+ popper/selfcheckgpt/llm_judge_v3.json)
