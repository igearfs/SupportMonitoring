from twilio.rest import Client
import json
import os

def load_config():
    """Load Twilio credentials from config.json or use hardcoded defaults."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Config file not found at:", config_path)
        print("🔁 Using hardcoded Twilio credentials.")
        return {
            "twilio": {
                "account_sid": "your_account_sid",  # Replace with your Twilio Account SID
                "auth_token": "your_auth_token",    # Replace with your Twilio Auth Token
                "from_number": "+12345678900"       # Replace with your Twilio phone number
            }
        }


def send_sms_alert(to_number, message, config=None):
    """
    Sends an SMS alert via Twilio.

    Args:
        to_number (str): The recipient's phone number.
        message (str): The message body to send.
        config (dict, optional): Configuration dictionary to override default values.

    Returns:
        str: The SID of the sent message if successful, None otherwise.
    """
    config = config or load_config()
    twilio_cfg = config.get("twilio", {})

    account_sid = twilio_cfg.get("account_sid")
    auth_token = twilio_cfg.get("auth_token")
    from_number = twilio_cfg.get("from_number")

    if not account_sid or not auth_token or not from_number:
        print("❌ Missing Twilio credentials in configuration.")
        return None

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
    send_sms_alert("+19876543210", "Hello! This is your monitoring alert.")
