"""Deployment, workflow, Dockerfile, and dashboard contract regression tests."""

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_dockerfile_uses_no_sync_and_port_8080():
    """Dockerfile must not re-sync packages at container startup and must listen on 8080."""
    dockerfile = (REPO_ROOT / "Dockerfile").read_text(encoding="utf-8")
    assert "--no-sync" in dockerfile, "Dockerfile CMD must pass --no-sync to uv run"
    assert "8080" in dockerfile


def test_deploy_workflow_contract():
    """deploy.yml must enforce memory limits, scale-to-zero, IAP-safe auth, and WIF."""
    deploy_path = REPO_ROOT / ".github" / "workflows" / "deploy.yml"
    raw = deploy_path.read_text(encoding="utf-8")
    parsed = yaml.safe_load(raw)

    assert "deploy" in parsed["jobs"]
    assert "--memory 2Gi" in raw or "--memory 1Gi" in raw
    assert "--min-instances 0" in raw
    assert "--no-allow-unauthenticated" in raw
    assert "--allow-unauthenticated" not in raw
    assert "IAP_ENABLED" in raw
    assert "DEPLOYED_IMAGE" in raw
    assert "--include-email" in raw
    assert "hackathon-y26" not in raw
    assert "922201496337" not in raw


def test_dashboard_html_uses_idle_aware_polling():
    """Dashboard HTML must not run an unconditional top-level setInterval poll."""
    html = (REPO_ROOT / "app" / "static" / "dashboard.html").read_text(encoding="utf-8")
    assert "startDemoSession" in html
    assert "stopDemoSession" in html
    assert "visibilitychange" in html
    assert "setInterval(fetchTelemetry, 4000)" not in html.splitlines()[-10:]


def test_no_stale_legacy_project_ids():
    """Prevent legacy hackathon-y26 / 922201496337 references from creeping back in."""
    checked_paths = [
        REPO_ROOT / "DEMO_SCRIPT.md",
        REPO_ROOT / "deployment_metadata.json",
        REPO_ROOT / "app" / "fast_api_app.py",
        REPO_ROOT / "local_tester" / "server.py",
        REPO_ROOT / ".github" / "workflows" / "deploy.yml",
        REPO_ROOT / ".github" / "workflows" / "pr-checks.yml",
    ]
    for path in checked_paths:
        content = path.read_text(encoding="utf-8")
        assert "hackathon-y26" not in content, f"Stale hackathon-y26 in {path.name}"
        assert "922201496337" not in content, f"Stale 922201496337 in {path.name}"
