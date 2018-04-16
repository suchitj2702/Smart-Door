# importing the required libraries
import cv2
import sys
from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import netifaces as ni

# extacting the ip address for streaming
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

# routine to run the live stream on the ip address
video_camera = VideoCamera(flip=True)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(host=str(ip), debug=False)
