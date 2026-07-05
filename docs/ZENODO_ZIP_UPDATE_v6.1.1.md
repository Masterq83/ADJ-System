# Zenodo — Supplement-ZIP ersetzen (v6.1.1)

**Stand:** 2026-07-05  
**Record:** https://zenodo.org/records/21205393  
**DOI:** https://doi.org/10.5281/zenodo.21205393 (bleibt gleich)

---

## Warum ersetzen?

Die alte `zenodo_release_v6.1.zip` enthielt **keinen Quellcode**, aber:

| Problem | Alt | Neu (v6.1.1) |
|---------|-----|--------------|
| Reproduktions-Befehle | Verwiesen auf `adj-prototype`, Scripts | Entfernt — „implementation proprietary“ |
| `epi_manifest.json` | Alle Holdout-Case-IDs | Nur Counts + Protokoll |
| PPTX | nicht in ZIP | nicht in ZIP (PPTX bleibt lokal) |

**Vollcode war nie in der ZIP** — trotzdem soll die ZIP aktualisiert werden, damit niemand den Eindruck bekommt, das System sei reproduzierbar ohne proprietären Code.

---

## Neue Datei (lokal generiert)

```
E:\Cursor Projekte\ADJ-System\docs\zenodo_release_v6.1.zip
```

Neu bauen:

```powershell
cd "E:\Cursor Projekte\ADJ-System"
python scripts/build_zenodo_release.py
```

---

## Manuell auf Zenodo ersetzen

1. https://zenodo.org/records/21205393 → **Edit** (New version oder Edit files)
2. Alte `zenodo_release_v6.1.zip` **entfernen**
3. Neue ZIP hochladen (gleicher Dateiname oder `zenodo_release_v6.1.1.zip`)
4. Version-Hinweis: „Supplement v6.1.1 — no source code, redacted manifest“
5. **Publish** (DOI bleibt bei New Version gleich)

PDF **nicht** neu nötig, sofern Preprint-Text unverändert.

---

## Was in der ZIP bleibt (öffentlich OK)

- Benchmark-Reports (EPI-487, H120, Z100, LIVE, FEVER)
- Specs + Human-Eval-Vorlage
- Keine labelled Corpora, kein adj-prototype

---

## Was nur lokal bleibt

- `adj-prototype/`, `adj-api/`, `adj_v5_test/`
- `benchmarks/corpora/` (487 Fälle + Labels)
- `docs/ADJ_Vortrag*.pptx` (Präsentation **noch nicht fertig**)
