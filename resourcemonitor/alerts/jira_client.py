import os
import json
import requests
from requests.auth import HTTPBasicAuth

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r") as f:
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
    """
    Creates a new Jira issue if one doesn't already exist.
    Returns True if the ticket was created successfully, False if it's a duplicate.
    """
    config = config or load_config()
    if issue_exists(summary, config=config):
        print(f"⚠️ Duplicate Jira ticket detected for: {summary}")
        return False  # Duplicate, do not send alerts

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
            return True  # Issue created, proceed with alerts
        else:
            print(f"❌ Failed to create issue: {response.status_code} {response.text}")
            return False  # Failed to create issue
    except Exception as e:
        print(f"❌ Error while creating issue: {e}")
        return False  # Error while creating issue
