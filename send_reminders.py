import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acumen_site.settings")

application = get_wsgi_application()

#from acuthon.models import *

message = """
Hello {0},
Thanks for getting registered for Acuthon - Edition I.
We're excited to see you as part of Acuthon this Saturday, 9th of March, 2019.

This is a gentle reminder to complete your registration by completing the payment in our website.

Website link: https://www.acumenit.in/acuthon
"""

#participants = Participant.object.fileter(payment=None)
class User:
    def __init__(self):
        self.first_name = 'Krushi Raj'
        self.email = 'krushiraj123@gmail.com'
    


class Participant:
    def __init__(self):
        self.user = User()

participants = [Participant()]

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("acumen.it.vce@gmail.com", 
            "acumenIT@2K19"
        )

msg = MIMEMultipart()

msg['From'] = "Acuthon <acumen.it.vce+acuthon@gmail.com>"
msg['Subject'] = 'Acuthon - Gentle reminder to complete your registration'

for participant in participants: 

    msg['To'] = participant.user.email
    text = message.format(participant.user.first_name)
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    server.sendmail(
        "Acuthon <acumen.it.vce+acuthon@gmail.com>", 
        participant.user.email, 
        msg.as_string()
    )
    # val = send_mail(
    #         'Gentle reminder to complete your registration for Acuthon',
    #         None,
    #         'acuthon@acumenit.in',
    #         recipient_list=[participant.user.email],
    #         fail_silently=False,
    #         auth_user='acuthon@acumenit.in',
    #         auth_password='acumenIT@2K19',
    #         connection=None,
    #         html_message=message.format(participant.user.first_name)
    # )

    # print("Returned by send_mail" + str(val))

server.quit()
