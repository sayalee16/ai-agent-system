from email import message_from_string

def process_email(email_text):
        msg = message_from_string(email_text)
        subject = msg.get("Subject", "No Subject")
        sender = msg.get("From", "Unknown Sender")
        body = msg.get_payload()
        return {
            "type": "email",
            "subject": subject,
            "sender": sender,
            "body": body.strip()
        }