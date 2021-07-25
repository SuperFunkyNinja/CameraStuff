from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
camera.annotate_text = "Hello Marty!"
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()