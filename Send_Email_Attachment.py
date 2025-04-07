"""Send Email with Python (with Attachment support)"""
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, subject, body, attachment_path=None):
    try:
        context = ssl.create_default_context()

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # If there's an attachment, add it
        if attachment_path:
            filename = os.path.basename(attachment_path)  # Get the filename

            with open(attachment_path, 'rb') as attachment: # Open the file in binary mode
                part = MIMEBase('application', 'octet-stream') # Create a MIMEBase object
                part.set_payload(attachment.read()) # Read the file content
            
            # Encode the file in base64
            encoders.encode_base64(part)  # Encode to base64
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}',
            ) # Add header for the attachment
            msg.attach(part) # Attach the file to the email

        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    recipient_email = "example@gmail.com"  # Replace with the recipient's email
    subject = "Test Email with Attachment"
    body = "This is a test email sent from Python with an attachment."

    # Provide the path to your attachment file (PDF, image, etc.)
    attachment_path = "./attachment.txt"  # path to your attachment file Example: "documents/report.pdf"
    
    # Ensure the file exists before sending
    if not os.path.isfile(attachment_path):
        print(f"Attachment file {attachment_path} does not exist.")
    else:
        # Call the function to send the email with attachment
        send_email(recipient_email, subject, body, attachment_path)
