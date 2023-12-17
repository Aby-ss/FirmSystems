import smtplib
import json

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Email configuration
smtp_server = 'your_smtp_server'
smtp_port = 587  # Use appropriate port
sender_email = 'raoabdulhadi952@gmail.com'
password = 'hadi@notion2'

# Connect to SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

# Iterate through clients and send emails
for client in data['clients']:
    for template in data['templates']:
        # Replace placeholders in the email template
        email_body = template['body'].replace('{{ClientName}}', client['name'])        
        # Construct email
        message = f"Subject: {template['subject']}\\n\\n{email_body}"

        # Send email
        server.sendmail(sender_email, client['email'], message)

# Quit SMTP server
server.quit()
