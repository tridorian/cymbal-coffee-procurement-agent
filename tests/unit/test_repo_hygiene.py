# Copyright 2026 Google LLC
# SPDX-License-Identifier: Apache-2.0
"""Repository metadata, link portability, and model-default hygiene tests."""

import re
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def _strip_code(md_text: str) -> str:
    without_fences = re.sub(r"```.*?```", "", md_text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", without_fences)


def test_pyproject_metadata_is_populated_and_apache_licensed() -> None:
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = pyproject["project"]
    assert project["name"] == "cymbal-coffee-procurement-agent"
    assert project["readme"] == "README.md"
    assert project["description"].strip() != ""
    license_val = project["license"]
    if isinstance(license_val, dict):
        assert license_val.get("text") == "Apache-2.0"
    else:
        assert license_val == "Apache-2.0"
    for author in project.get("authors", []):
        assert author.get("name") != "Your Name"
        assert author.get("email") != "your@email.com"


def test_docs_and_readme_contain_zero_file_uris_and_valid_relative_links() -> None:
    md_files = [REPO_ROOT / "README.md", *sorted((REPO_ROOT / "docs").rglob("*.md"))]
    broken: list[str] = []
    for md_path in md_files:
        raw = md_path.read_text(encoding="utf-8")
        rel_doc = md_path.relative_to(REPO_ROOT).as_posix()
        assert "file://" not in raw, f"{rel_doc} contains non-portable file:// URI"
        prose = _strip_code(raw)
        for match in LINK_RE.finditer(prose):
            raw_target = match.group(1).strip()
            if not raw_target:
                continue
            target = raw_target.split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            resolved = (md_path.parent / clean).resolve()
            if not resolved.is_relative_to(REPO_ROOT) or not resolved.exists():
                broken.append(f"{rel_doc}: broken relative link '{raw_target}'")
    assert broken == []


def test_default_gemini_model_is_upgraded_from_deprecated_35_flash() -> None:
    agent_src = (REPO_ROOT / "app" / "agent.py").read_text(encoding="utf-8")
    assert '"gemini-3.8-flash"' in agent_src
    assert "gemini-3.5-flash" not in agent_src
