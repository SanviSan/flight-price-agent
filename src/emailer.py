import smtplib
import os
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()


def send_email(body):
    print( "SMTP_USER: ",os.getenv("SMTP_USER"))
    print( "SMTP_PASS: ",os.getenv("SMTP_PASS"))
    print( "SMTP_HOST: ",os.getenv("SMTP_HOST"))
    print( "SMTP_PORT: ",os.getenv("SMTP_PORT"))
    msg = EmailMessage()
    msg["Subject"] = " Cheapest London_banaglore Flight [July - Aug 2026]"
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = os.getenv("TO_EMAIL")
    msg.set_content(body)

    with smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.send_message(msg)