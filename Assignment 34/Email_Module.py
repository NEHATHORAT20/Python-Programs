import smtplib
import logging
import os
from email.message import EmailMessage

def SendEmail(log_file, zip_file):

    sender = "nehajthorat.sits.it@gmail.com"
    receiver = "nehaathorat12345@gmail.com"
    password = "hrjn whwo gbuu fkld"

    msg = EmailMessage()
    msg["Subject"] = "Backup Completed"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Backup completed successfully.")

    with open(log_file, "r") as fobj:
        msg.add_attachment( fobj.read(), subtype="plain", filename=os.path.basename(log_file))

    with open(zip_file, "rb") as zobj:
        msg.add_attachment(zobj.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(zip_file))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

    except Exception as eobj:
        logging.error("Email error: %s", eobj)