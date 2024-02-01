import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mailConnection(subject, message):
    # Email configuration
    sender_email = 'ayyana2@gmail.com'
    sender_password = 'ifrsmagwqpjdc'
    receiver_emails = ['gulraiz0777770@gmail.com','noumanjilani@gmail.com']  
    
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)  # Join the list of recipients into a comma-separated string
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start a secure TLS connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())

    print('Email sent successfully!')