# GitHub Upload — ADJ-System v6.1

**Stand:** 2026-07-05  
**Remote-Status:** https://github.com/Masterq83/ADJ-System → **✅ online**  
**Release:** https://github.com/Masterq83/ADJ-System/releases/tag/v6.1  
**Zenodo:** https://doi.org/10.5281/zenodo.21205393 ✅

---

## Voraussetzungen

- Git installiert
- GitHub-Konto `Masterq83`
- `.gitignore` prüft Secrets (`.env`, `secrets/`, `PROJECT_MEMORY.md`, …)

---

## Schritt 1 — Repository auf GitHub anlegen

1. https://github.com/new
2. **Repository name:** `ADJ-System`
3. **Public**
4. **Kein** README/License initialisieren (wir haben lokal schon Dateien)
5. **Create repository**

---

## Schritt 2 — Lokal initialisieren (einmalig)

```powershell
cd "E:\Cursor Projekte\ADJ-System"

git init
git branch -M main
git remote add origin https://github.com/Masterq83/ADJ-System.git

git add .
git status
# Prüfen: KEINE .env, secrets/, buvmkey, tmp_test_*.py, PROJECT_MEMORY.md

git commit -m "Release v6.1: ADJ preprint, EPI suite, human eval pack, Zenodo DOI"
git push -u origin main
```

---

## Schritt 3 — GitHub Release v6.1

1. GitHub → **Releases** → **Draft new release**
2. Tag: `v6.1`
3. Title: `ADJ-System Preprint v6.1`
4. Body:

```markdown
## ADJ-System v6.1

- Zenodo: https://doi.org/10.5281/zenodo.21205393
- EPI-Suite: 487/487, Holdout, Gap-Z, Live-Baselines
- Human Eval: benchmarks/human_eval_pack/

## Assets
- ADJ_System_v6.1_Preprint.pdf
- zenodo_release_v6.1.zip
```

5. Assets anhängen:
   - `docs\ADJ_System_v6.1_Preprint.pdf`
   - `docs\zenodo_release_v6.1.zip`

---

## Schritt 4 — README DOI-Badge

Bereits in `README.md`:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21205393.svg)](https://doi.org/10.5281/zenodo.21205393)
```

---

## EPI-HUMAN30 auf GitHub

Enthalten in Push (Rater-sicher):

```
benchmarks/human_eval_pack/
  README.md
  ANLEITUNG_RATER_DE.md
  SUBMIT_RESULTS.md
  rater_sheet.csv
  RATER_ANLEITUNG.md
  submissions/          ← Abgabe per PR
```

**Nicht auf GitHub** (gitignored — Blind-Mapping bleibt beim Auswerter lokal):

- `ANALYST_blind_mapping.json`
- `pack_manifest.json` (enthält lokale Pfade)

Rater: Issue öffnen oder CSV in `submissions/` per PR.

---

## Sicherheits-Check vor `git add`

```powershell
cd "E:\Cursor Projekte\ADJ-System"
git check-ignore -v secrets/zenodo_token.txt .env PROJECT_MEMORY.md
# Sollte .gitignore-Treffer zeigen

rg "nvapi-[A-Za-z0-9_-]{20,}" --glob "!secrets/*" --glob "!.git/*"
# Sollte 0 Treffer in tracked files sein
```

---

## Nach Push

- [ ] Release v6.1 mit PDF + ZIP
- [ ] Zenodo Related work „Is supplemented by“ zeigt auf GitHub (bereits gesetzt)
- [ ] Optional: GitHub Issue Template „Human Eval“

---

*Upload-Anleitung v6.1*
