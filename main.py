# importing the various python control libraries
from gpiozero import Button
from time import sleep
import os

button = Button(2)

# an infinite loop to monitor the button press
while True:
	if button.is_pressed:
		os.system('bash /home/pi/Desktop/procedure.sh')
