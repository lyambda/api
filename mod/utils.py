from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import smtplib
import json
import os

def emailt(email, code, smtp):
    env = Environment(loader=FileSystemLoader('%s/html/' % os.path.dirname(__file__)))
    template = env.get_template('new.html')
    output = template.render(data={'code' : code, 'mail' : email})

    message = MIMEMultipart()

    message['From'] = smtp['email']
    message['To'] = email
    message['Subject'] = "Lamda"

    message.attach(MIMEText(output, 'html'))

    server = smtplib.SMTP(f'{smtp["host"]}: {smtp["port"]}')
    server.starttls()
    server.login(smtp['email'], smtp['password'])
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()