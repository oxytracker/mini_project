import pandas as pd
import numpy as np
import smtplib
from SQLquerying import check_anamoly


def send_msg():
    #Connecting the smtp connection to gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        #Getting the anamoly values
        df=check_anamoly()
        #Writing the email for sudden check
        subject='SpO2 and Heartbeat rate needs to be checked manually'
        body='As noted by the Oxymeter sensor, there is a fall below recommended levels, please check the patient'
        smtp.login("oxytracker@gmail.com", "miniproject2021")
        msg=f'Subject: {subject}\n\n{body}'
        #Sending the email from sender, to reciever, message
        smtp.sendmail("oxytracker@gmail.com", "gurujeetshetty@gmail.com", msg)
        return