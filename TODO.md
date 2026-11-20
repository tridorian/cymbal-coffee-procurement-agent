# TODO

Structured engineering, security, and compliance backlog for `cymbal-coffee-procurement-agent`.
For historical milestone notes and demo architecture details, also see [`docs/PROJECT_STATUS_AND_TODO.md`](docs/PROJECT_STATUS_AND_TODO.md).

## CI/CD & Workflow Hardening

- [x] **Pin all third-party GitHub Actions to full 40-char commit SHAs** (with version comments) across workflows:
  - `.github/workflows/pr-checks.yml`: `actions/checkout`, `astral-sh/setup-uv`, `google-github-actions/auth`
  - `.github/workflows/deploy.yml`: `actions/checkout`, `google-github-actions/auth`, `google-github-actions/setup-gcloud`
- [x] **Add `concurrency` blocks** to `.github/workflows/pr-checks.yml` (with `cancel-in-progress: true` on pull requests) and `.github/workflows/deploy.yml` (serialized deploys without canceling an active rollout).
- [x] **Migrate GCP CI authentication to Workload Identity Federation (WIF)** instead of static `secrets.GCP_CREDENTIALS` JSON keys where supported.
- [ ] **Run `actionlint` in CI** so workflow regressions are caught automatically on every pull request.

## Supply-Chain, SBOM & OSS Compliance

- [x] **Add automated secret scanning (`gitleaks`)** to `.github/workflows/pr-checks.yml`.
- [ ] **Generate and scan SBOMs (`syft` + `grype`)** for Python dependencies (`uv.lock`) and the production `Dockerfile` container image during CI/release builds.
- [ ] **Enforce SPDX license headers** (`SPDX-License-Identifier: Apache-2.0`) on Python source files and scripts using `addlicense -check -l apache` or `reuse lint`.
- [ ] **Enable Dependabot or Renovate** for `uv` dependencies, Docker base images, and GitHub Actions updates.
- [x] **Update package metadata in `pyproject.toml`** (license field `Apache-2.0`, repository description, and maintainer metadata).

## Cloud Run & Gemini Enterprise Configuration Hygiene

- [ ] **Keep Cloud Run and Gemini Enterprise configuration strictly environment-driven**:
  - Replace hardcoded project/service identifiers (`PROJECT_ID`, `PROJECT_NUMBER`, `REGION`, `SERVICE`, `APP_URL`, `GE_APP_ID`, `GE_AGENT_ID`, `GOOGLE_CLOUD_PROJECT`) in `.github/workflows/deploy.yml` and `.github/workflows/pr-checks.yml` with GitHub Actions repository/environment variables (`vars.*`) and secrets (`secrets.*`).
  - Keep `.env.example` synchronized with all required runtime environment variables and avoid committing environment-specific endpoints or identifiers in source or workflow files.
- [ ] **Review Cloud Run IAM exposure** (`--allow-unauthenticated` in `deploy.yml`) and document whether IAP or authenticated A2A invocation should be enforced outside public demo environments.

## Application & Documentation Follow-Ups

- [ ] **Multi-Tenant Store Telemetry Scaling**: Extend `STORE_TELEMETRY` to support additional regional branches (carried forward from `docs/PROJECT_STATUS_AND_TODO.md`).
- [x] **Replace machine-specific `file://` links** in `docs/PROJECT_STATUS_AND_TODO.md` and `docs/DEVELOPMENT_AND_DEPLOYMENT_FLOW.md` with repo-relative Markdown links.
