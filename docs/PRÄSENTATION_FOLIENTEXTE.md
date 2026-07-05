# ADJ v6.1 — Folientexte (Copy-Paste für PowerPoint)

**DOI:** https://doi.org/10.5281/zenodo.21205393  
**Speichern als:** `E:\Cursor Projekte\ADJ-System\docs\ADJ_Vortrag_v6.1.pptx`

---

## Folie 1 — Titel

**ADJ-System: Advocatus Diaboli Judgment**

Epistemische Prüfung von KI-Abweichungen — Lücke Z

Max Funk · Funk!Werk Ai Solutions  
Preprint v6.1 · https://doi.org/10.5281/zenodo.21205393

---

## Folie 2 — Problem

**Die KI weicht ab — ist das ein Fehler oder eine Entdeckung?**

- Blueprint vs. KI-Output → **Lücke Z**
- Halluzination (Fehler) vs. plausible neue These
- LLM kann **sich nicht selbst** zuverlässig prüfen

---

## Folie 3 — Vier Farben (Ampel)

| Farbe | Klasse | Bedeutung |
|-------|--------|-----------|
| Rot | LIKELY_HALLUCINATION | Wahrscheinlich Fehler |
| **Gelb** | **PLAUSIBLE_HYPOTHESIS** | **Lücke Z — Raum für Neues** |
| Grün | VERIFIED_CANDIDATE | Gut belegt |
| Orange | INDETERMINATE_UNSAFE | Nicht sicher entscheidbar |

---

## Folie 4 — Metapher 1: Tribunal

**Gericht statt Selbsturteil**

- **Ankläger** (Advocatus Diaboli) — sucht Widerlegung
- **Richter** (Judgment Agent) — formelles Urteil
- **Archivar** — Wissensgraph (KAG)

→ Gewaltenteilung nach Popper: **Falsifikation vor Verifikation**

---

## Folie 5 — Falsifikationstrichter

**6 Modi — von grob nach tief**

M1 Axiom → M2 Isomorphie → M3 Minimalannahme → M4 Tempo → M5 Triangulation → M6 Geodätisch

Jeder Modus kann **STOP** — nicht alles muss bis zum Ende.

---

## Folie 6 — Metapher 2: Orchester

**Wann schnell, wann tief?**

- **Geigen (UB)** — schnell, heuristisch (Kahneman System 1)
- **Celli (B)** — tief, regelbasiert (System 2)
- **Dirigent (MC)** — Routing, Tempo T1–T4

---

## Folie 7 — Weg zur Erkenntnis

```
Metapher verstehen → System bauen → Benchmark messen → Grenzen benennen
```

Metapher = **Kommunikation**  
Benchmark = **Beweis**

---

## Folie 8 — Ergebnisse (EPI-Suite)

| Benchmark | ADJ | Beste Baseline |
|-----------|-----|----------------|
| EPI-487 | **100 %** | LLM 60 % |
| Holdout H120 | **100 %** | LLM 68 % |
| Gap-Z Z100 | **100 %** | LLM 67 % |
| Live vs. API | **100 %** | LLM-live **77 %** |

McNemar p ≈ 0 · Symbolisch · Kein LLM im ADJ-Kern

---

## Folie 9 — Was wir NICHT behaupten

- ❌ „100 % = für alle Ewigkeit bewiesen"
- ❌ FEVER-SOTA geschlagen (Task-Mismatch)
- ❌ Peer-reviewed (Zenodo-Preprint)
- ⏳ Human Eval (EPI-HUMAN30) — Rater gesucht

---

## Folie 10 — Call to Action

- **Preprint:** doi.org/10.5281/zenodo.21205393
- **Code:** github.com/Masterq83/ADJ-System
- **Human Eval mitmachen:** `benchmarks/human_eval_pack/`

---

## Backup B1 — Task formal (ML)

4-Klassen `ideal_adj` · KAG 266 Nodes · V4 single pass · McNemar · ECE 0,435

## Backup B2 — FEVER Transfer

100 % Enthaltung · 0 false commits · kein SOTA-Vergleich

---

*Folientexte v6.1 — siehe PRÄSENTATION_v6.1.md für Sprechnotizen.*
