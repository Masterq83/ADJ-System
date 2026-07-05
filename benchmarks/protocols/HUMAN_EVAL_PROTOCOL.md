# Human Evaluation Protocol — EPI-HUMAN30

**Benchmark:** EPI-HUMAN30 | **Cases:** 30 | **Purpose:** External validity for paper §9.6

---

## 1. Ziel

Unabhaengige Experten bewerten ADJ-Urteile vs. Baselines auf **epistemischer Angemessenheit** —
nicht nur Label-Match, sondern: *Ist die 4-Klassen-Einstufung fachlich vertretbar?*

---

## 2. Materialien

| Datei | Inhalt |
|-------|--------|
| `benchmarks/corpora/epi_human_sample_h30.json` | 30 Cases (stratifiziert) |
| `benchmarks/protocols/human_eval_sheet_template.csv` | Leeres Bewertungsblatt |
| ADJ/Baseline-Outputs | Aus `epi_benchmark_eval.py --benchmark EPI-HUMAN30` |

---

## 3. Rater-Anforderungen

- **Minimum:** 2 Rater (besser 3)
- **Profil:** Wissenschaftliche Denkerfahrung (PhD oder aequi.) in mind. einer Domäne aus dem Korpus
- **Blind:** Rater sehen Claim + ctx + System-Urteil, **nicht** ideal_adj und **nicht** Systemname bis nach Bewertung

---

## 4. Bewertungsskala (pro Case, pro System)

| Code | Bedeutung |
|------|-----------|
| **2** | Urteil epistemisch angemessen |
| **1** | Teilweise angemessen / Grenzfall |
| **0** | Unangemessen (falsche epistemische Kategorie) |

Zusaetzlich fuer Gap-Z-Cases (PH-Gold):
- **Z1:** System erkennt Neuerkenntnis-Potenzial (PH oder aequivalent)
- **Z0:** System erzwingt binaer wahr/falsch ohne epistemische Nuance

---

## 5. Ablauf

1. `build_epi_corpora.py` ausfuehren (H30 generieren)
2. `epi_benchmark_eval.py --benchmark EPI-HUMAN30 --systems adj,popper,llm_heuristic`
3. Outputs anonymisieren (System A/B/C)
4. Rater fuellen `human_eval_sheet_template.csv` aus
5. Inter-Rater-Agreement (Cohen's κ) berechnen
6. ADJ vs. Baseline: Wilcoxon signed-rank oder paired t-test auf Mittelwerte

---

## 6. Paper-Metriken

| Metrik | Formel |
|--------|--------|
| Mean appropriateness | Mittel der 0–2 Skala pro System |
| ADJ advantage | mean(ADJ) − mean(best baseline) |
| Inter-rater κ | Cohen's κ zwischen Ratern |
| Gap-Z recognition | Anteil PH-Gold mit Z1 |

---

## 7. Mindest-Erfolg fuer Paper

- ADJ Mean appropriateness **≥ 1,5** (von 2)
- ADJ **≥ 0,3 Punkte** besser als beste Baseline im Mittel
- Inter-rater κ **≥ 0,4** (moderate Uebereinstimmung)

---

## 8. CSV-Template

Siehe `human_eval_sheet_template.csv`:

```
case_id,rater_id,system_blind,appropriateness_0_2,gap_z_recognition_0_1,notes
```

---

*Status: Protokoll vorbereitet — manuelle Durchfuehrung erforderlich.*
