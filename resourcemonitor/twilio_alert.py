from twilio.rest import Client
import json

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Config file not found. Using hardcoded Twilio credentials.")
        return {
            "twilio": {
                "account_sid": "your_account_sid",
                "auth_token": "your_auth_token",
                "from_number": "+12345678900"
            }
        }

def send_sms(to_number, message, config=None):
    config = config or load_config()
    twilio_cfg = config.get("twilio", {})

    account_sid = twilio_cfg.get("account_sid")
    auth_token = twilio_cfg.get("auth_token")
    from_number = twilio_cfg.get("from_number")

    try:
        client = Client(account_sid, auth_token)
        msg = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"✅ SMS sent: SID {msg.sid}")
        return msg.sid
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")
        return None

# Example usage
if __name__ == "__main__":
    send_sms("+19876543210", "Hello! This is your monitoring alert.")
