# email_sender.py

import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent / "config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {}

def send_email(to_email, subject, body, config=None):
    config = config or load_config()
    email_cfg = config.get("email", {})

    smtp_server = email_cfg.get("smtp_server", "smtp.example.com")
    smtp_port = email_cfg.get("smtp_port", 587)
    username = email_cfg.get("username", "default@email.com")
    password = email_cfg.get("password", "changeme")
    from_email = email_cfg.get("from_email", username)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            print("✅ Email sent successfully.")
            return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False
