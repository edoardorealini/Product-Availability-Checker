import requests
import os
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

iPadPro = "https://www.unieuro.it/online/iPad/iPad-Pro-pidAPLMQDY2TYA"
testProductDisponibile = "https://www.unieuro.it/online/iPad/iPad-Pro-pidAPLMPF12TYA"


def checkAvailability(url):
	response = requests.get(url)
	html = response.text
	lines = html.splitlines()

	availability = True

	for i in range(4300, 4400):
		if lines[i].find("Non Disponibile") != -1:
			availability = False

	if availability == True:
		print("iPad Disponibile")
		os.system("xdg-open " + url)
		for i in range(0,3):
			os.system("beep -f 555 -l 200")

		fromaddr = "your gmail address"
		toaddr = "here insert destination address, can be the same as fromaddr"
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
		server.login("your gmail address here", "your password")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)

		return True

	else:
		print("iPad NON Disponibile")
		return False

while True:
	print (time.asctime( time.localtime(time.time())))
	if checkAvailability(iPadPro) == True:
		break;
	time.sleep(5)