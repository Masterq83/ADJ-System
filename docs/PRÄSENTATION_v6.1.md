# ADJ v6.1 — Präsentation (Dual-Track: ML & Nicht-ML)

**Stand:** 2026-07-05 | **Ziel:** Vortrag / Pitch / Workshop  
**Basis:** `Metaphors.md`, `ZENODO_PUBLIKATION.md` Anhang A, EPI-Suite  
**Hinweis:** `ADJ_Vortrag.pptx` nicht im Repo — Folien aus diesem Dokument neu bauen.

---

## Recherche — Wie präsentieren? (ML vs. Nicht-ML)

| Prinzip | Quelle / Idee | Umsetzung für ADJ |
|---------|---------------|-------------------|
| **Dual-Layer** | Transformer Explainer, DNF-Framework | Hauptfolien = Story; Backup = Metriken |
| **Metapher zuerst, Limitation nennen** | Punya Mishra „Double Black Box" | Nach Gericht/Orchester: „Bild, kein Beweis" |
| **Begriff vor Nutzung** | Gwern „Grow-Speech" | LH/PH/VC auf Folie 3 definieren |
| **Try → Score → Change** | RL-for-Children | Problem → Benchmark → Ergebnis |
| **Kein Hype** | Georgia Tech AI Literacy | „Mehr Mathe als Magie" — symbolisch, reproduzierbar |

**Struktur:** 20 Min Hauptteil (Nicht-ML-tauglich) + 10 Min Backup (ML) + 5 Min Q&A.

---

## Erzählbogen: Metapher → Erkenntnis

```
1. PROBLEM     „Die KI lügt nicht absichtlich — sie rät."
2. METAPHER 1  Gericht: Ankläger ≠ Richter (Gewaltenteilung)
3. METAPHER 2  Ampel: Rot / Gelb / Grün / Orange (Lücke Z = Gelb)
4. METAPHER 3  Orchester: Wann schnell, wann tief? (Routing)
5. SYSTEM      6 Modi = Falsifikationstrichter (1 Folie, optional Detail)
6. BEWEIS      EPI-Suite in 4 Zahlen (487, H120, Z100, LIVE)
7. EHRLICH     Grenzen: ECE, FEVER-Mismatch, Human Eval pending
8. AUSBLICK    Zenodo, Human Eval, Journal
```

---

## Folienplan (20 + Backup)

### Block A — Für alle (Nicht-ML)

| # | Titel | Inhalt | Sprecher-Notiz |
|---|-------|--------|----------------|
| 1 | Titel | ADJ — Wer prüft die KI? | Kein Jargon |
| 2 | Alltag | Blueprint vs. KI-Abweichung | Beispiel: Code, Medizin, Plan |
| 3 | Vier Farben | LH rot, PH **gelb**, VC grün, IU orange | **Lücke Z = Gelb** |
| 4 | Warum nicht LLM? | „Richter kann nicht Ankläger sein" | Selbstreferenz-Falle |
| 5 | Tribunal v4 | AD, J, A — 3 Rollen | Gerichtszeichnung |
| 6 | Falsifikationstrichter | 6 STOP-Schilder (Icons) | Popper in einem Satz |
| 7 | Orchester v5 | Geigen / Celli / Dirigent | Kahneman: System 1/2 |
| 8 | Weg zur Erkenntnis | Metapher → Bau → Test | Diese Folie = roter Faden |
| 9 | Ergebnis in einem Satz | 487/487, Live-Baselines geschlagen | **Keine** McNemar hier |
| 10 | Was wir NICHT behaupten | FEVER ≠ SOTA, nicht peer-reviewed | Vertrauen durch Ehrlichkeit |
| 11 | Demo / Graph | Graphify / 1 Case PH vs LH | Optional live |
| 12 | Call to Action | Zenodo, GitHub, Human Eval | |

### Block B — Backup (ML / Reviewer)

| # | Titel | Inhalt |
|---|-------|--------|
| B1 | Task formal | 4-Klassen, `ideal_adj`, KAG, kein LLM im Kern |
| B2 | EPI-Suite Tabelle | 487, H120, Z100, LIVE487, FEVER, HUMAN30 |
| B3 | Confusion / McNemar | p≈0, 0 PH↔LH auf Z100 |
| B4 | Live-Baselines | Llama 3.1 8B, dual-key, Rate limits |
| B5 | S3 / ECE | 0,435, Robustheit, Repro |
| B6 | Ablation / Router | UB_ONLY → V4_FULL |
| B7 | Related Work | FEVER, SelfCheck, LLM-Judge — Task-Mismatch |

---

## Zwei Sprechweisen (gleiche Folie, anderer Text)

### Folie 9 — Ergebnis

**Nicht-ML:**  
> „Auf 487 kuratierten Fällen lag unser Prüfsystem immer richtig. Gegen zwei bekannte KI-Prüfmethoden, die live per API liefen, lagen wir deutlich vorn — ohne selbst eine große Sprach-KI zu sein."

**ML:**  
> „100 % 4-class accuracy on ideal_adj (n=487). McNemar vs LLM-live (77.4 %) and SelfCheck-live (37.2 %): p≈0. Symbolic pipeline, median ~511 ms, deterministic repro."

### Folie 6 — Falsifikation

**Nicht-ML:**  
> „Statt zu fragen ‚Ist das wahr?', fragen wir: ‚Was müsste falsch sein, damit es stimmt?' — wie im Gericht."

**ML:**  
> „Six-mode falsification funnel M1–M6; early exit on axiom conflict; PH preserved as non-commitment class."

---

## Metaphern — Was NICHT sagen

| Vermeiden | Besser |
|-----------|--------|
| „Die KI denkt wie ein Mensch" | „Regeln + Graph + Routing" |
| „100 % = bewiesen für alle Ewigkeit" | „100 % auf kuratiertem Gold; Human Eval folgt" |
| „Schlägt FEVER SOTA" | „Transfer zeigt Enthaltung, Task-Mismatch" |
| „AGI / Bewusstsein" (v5) | „Pre-conscious architecture" (Metaphors.md) |

---

## Visuelle Empfehlungen

1. **Folie 3:** Ampel mit **Gelb = Lücke Z** groß  
2. **Folie 5–7:** Split-Screen Tribunal | Orchester  
3. **Folie 8:** Timeline: Idee 2024 → v4 → v5 → EPI 2026  
4. **Folie 9:** Ein Balkendiagramm (ADJ 100 % vs LLM 77 % vs SelfCheck 37 %)  
5. **Backup B2:** Volle Tabelle aus `zenodo_release_v6.1/00_BENCHMARK_RESULTS_SUMMARY.md`

---

## PPTX neu erstellen

1. PowerPoint / Google Slides — Template: dunkel, Ampel-Akzentfarben  
2. Folien 1–12 aus Block A  
3. Sektion „Appendix" mit B1–B7  
4. Speaker Notes aus Sprechweisen oben  
5. Speichern als: `docs/ADJ_Vortrag_v6.1.pptx`

---

## Dateien

| Zweck | Pfad |
|-------|------|
| Metaphern-Referenz | `docs/Metaphors.md` |
| Paper DE (Autor) | `docs/PAPER_DE_v6.1.md` |
| Zahlen | `docs/zenodo_release_v6.1/00_BENCHMARK_RESULTS_SUMMARY.md` |
| Zenodo später | `docs/ZENODO_FORTSETZUNG.md` |

---

*Präsentations-Leitfaden v6.1 — Metapher führt, Zahlen belegen, Grenzen schließen ab.*
