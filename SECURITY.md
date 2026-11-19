# Security Policy

## Supported Versions

Security fixes are applied to the latest commit on the `main` branch.

| Version / Branch | Supported |
| ---------------- | --------- |
| `main` (latest)  | Yes       |
| Older commits    | No        |

## Reporting a Vulnerability

Please **do not** report security vulnerabilities through public GitHub issues, pull requests, or discussions.

Instead, report potential vulnerabilities privately using one of the following methods:

1. **GitHub Private Vulnerability Reporting (Preferred):** Navigate to the **Security** tab of `wtg-codes/cymbal-coffee-procurement-agent` and click **Report a vulnerability** to open a private security advisory.
2. **Direct Maintainer Contact:** If private vulnerability reporting is not enabled, contact the repository maintainer directly through GitHub (`@wtg-codes`) without posting exploit details or sensitive data publicly.

### What to Include

To help reproduce and resolve the issue quickly, please include:

- A clear description of the vulnerability and its potential impact.
- Steps to reproduce, proof-of-concept request/payload, or affected files/endpoints (for example, FastAPI/A2A endpoints, A2UI card rendering/post-processing, ADK tools, or GitHub Actions workflows).
- Any suggested mitigations or fixes, if known.

### Response Expectations

- **Acknowledgment:** Within 5 business days of receipt.
- **Triage & Updates:** We will confirm scope, severity, and remediation plans as investigation progresses.
- **Disclosure:** Please allow reasonable time to patch and verify a fix before public disclosure.

## Security Hygiene for Contributors

- Never commit API keys, service account JSON files, OAuth client secrets, `.env` files, or private internal endpoints.
- Store production credentials in Google Cloud Secret Manager and GitHub Actions Secrets rather than source files or plain-text environment variables.
- Run `gitleaks dir . --no-banner` and `actionlint` before opening pull requests.
