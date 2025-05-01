
## 🛠️ SupportMonitoring

**SupportMonitoring** is a Django-based dashboard for tracking the status of TCP, API, and SFTP targets in real-time. It includes health checks and a Plotly-powered graph to visualize SFTP file activity.


## 🚀 Features

- ✅ Monitor TCP services (e.g., ports open/closed)
- 🌐 Check HTTP status codes of APIs
- 📂 Connect to SFTP servers and count files
- 📊 Visualize file count history with Plotly
- 🔄 Auto-refresh and dropdown filtering

---

Sure! Here's a clean and clear section you can include in your `README.md` for your error alerting system — covering **email alerts**, **Jira ticket creation**, and **SMS notifications**.

---

## ⚠️ Error Alerting System Overview

This project includes simple Python utilities to automatically notify and respond to system failures using:

- 📧 Email alerts (`email_alert.py`)
- 🧾 Jira ticket creation (`jira_alert.py`)
- 📱 SMS notifications via Twilio (`twilio_alert.py`)

Each utility can be configured via **hardcoded values** or loaded from a `config.json` file.

---

### 📧 Email Alert Sender – `email_alert.py`

Sends an alert email when a service check fails.

#### Example usage:

```python
from email_alert import send_email

send_email("Alert: API down", "The OpenAI API returned a 500 error.")
```

#### Config structure (optional):

```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "email_username": "your_email@example.com",
  "email_password": "your_password",
  "email_recipient": "admin@example.com"
}
```

---

### 🧾 Jira Ticket Creator – `jira_alert.py`

Automatically creates a Jira ticket for a failed system check. It includes logic to avoid duplicate tickets based on summary text.

#### Example usage:

```python
from jira_alert import create_jira_ticket

create_jira_ticket("API Failure", "OpenAI returned 500 error on healthcheck.")
```

#### Duplicate Check:

The tool checks if a ticket with the same summary already exists in the project before creating a new one.

#### Config structure:

```json
{
  "jira_url": "https://yourdomain.atlassian.net",
  "jira_email": "you@example.com",
  "jira_api_token": "your_api_token",
  "jira_project_key": "PROJ",
  "jira_assignee": "admin"
}
```

---

### 📱 SMS Notification – `twilio_alert.py`

Sends SMS alerts using the Twilio API.

#### Example usage:

```python
from twilio_alert import send_sms

send_sms("+1234567890", "System Alert: Database is unreachable.")
```

#### Config structure:

```json
{
  "twilio_account_sid": "your_sid",
  "twilio_auth_token": "your_token",
  "twilio_from_number": "+15005550006",
  "twilio_to_number": "+1234567890"
}
```

---

## 🧱 Requirements

- Python 3.8+
- Django 4.x
- Plotly.js (loaded via CDN)
- Paramiko
- Requests

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/igearfs/SupportMonitoring.git
cd SupportMonitoring
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🗃️ Database Setup

Initialize the SQLite database:

```bash
python manage.py migrate
```

(Optional) Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

---

## 🏁 Running the App

```bash
python manage.py runserver
```

Then open your browser to:  
http://127.0.0.1:8000/

---

## 🧪 Adding Targets

Targets are defined in `views.py` as a hardcoded list. Modify the `targets` array to add/remove monitored services.

---

## 🖼️ Screenshots

- Dashboard with live monitor tables
- Plotly graph for SFTP activity
- Dropdown filtering by host

---

## 📂 Project Structure

```
resourcemonitor/
├── views.py
├── urls.py
├── templates/
│   └── resourcemonitor/dashboard.html
├── static/
│   └── resourcemonitor/js/dashboard.js
├── sftp_monitor.py
├── api_monitor.py
├── tcp_monitor.py
└── ...
```

---

### 🚀 Future Features:

1. **Email Notification System**:
   - A generic class to send an email notification when an error occurs.
   - Support for multiple email servers, including:
     - User/pass login configuration.
     - Integration with Microsoft Flow (using the URL flow).
   - Option to dynamically update a list of users without restarting the server. This would allow users to be added or removed from the notification list without any downtime.

2. **Jira Ticket**:  
   - [**Email Notification System & Dynamic User List for Error Handling**](https://jira.yourcompany.com/browse/TICKET_ID)
   - A Jira ticket has been created for tracking the development of the email notification system and dynamic user list feature. Check the ticket for updates and progress.

3. **Error Handling Enhancement**:
   - Ability to trigger the email notifications in case of system failures, error logs, or important events.
   - Ensure proper error logging and detailed alerts, including:
     - Error type and message.
     - Host or service related to the error.

4. **Dynamic User List**:
   - Ability to manage a list of users for notifications through a simple file-based mechanism (like a `.txt` or `.json` file).
   - Users should be able to add/remove entries to the list, and the system should update without requiring a server restart.
   - Ensure proper validation of email addresses and smooth integration with the email notification system.

---
---

## ⚖️ License

MIT License — see the [LICENSE](LICENSE) file for details.  
© 2024 In-Game Event, A Red Flag Syndicate LLC.
```

---
