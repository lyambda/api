# ************** Standart module *********************
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import smtplib
import os
# ************** Standart module end *****************

# ************** Read "config.ini" ********************
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
mail = config["EMAIL"]
# ************** END **********************************

# ето магия, не трогай, сламаешь!!!
def email(email, code, smtp):
    env = Environment(loader=FileSystemLoader('%s/html/' % os.path.dirname(__file__)))
    template = env.get_template('new.html')
    output = template.render(data={'code' : code, 'mail' : email})

    message = MIMEMultipart()

    message['From'] = mail['mail']
    message['To'] = email
    message['Subject'] = "Lamda"

    message.attach(MIMEText(output, 'html'))

    server = smtplib.SMTP(f'{mail["host"]}: {mail["port"]}')
    server.starttls()
    server.login(mail['mail'], mail['password'])
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()