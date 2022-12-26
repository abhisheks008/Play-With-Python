import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'write-your-email-@gmail.com'
email_password = 'write-password-here'

# List of email addresses
email_receivers = ['example-1@gmail.com', 'example-2@gmail.com']

subject = 'Check out my Project'
body = """
This is demo of automated email sender,
Hope you like this
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = ', '.join(email_receivers)
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receivers, em.as_string())
