# EPI-HUMAN30 — Ergebnisse zurücksenden

**Preprint:** https://doi.org/10.5281/zenodo.21205393

---

## Was Sie einsenden

- Ausgefüllte Datei: `rater_sheet_IHRNAME.csv`
- Format: UTF-8 CSV (wie Vorlage)
- **Nicht** `ANALYST_blind_mapping.json` mit an Rater weitergeben

---

## Option A — GitHub Issue (empfohlen, wenn Repo online)

1. Repository: https://github.com/Masterq83/ADJ-System
2. **Issues** → **New issue**
3. Titel: `EPI-HUMAN30 Rater: IHRNAME`
4. CSV als Anhang (oder Inhalt in Code-Block, wenn klein)
5. Kurz bestätigen: „Ich habe die Anleitung gelesen, blind bewertet“

---

## Option B — E-Mail

An: *(Autor trägt Kontakt ein — z. B. mx.funk@…)*  
Betreff: `EPI-HUMAN30 Rater — IHRNAME`  
Anhang: `rater_sheet_IHRNAME.csv`

---

## Option C — Pull Request (für technisch Versierte)

```text
benchmarks/human_eval_pack/submissions/rater_sheet_IHRNAME.csv
```

Neuer Ordner `submissions/` anlegen, nur Ihre CSV dort ablegen, PR öffnen.

---

## Datenschutz

- Keine personenbezogenen Daten in der CSV nötig (Name nur im Dateinamen)
- Auswertung aggregiert für Paper §9.6
- Mindestens **2 unabhängige Rater** für Publikation

---

## Fragen

GitHub Issue mit Label `human-eval` oder E-Mail an Autor.
