from email.message import EmailMessage
import ssl
import smtplib

from rich.traceback import install
install(show_locals=True)

email_sender = "raoabdulhadi952@gmail.com"
email_password = "--"

email_reciever = "fenaroj221@bayxs.com"

subject = "Email Outreach Client Testing"
body = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 443, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())