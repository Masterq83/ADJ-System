# ADJ-System — Paper (Deutsch, Normal)

> **Aktuelle Version:** `docs/PAPER_DE_v6.1.md` (Zenodo v6.1, DOI [10.5281/zenodo.21205393](https://doi.org/10.5281/zenodo.21205393))  
> Diese Datei ist die **v6.0-Fassung** — nur noch als Archiv.

**Advocatus Diaboli Judgment: Ein epistemisches Falsifikationssystem für KI-Abweichungen**

Version v6.0 | Juli 2026 | Max Funk, Funk!Werk Ai Solutions  
Repository: https://github.com/Masterq83/ADJ-System  
*Nicht peer-reviewed — Zenodo-Preprint*

---

## Kurzfassung

Wenn eine KI etwas behauptet, das vom Plan abweicht, stellt sich die Frage: Ist das ein **Fehler** (Halluzination) oder eine **mögliche neue Erkenntnis**? ADJ (Advocatus Diaboli Judgment) ist ein Prüfsystem, das diese Entscheidung nicht dem Modell selbst überlässt, sondern über ein mehrstufiges, gewaltenteiliges Verfahren nach Popper.

Das System besteht aus zwei Teilen:

- **ADJ v4 (Tribunal):** Drei unabhängige Rollen — Ermittler (Advocatus Diaboli), Richter (Judgment Agent), Archivar — prüfen Aussagen über sechs epistemische Modi und speichern Wissen in einem Graphen (KAG).
- **ADJ v5 (Orchester):** Schneller und langsamer Denkweg (UB/B) nach Kahneman, gesteuert von einem Meta-Controller. Der MC-Router wählt je nach Komplexität den passenden Prüfpfad.

**Ergebnis (Juli 2026):** Auf 487 Testfällen trifft ADJ **487 Mal** das menschlich definierte Soll-Urteil (**100 %**). Alle vier Urteils-Kategorien (LH, VC, IU, PH) sind vollständig grün. Im Vergleich mit drei Baselines liegt ADJ deutlich vorn.

---

## 1. Das Problem: Lücke Z

Eine KI erzeugt eine Abweichung vom Blueprint — „Lücke Z". Das kann bedeuten:

| Fall | Bedeutung |
|------|-----------|
| Halluzination | Logischer Fehler, Widerspruch zu bekanntem Wissen |
| Unentdeckte Wahrheit | Potenziell valide, aber noch nicht abschließend prüfbar |

Ein LLM kann **sich selbst nicht zuverlässig prüfen** — Ermittler und Richter müssen getrennt sein. ADJ setzt genau das um: Falsifikation statt blinder Verifikation.

### Vier typische Fallen

1. **Ground-Truth-Illusion** — Es gibt keine externe, unfehlbare Wahrheitsmaschine.
2. **Ontologische Trägheit** — Ein perfekter Wissensspeicher verwirft Neues.
3. **50/50-Falle** — Ohne testbare Vorhersage bleibt alles unentscheidbar.
4. **Newtonsche Statik** — Wissen ist nicht statisch; es expandiert und verändert sich.

---

## 2. Architektur im Überblick

```
Eingabe (Behauptung Z)
    │
    ▼
MC-Router ──► UB_ONLY (ms) ──► AXIOM_CHECK (~100 ms)
    │              │
    │              ▼
    │         V5_FULL (~0,5 s) ──► MetaController UB→B
    │              │
    │              ▼
    └────────► V4_FULL (~s) ──► Tribunal M0–M6 + Iteration
                    │
                    ▼
              Urteil + Konfidenz C_new
                    │
                    ▼
              Ausgabe (Prüf-API / adj_service)
```

| Komponente | Aufgabe | Stand |
|------------|---------|-------|
| ADJ v4 | Formale epistemische Prüfung | 487/487 (100 %) |
| MC-Router v5.24b | Routing nach Komplexität | V5_FULL ✅ |
| KAG | 266 Knoten, 19 Domänen | S2b ✅ |
| adj_service / Prüf-API | Ein- und Ausgabe, eigenständiger Betrieb | Implementiert |

---

## 3. ADJ v4 — Das Tribunal

### Drei Instanzen (Gewaltenteilung)

| Instanz | Rolle |
|---------|-------|
| **Advocatus Diaboli (AD)** | Sammelt Beweise, führt 6 Prüfmodi aus |
| **Judgment Agent (J)** | Formales Urteil + Bayesianische Konfidenz |
| **Archivar (A)** | KAG-Verwaltung, Signaturprüfung, Transaktionen |

### Sechs Prüfmodi (Falsifikationstrichter)

Von grob nach tief — jeder Modus kann abbrechen:

1. **M1 Axiom-Konflikt** — Widerspruch zu bekannten Axiomen?
2. **M2 Isomorphie/Schwerpunkt** — Ähnliche Fälle im KAG?
3. **M3 Minimalannahme (Spock)** — Kleinste Zusatzannahme für Konsistenz?
4. **M4 Tempo** — Domänen-Geschwindigkeit
5. **M5 Triangulation** — Schnittmenge mehrerer Pfade
6. **M6 Geodätische** — Kürzester logischer Pfad

### Vier Urteile

| Urteil | Bedeutung |
|--------|-----------|
| **VERIFIED_CANDIDATE** (grün) | Bestätigt, hohe Konfidenz |
| **PLAUSIBLE_HYPOTHESIS** (gelb) | Nicht verurteilt, aber nicht final bewiesen |
| **INDETERMINATE_UNSAFE** (orange) | Nicht entscheidbar, unsicher |
| **LIKELY_HALLUCINATION** (rot) | Widersprüchlich, wahrscheinlich Fehler |

---

## 4. ADJ v5 — Das Kognitive Orchester

Nach Kahnemans Dual-Process-Modell:

- **UB (schnell):** Assoziativ, energiearm, 15 Heuristiken — wie Geigen in einem Orchester.
- **B (langsam):** Regelbasiert, rechenintensiv — wie tiefe Celli.
- **Meta-Controller (MC):** Dirigent — entscheidet, wann UB reicht und wann B nachzieht.

Zusätzlich: Energie-/Stress-Modell (GABA-ähnliche Bremse), Wertesystem (Core- vs. Situations-Axiome), sechs parallele „Stimmen" (Hash, FAISS, UB, Isomorphie, Annahme, MC).

**V5_FULL (v5.24b):** Der MC-Router ruft über `v5_adapter.py` den MetaController aus dem v5-Prototyp auf — echte UB→B-Oszillation, kein Fallback auf V4-Ein-Pass mehr.

---

## 5. ADJ als eigenständiges System

ADJ ist ein **eigenes Projekt**. Es prüft epistemisch: *Stimmt diese Behauptung?*

- Eingabe: Behauptung Z, Kontext, Domäne (über `PruefRequest` / `adj_service`)
- Intern: MC-Router → v4-Tribunal oder v5-Orchester
- Ausgabe: `FinalStatus`, Konfidenz C_new, Flags, Laufzeit

Keine Abhängigkeit von anderen Projekten. Externe Systeme *können* ADJ optional anbinden — das ist aber nicht Teil des ADJ-Kerns.

---

## 6. Empirische Ergebnisse

### Hauptergebnisse (487 Cases, ideal_adj)

| Metrik | Wert |
|--------|------|
| Pass gesamt | **487/487 (100 %)** |
| LH (Halluzination) | 159/159 |
| VC (Verifiziert) | 109/109 |
| IU (Unentscheidbar) | 46/46 |
| PH (Plausibel) | 173/173 |

### S4 — Vergleich mit Baselines

| System | Korrekt | Genauigkeit |
|--------|---------|-------------|
| **ADJ** | **487/487** | **100 %** |
| LLM-Judge (heuristisch) | 293/487 | 60,2 % |
| POPPER (regelbasiert) | 168/487 | 34,5 % |
| SelfCheckGPT (heuristisch) | 76/487 | 15,6 % |

McNemar-Test: ADJ signifikant besser gegen alle drei Baselines (p≈0).

### S3 — Wissenschaftliche Belastbarkeit

- ECE 0,435 (Konfidenz etwas unterkalibriert — dokumentiert, kein Blocker)
- Robustheit unter Rauschen: 96,5 %
- Kurze Claims (<10 Wörter): 80,7 %
- Reproduzierbarkeit: deterministisch ✅
- Median ~811 ms/Case

---

## 7. Grenzen und Ausblick

**Was funktioniert:** 100 % auf 487 Cases, alle Gates grün, V5_FULL produktiv, deutlicher Vorsprung gegen Baselines.

**Was noch offen ist:**

- Konfidenz-Kalibrierung (ECE) verbesserungsfähig
- Deutsche/kurze Claims schwächer als englische/lange
- Baselines ohne Live-API (Heuristiken)

**Nächste Schritte:** Zenodo-Upload mit DOI, optional GPT-4o-mini-Vergleich, PH-Feintuning.

---

## 8. Metaphern (Kurz)

| v4 Tribunal | v5 Orchester |
|-------------|--------------|
| Gericht mit Ankläger, Richter, Archivar | Orchester mit Geigen (UB), Celli (B), Dirigent (MC) |
| Gesetzestext | Erfahrener Richter |
| Falsifikationstrichter | Energie + Stress + Taktgeber |

---

## Literatur (Auswahl)

1. Popper, K. R. (1934). *Logik der Forschung*.
2. Kahneman, D. (2011). *Thinking, Fast and Slow*.
3. Hofstadter, D. R. (1979). *Gödel, Escher, Bach*.
4. ADJ-Systemdokumentation v4/v5. https://github.com/Masterq83/ADJ-System

---

*Basierend auf `docs/ZENODO_PUBLIKATION.md` v6.0 — lesbare Normal-Variante für den Autor.*

> **Aktuell:** Siehe **`docs/PAPER_DE_v6.1.md`** (EPI-Suite, Live-Baselines, FEVER, Metapher→Erkenntnis).
