import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_template(file_name):
    """Reads the message template from a JSON file."""
    with open(file_name, 'r') as file:
        template = json.load(file)
    return template

def send_email(subject, message, sender_email, receiver_email, password):
    """Sends the email using SMTP."""
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    # File name containing the message template
    template_file = 'message_templates.json'

    # Read the message template from the file
    message_templates = read_template(template_file)

    # Extract details from a specific template
    selected_template = "template_1"
    template = message_templates['outreach_messages'][selected_template]

    # Extract relevant details from the template
    description = template['description']
    subject = template['subject']
    product_name = template['product_name']
    company_name = template['company_name']
    client_name = template['client_name']

    # Construct the email message
    message = f"Dear {client_name},\n\n{description}\n\nAt {company_name}, we are excited to introduce our latest product, {product_name}. This innovative solution is designed to...\n\nWarm regards,\nYour Name"

    # Email credentials
    sender_email = 'your_email@gmail.com'  # Replace with your email
    password = 'your_password'  # Replace with your password
    receiver_email = 'client_email@example.com'  # Replace with the client's email

    # Send the email
    send_email(subject, message, sender_email, receiver_email, password)

