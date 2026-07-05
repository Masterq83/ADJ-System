# EPI-HUMAN30 — Blind Human Evaluation (öffentliches Rater-Paket)

**Preprint:** [10.5281/zenodo.21205393](https://doi.org/10.5281/zenodo.21205393)  
**Benchmark:** EPI-HUMAN30 (n=30 Claims, 90 Zeilen = 30×3 Systeme A/B/C)

---

## Für Rater (extern)

1. **Lesen:** `ANLEITUNG_RATER_DE.md`
2. **Ausfüllen:** `rater_sheet.csv` (Spalten `appropriateness_0_2`, optional `gap_z_recognition_0_1`)
3. **Speichern als:** `rater_sheet_IHRNAME.csv`
4. **Zurücksenden:** siehe `SUBMIT_RESULTS.md`

**Nicht öffnen vor Bewertung:** `ANALYST_blind_mapping.json` (nur für Auswerter)

---

## Für Auswerter (Projektinhaber)

```powershell
cd <repo-root>
python benchmarks/scripts/score_human_eval.py benchmarks/human_eval_pack/rater_sheet_rater1.csv rater_sheet_rater2.csv
```

Ergebnis: `benchmarks/results/epi_human30_scores.json`

Paket neu erzeugen:

```powershell
python benchmarks/scripts/prepare_human_eval_pack.py
```

---

## Dateien

| Datei | Rolle |
|-------|--------|
| `rater_sheet.csv` | Blind-Bewertungsbogen (90 Zeilen) |
| `ANLEITUNG_RATER_DE.md` | Anleitung für Rater |
| `SUBMIT_RESULTS.md` | Abgabe-Workflow |
| `ANALYST_blind_mapping.json` | Mapping A/B/C → System (geheim bis Auswertung) |
| `pack_manifest.json` | Metadaten (generiert) |

Protokoll: `benchmarks/protocols/HUMAN_EVAL_PROTOCOL.md`
