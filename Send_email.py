"""Send Email with Python"""
import smtplib  # For sending emails using SMTP
import ssl  # For creating a secure connection
import os  # For working with environment variables
from email.mime.multipart import MIMEMultipart  # For creating a multipart message
from email.mime.text import MIMEText  # For adding plain text to the email
from dotenv import load_dotenv  # For loading environment variables from a .env file

load_dotenv()  # Load environment variables from .env

SMTP_SERVER = "smtp.gmail.com"  # Gmail SMTP server
SMTP_PORT = 587  # TLS port for Gmail
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Sender's email address from environment variable
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Sender's email password from environment variable

def send_email(recipient_email, subject, body):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the plain text body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the Gmail SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email message

        print("Email sent successfully!")  # Success message

    except Exception as e:
        print(f"Failed to send email: {e}")  # Error handling

if __name__ == "__main__":
    recipient_email = "example@gmail.com"  # Replace with the recipient's email you can also use a list of emails
    subject = "Test Email"  # Email subject
    body = "This is a test email sent from Python."  # Email body text

    send_email(recipient_email, subject, body)  # Call the function to send the email
