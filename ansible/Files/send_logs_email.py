import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Configuration
sender = "jenkins@example.com"
receiver = "khaleeldk11@mail.com"
subject = "WebLogic Log Files"
smtp_server = "smtp.example.com"  # Change this
smtp_port = 25  # Or 587 if using TLS

log_files = [
    ("/home/weblogic/admin.log", "admin.log"),
    ("/home/weblogic/nodemanager.log", "nodemanager.log"),
]

# Compose email
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEBase('application', 'octet-stream'))

# Attach log files
for path, filename in log_files:
    with open(path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)

# Send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.send_message(msg)
