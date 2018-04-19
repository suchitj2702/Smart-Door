# importing the required libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import netifaces as ni

# giving the sending email credentials
fromEmail = 'smartdoor.snu2@gmail.com'
fromEmailPassword = 'Test@123'
import smtplib

# dynamically extracting the ip address raspi is connected to
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

# email to which the mail is sent
toEmail = 'sj535@snu.edu.in'

# function to actually send the email after proper structuring
def sendEmail(img):
	# forming the structure of the mail
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Smart Door Notification'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Smart Door Update'
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart Door detected the following outside your door:\nPress the following link to view the live feed\n'+str(ip)+':5000')
	msgAlternative.attach(msgText)

	# attaching the image
	msgImage = MIMEImage(img)
	msgRoot.attach(msgImage)

	# calling the smtp routine by google for sending the mail
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()
