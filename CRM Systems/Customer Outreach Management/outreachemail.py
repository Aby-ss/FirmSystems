import requests
import json
import csv, smtplib, ssl

from rich import text, box
from rich.panel import Panel
from rich.prompt import Prompt

from rich.traceback import install
install(show_locals=True)

subject = prompt.ask("Subject of your Email ")
reciever = prompt.ask("Recipient's name with corresponding prefix (Mr/Mrs) ")

message = """Subject: {subject}

Hi {reciever}, your grade is {grade}"""
from_address = prompt.ask("Your Gmail ")
password = prompt.ask("Type your password ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )



