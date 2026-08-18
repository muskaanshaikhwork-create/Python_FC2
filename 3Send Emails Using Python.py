# Project 3: Send Emails Using Python

# Problem Statement:
# You want to write a Python program that can send emails to one or multiple
# recipients using an email account.

# Question:
# How can I write a Python program that can send emails to one or multiple
# recipients using an email account?


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email credentials
sender_email = "useremail@gmail.com"
sender_password = ""

# List of recipients
recipients = [
    "recipient1@gmail.com",
    "recipient2@gmail.com"
]

# Email subject and body
subject = "Test Email"
body = "Hello,\n\nThis is a test email sent using Python.\n\nThank you!"

# Create email message
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send email to each recipient
for recipient in recipients:
    message["To"] = recipient
    server.sendmail(sender_email, recipient, message.as_string())
    print(f"Email sent to {recipient}")

# Close the connection
server.quit()
print("All emails sent successfully.")