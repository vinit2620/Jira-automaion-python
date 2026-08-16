import requests
from requests.auth import HTTPBasicAuth
from config import Config

class JiraClient:
    def __init__(self):
        Config.validate()
        self.base_url = Config.JIRA_BASE_URL.rstrip('/')
        self.auth = HTTPBasicAuth(Config.JIRA_USER_EMAIL, Config.JIRA_API_TOKEN)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_issue(self, summary: str, description: str, issue_type: str = "Task", project_key: str = None) -> dict:
        """
        Creates an issue in Jira Cloud using REST API v3.
        """
        url = f"{self.base_url}/rest/api/3/issue"
        key = project_key or Config.JIRA_PROJECT_KEY

        payload = {
            "fields": {
                "project": {
                    "key": key
                },
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description
                                }
                            ]
                        }
                    ]
                },
                "issuetype": {
                    "name": issue_type
                }
            }
        }

        try:
            response = requests.post(
                url,
                json=payload,
                headers=self.headers,
                auth=self.auth
            )
            response.raise_for_status()
            data = response.json()
            print(f"✅ Issue created successfully! Key: {data.get('key')} (ID: {data.get('id')})")
            return data

        except requests.exceptions.HTTPError as err:
            print(f"❌ HTTP Error ({response.status_code}): {response.text}")
            raise err
        except requests.exceptions.RequestException as err:
            print(f"❌ Connection Error: {err}")
            raise err