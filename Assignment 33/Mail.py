import smtplib
import os
from email.message import EmailMessage

def SendEmail(sender, app_password, receiver, subject, body, filename):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(filename, "rb") as fobj:
        msg.add_attachment(fobj.read(), maintype="application", subtype="octet-stream", filename = os.path.basename(filename))

    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        smtp.quit()
        print("Mail sent successfully")

    except Exception as e:
        print("Email Sending Error:", e)