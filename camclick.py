# importing the required libraries
from picamera import PiCamera
from mail import sendEmail

# process where the photo is actually clicked and sent via email
camera = PiCamera()
camera.rotation =  180
camera.resolution = (640, 480)
camera.capture('/home/pi/Downloads/Smart-Security-Camera-master/pics/img.jpg')
img = '/home/pi/Downloads/Smart-Security-Camera-master/pics/img.jpg'
with open( img, 'rb') as fp:
	sendEmail(fp)
