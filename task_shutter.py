from time import sleep, time
from picamera import PiCamera
from datetime import datetime

NIGHT_TIME_START='18' 
SHUTTER_SPEED_NIGHT=3000

camera = PiCamera()
camera.resolution = (1662, 1232)
camera.rotation = -90
camera.framerate = 30
exposure_mode = 'sports'

if (datetime.now().strftime('%H') == NIGHT_TIME_START):
	camera.shutter_speed = SHUTTER_SPEED_NIGHT

camera.capture('teste.jpg')
