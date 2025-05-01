import json
import requests
from requests.auth import HTTPBasicAuth

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Config file not found. Using hardcoded values.")
        return {
            "jira": {
                "base_url": "https://your-domain.atlassian.net",
                "username": "your-email@example.com",
                "api_token": "your-api-token",
                "project_key": "YOURPROJECT"
            }
        }

def issue_exists(summary, config=None):
    config = config or load_config()
    jira_cfg = config.get("jira", {})

    base_url = jira_cfg.get("base_url")
    username = jira_cfg.get("username")
    api_token = jira_cfg.get("api_token")
    project_key = jira_cfg.get("project_key")

    url = f"{base_url.rstrip('/')}/rest/api/2/search"
    auth = HTTPBasicAuth(username, api_token)
    headers = {
        "Accept": "application/json"
    }

    jql = f'project = "{project_key}" AND summary ~ "{summary}" ORDER BY created DESC'
    params = {"jql": jql, "maxResults": 1}

    try:
        response = requests.get(url, headers=headers, auth=auth, params=params)
        if response.status_code == 200:
            issues = response.json().get("issues", [])
            return len(issues) > 0
        else:
            print(f"⚠️ Failed to check for duplicates: {response.status_code} {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error during duplicate check: {e}")
        return False

def create_jira_issue(summary, description, issue_type="Task", config=None):
    if issue_exists(summary, config=config):
        print(f"⚠️ Duplicate detected. Jira ticket with similar summary already exists.")
        return None

    config = config or load_config()
    jira_cfg = config.get("jira", {})

    base_url = jira_cfg.get("base_url")
    username = jira_cfg.get("username")
    api_token = jira_cfg.get("api_token")
    project_key = jira_cfg.get("project_key")

    url = f"{base_url.rstrip('/')}/rest/api/2/issue"
    auth = HTTPBasicAuth(username, api_token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type}
        }
    }

    try:
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        if response.status_code == 201:
            key = response.json().get("key")
            print(f"✅ Created Jira issue: {key}")
            return key
        else:
            print(f"❌ Failed to create issue: {response.status_code} {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error while creating issue: {e}")
        return None

# Example usage
if __name__ == "__main__":
    create_jira_issue(
        summary="Database connection failure on Server X",
        description="Cannot connect to the database on 10.0.0.4. Port 5432 timeout.",
    )
