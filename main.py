import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
import threading
import netifaces as ni
from gpiozero import Button

# retrieves the ip address of the network on which Raspi is connected
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
video_camera = VideoCamera(flip=True)

app = Flask(__name__)

# this function is run in a thread parallel to the video feed
def button_press():
	# getting the button imput from GPIO pin 2 of Raspi
	button = Button(2)

	while True:
		if button.is_pressed:
			print("Button is pressed")
			# getting the frame from the video_camera at the instant the button is pressed
			frame = video_camera.get_frame()

			# send an email with the attachment as the image
			sendEmail(frame)
			print ("done!")

@app.route('/')
def index():
    return render_template('index.html')

# this function is called only when a request to view the video feed is made
def gen(camera):
   while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	# making the function button_press a part of another thread and starting it in parallel to the orignal function
    t = threading.Thread(target=button_press, args=())
    t.daemon = True
    t.start()

	# running the videofeed
    app.run(host=str(ip), debug=False)
