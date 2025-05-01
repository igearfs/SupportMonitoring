### ❤️ Support This Project

If you find this project useful or want to support continued development:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/igearfs)

Your support fuels prototypes, uptime tools, and indie infrastructure builds.

---

# ⚠️ PROTOTYPE — SupportMonitoring System

**SupportMonitoring** is a Django-based observability dashboard for tracking the real-time status of TCP, HTTP, and SFTP services.

This prototype includes a health-check dashboard, Plotly-powered visualizations, and an optional alerting system via email, Jira, or Twilio SMS.

> **Use in internal environments only** — see [Known Issues](#known-issues) for current limitations.

---

## 🚀 Features

- ✅ Monitor TCP services (port open/closed)
- 🌐 Check HTTP status codes of APIs
- 📂 Count files on remote SFTP servers
- 📊 Visualize file count history using Plotly
- 🔄 Auto-refresh and dropdown filtering
- 📢 Optional alerting via:
  - 📧 Email
  - 📱 SMS (Twilio)
  - 🧾 Jira ticket creation

---

## 🧱 Requirements

- Python 3.10 or higher (tested with 3.12)
- Django
- `requests`, `twilio` (optional alerts)

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your/repo.git
cd your-repo
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Django Server

```bash
python manage.py runserver
```

---

## 🔍 Target Configuration

Targets are defined in `views.py`:

```python
targets = [
    {"name": "Google", "host": "google.com", "port": 443, "type": "TCP"},
    {"name": "OpenAI API", "host": "api.openai.com", "port": 443, "url": "https://api.openai.com/v1/", "type": "API"},
    {"name": "Test SFTP", "host": "test.rebex.net", "port": 22, "username": "demo", "password": "password", "remote_dir": "/pub/example/", "type": "SFTP"},
    ...
]
```

Supported types: `"TCP"`, `"API"`, `"SFTP"`, `"LAMBDA"`

---

## 🔔 Alerting System (Optional)

All alerts are triggered via `send_alert()` and configured through `alerts_utils.py`.

### Configurable Alerts:

- 📧 Email: `email_alert.py`
- 🧾 Jira: `jira_alert.py`
- 📱 SMS: `twilio_alert.py`

Each can use hardcoded settings or a root-level `config.json`.

---

### Sample `config.json`:

```json
{
  "email": {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "username": "user@example.com",
    "password": "yourpassword",
    "from_email": "user@example.com",
    "to_email": "admin@example.com"
  },
  "twilio": {
    "account_sid": "your-sid",
    "auth_token": "your-token",
    "from_number": "+1234567890",
    "to_number": "+0987654321"
  },
  "jira": {
    "base_url": "https://your-domain.atlassian.net",
    "username": "your-email@example.com",
    "api_token": "your-api-token",
    "project_key": "PROJECT"
  }
}
```

---

## 🧪 GitHub Actions / CI

This project includes CI for Django test runs via GitHub Actions:

```yaml
# .github/workflows/django.yml
name: Django CI
...
```

---

## 📂 Project Structure

```
resourcemonitor/
├── views.py
├── alerts_utils.py
├── email_alert.py
├── jira_alert.py
├── twilio_alert.py
├── templates/
├── static/
└── ...
```

---

## 📈 Future Enhancements

- 🔐 Auth support for dashboard
- 🐳 Dockerfile and docker-compose support
- 🌐 Deployment options (Heroku, EC2, etc.)
- 👥 Dynamic alert recipient list (file-based)
- 🔁 Live config reload (no restart needed)

---

## 📎 Known Issues

- 🛠️ This is a prototype — stability, features, and alerting flows are still evolving.
- ❌ Not HTTPS compliant. Intended for **internal environments only**.
- 🚨 Alerting tools are implemented but **not fully tested** in all cases.
- 🧪 No frontend tests or coverage validation yet.
- ⚠️ Hardcoded targets — no admin UI for editing yet.

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for development setup, roadmap tasks, and contribution guidelines.

---

## ⚖️ License

MIT License — see [LICENSE](LICENSE).  
© 2024 In-Game Event / Red Flag Syndicate LLC.

---
