from bottle import route, run, template, request
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

def open():
    print("Let's turn it on")
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    time.sleep(0.5)
    GPIO.setup(7, GPIO.IN)

# Handler for the home page
@route('/')

def index():
	clicked = request.GET.get('clicked')
	print(clicked)
	if(clicked == 'true'):
		open()
	return template('/home/pi/pi_magazine/11_mi_light/home.tpl')
# Start the webserver running on port 80
run(host="192.168.0.23", port=80)
