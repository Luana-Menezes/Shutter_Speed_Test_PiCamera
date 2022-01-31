from time import sleep, time
from picamera import PiCamera
from datetime import datetime

DAY_TIME_START=7
NIGHT_TIME_START=17 
SHUTTER_SPEED_NIGHT=3000

camera = PiCamera()
camera.resolution = (1662, 1232)
camera.rotation = -90
camera.framerate = 30
exposure_mode = 'sports'

hour = int(datetime.now().strftime('%H'))

if (hour >= NIGHT_TIME_START and hour <= DAY_TIME_START):
	camera.shutter_speed = SHUTTER_SPEED_NIGHT
else
	camera.shutter_speed = 0

camera.capture('teste.jpg')
