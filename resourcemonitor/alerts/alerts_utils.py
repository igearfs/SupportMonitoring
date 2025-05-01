from .email_sender import send_email_alert  # Import your email alert method
from .twilio_alert import send_sms_alert  # Import your SMS alert method
from .jira_client import create_jira_issue, issue_exists  # Import Jira methods

def send_alert(message, summary, send_email=False, send_sms=False, config=None):
    """
    Handle the alerting process: Jira ticket creation, Email, and SMS alerts.
    Args:
    - message (str): The message to send in the alerts.
    - summary (str): The summary for the Jira issue.
    - send_email (bool): Flag to send email alerts.
    - send_sms (bool): Flag to send SMS alerts.
    - config (dict, optional): Config data (if not using the default config).
    """

    # Call Jira's create_jira_issue method to create a ticket and check if the issue exists
    ticket_status = True #create_jira_issue(summary=summary, description=message, config=config)

    # If the ticket was created successfully
    if ticket_status:
        print(f"✅ Jira issue created for: {summary}")
    else:
        print(f"⚠️ Duplicate Jira ticket detected for: {summary}")

    # Send email if the flag is set to True and the ticket was successfully created
    if send_email and ticket_status:
        print("✅ Attempting to send email.")
        try:
            send_email_alert(subject="TCP Monitor Alert", body=message)
            print("✅ Email alert sent successfully.")
        except Exception as e:
            print(f"❌ Error sending email alert: {e}")

    # Send SMS if the flag is set to True and the ticket was successfully created
    if send_sms and ticket_status:
        print("✅ Attempting to send SMS.")
        try:
            send_sms_alert(message=message)
            print("✅ SMS alert sent successfully.")
        except Exception as e:
            print(f"❌ Error sending SMS alert: {e}")
