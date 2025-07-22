import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

departments = {
    "marketing": "sheikh.khaleel17@gmail.com",
    "sales": "sheikh.khaleel17@gmail.com"
}

for dept, recipient in departments.items():
    msg = MIMEMultipart()
    msg['Subject'] = f'{dept.capitalize()} Report Screenshot'
    msg['From'] = 'jenkins@example.com'
    msg['To'] = recipient

    html = f"""
    <html>
      <body>
        <p>Hi {dept.capitalize()},</p>
        <p>Here is your latest report:</p>
        <img src="cid:{dept}">
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    with open(f'screenshots/{dept}.png', 'rb') as img:
        image = MIMEImage(img.read())
        image.add_header('Content-ID', f'<{dept}>')
        msg.attach(image)

    with smtplib.SMTP('smtp.example.com') as s:
        s.send_message(msg)
