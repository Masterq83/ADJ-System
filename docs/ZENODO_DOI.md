# Zenodo DOI — ADJ-System v6.1



**Status:** ✅ **Publiziert** — 2026-07-05  
**Record:** https://zenodo.org/records/21205393  
**DOI:** https://doi.org/10.5281/zenodo.21205393



---



## Metadaten (Zenodo-Upload)



| Feld | Wert |

|------|------|

| **Upload type** | Publication / Preprint |

| **Title** | ADJ-System: Advocatus Diaboli Judgment — Ein epistemisches Falsifikationssystem für KI-generierte Abweichungen |

| **Authors** | Funk, Max |

| **Affiliation** | Funk!Werk Ai Solutions, Dorsten, Germany |

| **Description** | Preprint v6.1. EPI-Benchmark-Suite: 487/487 ideal_adj (100%), Holdout H120 100%, Gap-Z Z100 100%, Live-Baselines EPI-LIVE487 (LLM 77.4%, SelfCheck 37.2%), FEVER-500 Transfer. McNemar p≈0. Nicht peer-reviewed. Supplement enthält alle Benchmark-Reports. |

| **Keywords** | epistemische Falsifikation, Lücke Z, Halluzination, Knowledge Augmentation Graph, Multi-Agent, Popper, FEVER, SelfCheckGPT, LLM-as-Judge |

| **License** | CC0 1.0 Universal |

| **Version** | v6.1 |

| **Publication date** | 2026-07-05 |

| **Related identifier** | https://github.com/Masterq83/ADJ-System (isSupplementTo) |



---



## DOI



```

10.5281/zenodo.21205393

```



> Nach Upload: Platzhalter durch echte Zenodo-ID ersetzen in `ZENODO_PUBLIKATION.md` und hier.



---



## Upload-Dateien



| Datei | Pfad | Pflicht |

|-------|------|---------|

| Preprint PDF | `docs/ADJ_System_v6.1_Preprint.pdf` | **ja** |

| Preprint Markdown | `docs/ZENODO_PUBLIKATION.md` | empfohlen |

| Benchmark Supplement | `docs/zenodo_release_v6.1/` (ZIP oder Ordner) | **ja** |

| Upload-Checkliste | `docs/ZENODO_UPLOAD_README.md` | intern |



PDF + Bundle erzeugen:



```powershell

cd "E:\Cursor Projekte\ADJ-System"

python scripts/create_preprint_pdf.py

python scripts/build_zenodo_release.py

```



Optional ZIP:



```powershell

Compress-Archive -Path "docs\zenodo_release_v6.1\*" -DestinationPath "docs\zenodo_release_v6.1.zip"

```



---



## Benchmark-Ergebnisse (v6.1)



| Benchmark | ADJ | Best Baseline | Status |

|-----------|-----|---------------|--------|

| EPI-487 | 100% | LLM 60.2% | ✅ |

| EPI-H120 | 100% | LLM 67.5% | ✅ |

| EPI-Z100 | 100% | LLM 67.0% | ✅ |

| EPI-LIVE487 | 100% | LLM-live 77.4% | ✅ |

| FEVER-500 | 0% FEVER-3* | SelfCheck 7.0% | ✅ |

| EPI-HUMAN30 | pending | — | 📋 Material ready |



*Konservative Enthaltung — Task-Mismatch, 0 false commits.



---



## Upload-Schritte



1. PDF + Supplement prüfen

2. https://zenodo.org/deposit/new

3. Metadaten aus Tabelle oben

4. Dateien hochladen (PDF + zenodo_release_v6.1.zip)

5. DOI reservieren → eintragen

6. Publish

7. Optional: GitHub Release v6.1



---



## Nach EPI-HUMAN30



```powershell

python benchmarks/scripts/score_human_eval.py benchmarks/human_eval_pack/rater_sheet_*.csv

```



→ §9.6 in ZENODO_PUBLIKATION.md ergänzen → PDF v6.1.1 neu generieren (optional vor Publish).

---

## Fortsetzung / Lesson Learned

**Session gespeichert:** `docs/ZENODO_FORTSETZUNG.md`

- API-Upload 2026-07-05: 403 (vermutlich zu viele Test-Requests)
- **Nächster Versuch:** Browser-Upload bevorzugt; API max. 1 Versuch
- Token nach Screenshots rotieren

