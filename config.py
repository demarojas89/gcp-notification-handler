from pathlib import Path

from decouple import AutoConfig

REPO_ROOT = Path.cwd()
config = AutoConfig(REPO_ROOT)

GCP_PROJECT_ID = "project_id"

SLACK_BOT_TOKEN = config("SLACK_BOT_TOKEN")
SLACK_DEFAULT_CHANNEL = "default-monitoring-slack-channel"
