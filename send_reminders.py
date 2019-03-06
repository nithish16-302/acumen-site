import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acumen_site.settings")

application = get_wsgi_application()

from acuthon.models import *

message = """
Hello {0},
Thanks for getting registered for Acuthon - Edition I.
We're excited to see you as part of Acuthon this Saturday, 9th of March, 2019.

This is a gentle reminder to complete your registration by completing the payment in our website.

Website link: https://www.acumenit.in/acuthon
"""

#participants = Participant.object.fileter(payment=None)


participants = Participant.objects.filter(payment=None)

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
    print('sent to {0} at {1}'.format(participant.user.first_name, participant.user.email))

server.quit()
