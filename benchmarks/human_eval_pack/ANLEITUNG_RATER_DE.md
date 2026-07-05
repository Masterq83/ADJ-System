# EPI-HUMAN30 — Anleitung für Rater (Deutsch)

**Zeitaufwand:** ca. 2–3 Stunden  
**Voraussetzung:** Wissenschaftlicher Hintergrund (Informatik, Logik, Naturwissenschaften o.ä.)

---

## Aufgabe

Bewerten Sie pro Zeile in `rater_sheet.csv`, ob das gezeigte **4-Klassen-Urteil** (`verdict_shown`) für **Claim + Kontext** epistemisch angemessen ist.

Sie sehen **System A, B oder C** — **ohne** Namen (blind).

---

## Skala `appropriateness_0_2` (Pflicht)

| Wert | Bedeutung |
|------|-----------|
| **2** | Urteil ist angemessen |
| **1** | Grenzfall / teilweise passend |
| **0** | Urteil ist unangemessen |

---

## Optional: `gap_z_recognition_0_1`

Nur wenn der Claim eine **offene oder plausible These** ist (nicht offensichtlich falsch/wahr):

| Wert | Bedeutung |
|------|-----------|
| **1** | System lässt Raum für mögliche Neuerkenntnis (Gelb-ähnlich) |
| **0** | System erzwingt binär wahr/falsch |

Leer lassen, wenn nicht anwendbar.

---

## Regeln

- **Nicht** googeln / Wikipedia — nur Claim, Kontext und gezeigtes Urteil bewerten
- Pro Case **3 Zeilen** (A, B, C) — **unabhängig** voneinander
- Keine Diskussion mit anderen Ratern über konkrete Cases (blind bleiben)

---

## Die vier Urteils-Klassen (Referenz)

| Klasse | Kurz |
|--------|------|
| LIKELY_HALLUCINATION | Wahrscheinlich Fehler |
| PLAUSIBLE_HYPOTHESIS | Plausible offene These (Lücke Z) |
| VERIFIED_CANDIDATE | Gut belegt / verifiziert |
| INDETERMINATE_UNSAFE | Nicht sicher entscheidbar |

---

## Abgabe

1. CSV speichern als: `rater_sheet_IHRNAME.csv`
2. Anleitung in `SUBMIT_RESULTS.md` befolgen

Vielen Dank für Ihre Mitwirkung an der externen Validierung des ADJ-Preprints.
