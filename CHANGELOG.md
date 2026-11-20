# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added canonical Apache License 2.0 (`LICENSE`).
- Added `SECURITY.md` with private vulnerability reporting guidance and contributor security hygiene standards.
- Added root `TODO.md` tracking remaining CI/CD hardening (SHA-pinning GitHub Actions), dependency/SBOM checks, and environment-driven Cloud Run / Gemini Enterprise configuration.
- Added `CHANGELOG.md` following the Keep a Changelog format.

### Changed

- Upgraded default `GEMINI_MODEL` in `app/agent.py` from deprecated `gemini-3.5-flash` to `gemini-3.8-flash` ahead of Dec 1, 2026 Gemini 4 pricing transition.

### Security

- Added explicit least-privilege top-level `permissions: { contents: read }` and `concurrency` blocks to `.github/workflows/pr-checks.yml` and `.github/workflows/deploy.yml`.
- Pinned all GitHub Actions (`actions/checkout`, `astral-sh/setup-uv`, `google-github-actions/auth`, `google-github-actions/setup-gcloud`) to verified 40-character commit SHAs on `ubuntu-24.04` runners and added keyless Workload Identity Federation (`vars.GCP_WORKLOAD_IDENTITY_PROVIDER`) support.

## [0.1.0] - 2026-07-31

### Added

- Built the Cymbal Coffee Intelligent Procurement & Inventory Automation Agent on Google ADK with FastAPI, A2A protocol support, and A2UI visual cards.
- Added real-time IoT bin telemetry, consumption velocity forecasting, purchase order creation, anomaly detection, and notification/delivery A2UI cards (`app/tools/`, `app/a2ui_config.py`).
- Added SVG progress bar image rendering with Cloud Run URLs and scenario-matched A2UI 0.8/0.9 card generation for Gemini Enterprise.
- Added automated GitHub Actions workflows for PR unit tests/linting (`.github/workflows/pr-checks.yml`) and Cloud Run deployment + Gemini Enterprise registration (`.github/workflows/deploy.yml`).
- Added unit, integration, and evaluation test suites (`tests/`), interactive local tester (`local_tester/`), Terraform deployment scaffolding (`deployment/`), and architecture decision records (`docs/adr/`).

### Fixed

- Hardened A2A/A2UI wire-protocol serialization, `userAction` extraction, and Gemini Enterprise card rendering.
- Removed vendored `gh` CLI binaries and man pages to keep the repository clean and fix GitHub language detection.
