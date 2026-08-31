import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

def send_summary_email(
        successful,
        failed,
        valid_records,
        invalid_records
):
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("EMAIL_APP_PASSWORD")

    if not sender_email or not receiver_email or not password:
        logger.error("Email Configuration is missing")
        return False

    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "University Faculty Scraper Summary"

    body = f"""
    University Faculty Scraper Completed.
    
    Successful Universities: {successful}
    Failed Universities: {failed}
    Valid lecturer records: {valid_records}
    Invalid lecturer records: {invalid_records}
    
    """
    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
        return True

if __name__ == "__main__":
    result = send_summary_email(
        successful=3,
        failed=1,
        valid_records=25,
        invalid_records=2
    )

    print(result)