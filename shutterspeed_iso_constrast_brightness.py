from time import sleep, time
from picamera import PiCamera
from datetime import datetime

def capture_photo(camera, shutter_speed, iso, contrast, brightness):
        camera.resolution = (1662, 1232)
        camera.rotation = -90
	camera.framerate = 30
	camera.shutter_speed = shutter_speed
        camera.iso = iso
	camera.contrast = contrast
	camera.brightness = brightness
	exposure_mode = 'sports'
	camera.exposure_mode = exposure_mode
        sleep(2)
        filename = 'img_'+ str(shutter_speed) + '_'+ str(iso) + '_'+ str(exposure_mode) \
+ '_'+ str(contrast) + '_'+ str(brightness) \
+ '_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.jpg'      
        camera.capture(filename)
        print("Foto Capturada: " + filename)
        #camera.close() 

camera = PiCamera()

while True:
        shutter_speed = int(input("Enter shutter speed: "))
        iso = int(input("Enter iso: "))
	contrast = int(input("Enter contrast level: "))
	brightness = int(input("Enter brightness: "))
        capture_photo(camera, shutter_speed, iso, contrast, brightness)
