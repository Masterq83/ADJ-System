#!/usr/bin/env python3
"""Assemble Zenodo upload bundle: paper PDF source, benchmark summaries, result copies."""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "benchmarks" / "results"
OUT = DOCS / "zenodo_release_v6.1"

# Patterns removed from public Zenodo artefacts (trade secrets / local paths)
_SANITIZE: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"E:\\\\Cursor Projekte\\\\ADJ-System", re.I), "benchmarks"),
    (re.compile(r"E:/Cursor Projekte/ADJ-System", re.I), "benchmarks"),
    (re.compile(r'E:\\\\buvmkey\.txt', re.I), "NVIDIA_API_KEY (env)"),
    (re.compile(r"E:/buvmkey\.txt", re.I), "NVIDIA_API_KEY (env)"),
    (re.compile(r"E:\\\\buvmkey\.txt", re.I), "NVIDIA_API_KEY (env)"),
    (re.compile(r"buvmkey\.txt", re.I), "NVIDIA_API_KEY (env)"),
    (re.compile(r"OpenJarvis|OpenMythos|Hermes", re.I), "Agent"),
    (re.compile(r"adj-prototype[/\\]?", re.I), "(proprietary implementation)"),
    (re.compile(r"benchmarks/scripts/", re.I), "(not public)"),
    (re.compile(r"build_epi_corpora\.py", re.I), "(proprietary)"),
    (re.compile(r"comparison_report\.py", re.I), "(proprietary)"),
]

# Key artefacts for supplementary upload (no internal-only caveman docs)
ARTEFACTS = [
    ("benchmarks/results/comparison_report.md", "01_EPI487_comparison_report.md"),
    ("benchmarks/results/comparison_stats.json", "01_EPI487_comparison_stats.json"),
    ("benchmarks/results/s3_evaluation.md", "02_S3_calibration_robustness.md"),
    ("benchmarks/results/epi_epi-h120_20260705T085733Z/EPI_REPORT_CAVEMAN.md", "03_EPI-H120_holdout.md"),
    ("benchmarks/results/epi_epi-h120_20260705T085733Z/epi_report.json", "03_EPI-H120_holdout.json"),
    ("benchmarks/results/epi_epi-z100_20260705T085857Z/EPI_REPORT_CAVEMAN.md", "04_EPI-Z100_gap_z.md"),
    ("benchmarks/results/epi_epi-z100_20260705T085857Z/epi_report.json", "04_EPI-Z100_gap_z.json"),
    ("benchmarks/results/epi_epi-live487_20260705T110726Z/EPI_REPORT_CAVEMAN.md", "05_EPI-LIVE487_live_baselines.md"),
    ("benchmarks/results/epi_epi-live487_20260705T110726Z/epi_report.json", "05_EPI-LIVE487_live_baselines.json"),
    ("benchmarks/results/fever_medium_20260705T075920Z/FEVER_PAPER_METRICS_CAVEMAN.md", "06_FEVER500_transfer.md"),
    ("benchmarks/results/fever_medium_20260705T075920Z/fever_paper_metrics.json", "06_FEVER500_transfer.json"),
    ("benchmarks/specs/epi_suite.json", "07_EPI_suite_specification.json"),
    ("benchmarks/corpora/epi_manifest.json", "08_EPI_corpus_manifest.json"),
    ("benchmarks/human_eval_pack/RATER_ANLEITUNG.md", "09_HUMAN30_rater_anleitung.md"),
    ("benchmarks/human_eval_pack/rater_sheet.csv", "09_HUMAN30_rater_sheet_template.csv"),
    ("docs/PAPER_SECTION9_DRAFT.md", "10_PAPER_section9_empirie.md"),
    ("docs/BENCHMARK_SUITE_PAPER.md", "12_BENCHMARK_suite_spec.md"),
]


def _sanitize_text(text: str) -> str:
    for pat, repl in _SANITIZE:
        text = pat.sub(repl, text)
    return text


def _sanitize_json_obj(obj: object) -> object:
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in ("key_path", "key_file"):
                continue
            if k == "corpus_path" and isinstance(v, str):
                name = Path(v.replace("\\", "/")).name
                out[k] = f"benchmarks/corpora/{name}"
                continue
            out[k] = _sanitize_json_obj(v)
        return out
    if isinstance(obj, list):
        return [_sanitize_json_obj(x) for x in obj]
    if isinstance(obj, str):
        s = _sanitize_text(obj)
        if "corpus_path" in s or s.endswith(".json") or s.endswith(".py"):
            # Keep relative corpus references only
            s = re.sub(r"^benchmarks/", "benchmarks/", s)
            s = s.replace("benchmarks\\corpora\\", "benchmarks/corpora/")
        return s
    return obj


def _redact_epi_manifest(data: dict) -> dict:
    """Holdout case IDs stay local — publish counts/protocol only."""
    out = {
        "generated_at": data.get("generated_at"),
        "source": "adj_expanded_v3 (proprietary corpus — not in supplement)",
        "source_n": data.get("source_n"),
        "seed": data.get("seed"),
        "holdout_protocol": data.get("holdout_protocol"),
        "note": "Full labelled corpora and implementation are proprietary. "
        "This manifest lists benchmark sizes only.",
        "benchmarks": {},
    }
    for name, block in (data.get("benchmarks") or {}).items():
        if isinstance(block, dict):
            out["benchmarks"][name] = {
                k: v for k, v in block.items() if k not in ("ids", "case_ids", "cases")
            }
        else:
            out["benchmarks"][name] = block
    return out


def _write_sanitized_copy(src: Path, dst: Path) -> None:
    if src.suffix == ".json":
        data = json.loads(src.read_text(encoding="utf-8"))
        if src.name == "epi_manifest.json":
            data = _redact_epi_manifest(data)
        else:
            data = _sanitize_json_obj(data)
        dst.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        dst.write_text(_sanitize_text(src.read_text(encoding="utf-8")), encoding="utf-8")


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    manifest = {
        "version": "v6.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "preprint_md": "docs/ZENODO_PUBLIKATION.md",
        "preprint_pdf": "docs/ADJ_System_v6.1_Preprint.pdf",
        "copied": [],
        "missing": [],
    }

    for src_rel, dst_name in ARTEFACTS:
        src = ROOT / src_rel
        dst = OUT / dst_name
        if src.exists():
            _write_sanitized_copy(src, dst)
            manifest["copied"].append({"src": src_rel, "dst": dst_name})
        else:
            manifest["missing"].append(src_rel)

    # Master summary (Zenodo description supplement)
    summary = """# ADJ v6.1.1 — Benchmark Results Summary (Zenodo Supplement)

**Preprint:** ZENODO_PUBLIKATION.md v6.1 | **Date:** 2026-07-05 (bundle v6.1.1)

## EPI Suite — Published Results

| Benchmark | n | ADJ Acc | Best Baseline | Notes |
|-----------|---|---------|---------------|-------|
| EPI-487 | 487 | **100%** | LLM-Judge 60.2% | McNemar p≈0 |
| EPI-H120 Holdout | 120 | **100%** | LLM 67.5% | Generalization |
| EPI-Z100 Gap-Z | 100 | **100%** | LLM 67.0% | 0% PH↔LH error |
| EPI-LIVE487 | 487 | **100%** | LLM-live **77.4%** | NVIDIA dual-key |
| FEVER-500 Transfer | 500 | 0% FEVER-3 | SelfCheck 7.0% | 0 false commits |
| EPI-HUMAN30 | 30 | pending | — | Rater pack on GitHub |

## Implementation

The ADJ reference implementation and labelled benchmark corpora are **proprietary**
(Funk!Werk Ai Solutions). This supplement contains **published metrics and reports only** —
no source code, no full case labels, no reproduction scripts.

Human evaluation: https://github.com/Masterq83/ADJ-System/tree/main/benchmarks/human_eval_pack

## License

CC0 1.0 — see preprint header.
"""
    (OUT / "00_BENCHMARK_RESULTS_SUMMARY.md").write_text(summary, encoding="utf-8")

    manifest["bundle_dir"] = str(OUT.relative_to(ROOT))
    manifest["bundle_version"] = "v6.1.1"
    manifest["trade_secret_note"] = "No implementation source or labelled corpora in this bundle."
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    zip_path = DOCS / "zenodo_release_v6.1.zip"
    if zip_path.exists():
        zip_path.unlink()
    shutil.make_archive(str(zip_path.with_suffix("")), "zip", OUT)
    print(f"Zenodo ZIP: {zip_path}")

    readme = DOCS / "ZENODO_UPLOAD_README.md"
    readme.write_text(
        f"""# Zenodo Upload v6.1 — Checkliste

**Generiert:** {manifest['generated_at']}

## Pflicht-Dateien

| Datei | Beschreibung |
|-------|--------------|
| `docs/ADJ_System_v6.1_Preprint.pdf` | Haupt-Preprint (PDF) |
| `docs/ZENODO_PUBLIKATION.md` | Preprint Markdown |
| `docs/zenodo_release_v6.1/` | Benchmark-Supplement (dieser Ordner) |

## Upload auf Zenodo

1. https://zenodo.org/deposit/new
2. Upload type: Publication → Preprint
3. Title/Authors/Keywords aus `docs/ZENODO_DOI.md`
4. Dateien: PDF + `zenodo_release_v6.1/` als ZIP oder Einzeldateien
5. Description: Abstract aus ZENODO_PUBLIKATION.md + Verweis auf Supplement
6. License: CC0 1.0
7. Version: **v6.1** (2026-07-05)
8. DOI reservieren → in ZENODO_PUBLIKATION.md eintragen

## Nach Human Eval (optional vor Publish)

```powershell
python benchmarks/scripts/score_human_eval.py benchmarks/human_eval_pack/rater_sheet_*.csv
```

Ergebnis in §9.6 eintragen und PDF neu generieren.

## Fehlende Artefakte

{json.dumps(manifest['missing'], indent=2) if manifest['missing'] else 'Keine — alle kopiert.'}
""",
        encoding="utf-8",
    )

    print(f"Zenodo bundle: {OUT}")
    print(f"Copied: {len(manifest['copied'])} | Missing: {len(manifest['missing'])}")
    print(f"Upload readme: {readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
