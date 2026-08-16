import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
    JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

    @classmethod
    def validate(cls):
        missing = [key for key in ["JIRA_BASE_URL", "JIRA_USER_EMAIL", "JIRA_API_TOKEN", "JIRA_PROJECT_KEY"] if not getattr(cls, key)]
        if missing:
            raise ValueError(f"Missing required environment variables in .env: {', '.join(missing)}")