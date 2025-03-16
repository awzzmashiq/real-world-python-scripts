import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email credentials (Use environment variables for security)
EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # Set in system environment
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Set in system environment

# Email content
msg = EmailMessage()
msg['Subject'] = 'Automated Email from Python'
msg['From'] = ''
msg['To'] = ''  # Replace with actual recipient
msg.set_content('Hello, this is an automated email sent using Python!')

# Attach a file (Optional)
file_path = 'Sample.txt'  # Replace with your file path
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(file_path))

# Connect to SMTP server and send email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Use the appropriate SMTP server
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
