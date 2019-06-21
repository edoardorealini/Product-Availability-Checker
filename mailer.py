import requests
import os
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

url = "https://www.unieuro.it/online/iPad/iPad-Pro-pidAPLMQDY2TYA"
testProductDisponibile = "https://www.unieuro.it/online/iPad/iPad-Pro-pidAPLMPF12TYA"


fromaddr = "iPadAvailabilityChecker@gmail.com"
toaddr = "your gmail address here"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "iPad AVAILABLE"

body = "iPad disponibile all'url " + url
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("your gmail address here", "your passwd")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)