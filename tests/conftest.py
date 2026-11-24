import os

import google.auth
import google.auth.credentials

os.environ.setdefault("GOOGLE_CLOUD_PROJECT", "gemini-ent-playground")
os.environ.setdefault("GCP_PROJECT", "gemini-ent-playground")
os.environ.setdefault("CLOUDSDK_CORE_PROJECT", "gemini-ent-playground")
os.environ["DISABLE_OTEL_TRACING"] = "true"

# Mock google.cloud.logging.Client to prevent GCP API calls in unit tests
try:
    from unittest.mock import MagicMock

    import google.cloud.logging

    google.cloud.logging.Client = MagicMock()
except ImportError:
    pass

# Mock google.adk.telemetry.google_cloud.get_gcp_exporters
try:
    import google.adk.telemetry.google_cloud

    google.adk.telemetry.google_cloud.get_gcp_exporters = lambda *args, **kwargs: []
except (ImportError, AttributeError):
    pass
