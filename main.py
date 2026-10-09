import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

sender_email =os.getenv("my_email")
sender_password =os.getenv("email_password")  # 16-character Google App Password
recipient_email =os.getenv("to_address")
# print(sender_email)
# print(sender_password)
# print(recipient_email)
# Read HTML file using relative path safely
BASE_DIR = Path(__file__).resolve().parent
html_file_path = BASE_DIR / "aaa.html"

with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Build MIME message
msg = MIMEMultipart("alternative")
msg["Subject"] = "HTML Email Test"
msg["From"] = sender_email
msg["To"] = recipient_email

msg.attach(MIMEText("Your email client does not support HTML.", "plain", "utf-8"))
msg.attach(MIMEText(html_content, "html", "utf-8"))

# Send email securely via Port 465
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("HTML Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")