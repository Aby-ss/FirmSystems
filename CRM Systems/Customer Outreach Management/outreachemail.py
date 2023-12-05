import requests
import json
import csv, smtplib, ssl

from rich import text, box
from rich.panel import Panel
from rich.prompt import Prompt

from rich.traceback import install
install(show_locals=True)

with open('templatemessages.json') as fp:
    messages_Data = json.loads(fp)


subject = prompt.ask("Subject of your Email ")
reciever = prompt.ask("Recipient's name with corresponding prefix (Mr/Mrs) ")

message = "Subject: {Subject}\n\nHello {reciever},\n{templatemessage_json}"
