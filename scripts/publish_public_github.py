#!/usr/bin/env python3
"""Build docs-only public tree and force-push to GitHub (Betriebsgeheimnis remediation)."""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_DOCS = [
    "ZENODO_PUBLIKATION.md",
    "PAPER_DE_v6.1.md",
    "PAPER_DE.md",
    "ADJ_System_v6.1_Preprint.pdf",
    "BENCHMARK_SUITE_PAPER.md",
    "ZENODO_DOI.md",
    "FULL_SIGNOFF.md",
    "PUBLIKATION_UND_MEDIEN.md",
    "PRÄSENTATION_v6.1.md",
    "PRÄSENTATION_FOLIENTEXTE.md",
    "Metaphors.md",
    "PAPER_SECTION9_DRAFT.md",
    "GITHUB_UPLOAD_ANLEITUNG.md",
    "ZENODO_ZIP_UPDATE_v6.1.1.md",
]

PUBLIC_SCRIPTS = [
    "scripts/create_preprint_pdf.py",
    "scripts/build_zenodo_release.py",
    "scripts/publish_public_github.py",
]

EXCLUDE_IN_HUMAN_PACK = {
    "ANALYST_blind_mapping.json",
    "pack_manifest.json",
}


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd or ROOT, check=True)


def copy_public_tree(dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    shutil.copy2(ROOT / "README.public.md", dest / "README.md")
    for name in ("LICENSE", "llms.txt", ".gitignore"):
        shutil.copy2(ROOT / name, dest / name)

    (dest / "docs").mkdir()
    for doc in PUBLIC_DOCS:
        src = ROOT / "docs" / doc
        if src.exists():
            shutil.copy2(src, dest / "docs" / doc)
        else:
            print(f"WARN missing doc: {doc}")

    for rel in (
        "benchmarks/README.md",
        "benchmarks/specs",
        "benchmarks/protocols",
        "benchmarks/human_eval_pack",
        "benchmarks/results/comparison_report.md",
        "benchmarks/results/comparison_stats.json",
        "benchmarks/results/comparison_confusion.json",
        "benchmarks/results/s3_evaluation.md",
        "benchmarks/results/s3_evaluation.json",
    ):
        src = ROOT / rel
        if not src.exists():
            print(f"WARN missing: {rel}")
            continue
        dst = dest / rel
        if src.is_dir():
            shutil.copytree(
                src,
                dst,
                ignore=lambda _d, names: [n for n in names if n in EXCLUDE_IN_HUMAN_PACK],
            )
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    for rel in PUBLIC_SCRIPTS:
        src = ROOT / rel
        dst = dest / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main() -> int:
    staging = Path(tempfile.mkdtemp(prefix="adj_public_"))
    try:
        copy_public_tree(staging)
        n = sum(1 for _ in staging.rglob("*") if _.is_file())
        print(f"Staging: {staging} ({n} files)")

        run(["git", "init"], cwd=staging)
        run(["git", "config", "user.email", "adj-system@funkwerk-ai.local"], cwd=staging)
        run(["git", "config", "user.name", "Funk!Werk Ai Solutions"], cwd=staging)
        run(["git", "branch", "-M", "main"], cwd=staging)
        run(["git", "add", "."], cwd=staging)
        run(
            [
                "git",
                "commit",
                "-m",
                "Public research bundle v6.1.1 (docs-only, no PPTX, no source)",
                "-m",
                "Preprint + EPI results + human eval. Implementation and PPTX remain local only.",
            ],
            cwd=staging,
        )
        run(["git", "remote", "add", "origin", "https://github.com/Masterq83/ADJ-System.git"], cwd=staging)
        run(["git", "push", "--force", "origin", "main"], cwd=staging)
        print("OK: force-pushed docs-only main")
        return 0
    finally:
        shutil.rmtree(staging, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
