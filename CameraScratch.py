import picamera
from time import sleep
# import math
import pantilthat

camera = picamera.PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
sleep(1)
pantilthat.pan(-10)
sleep(1)
pantilthat.tilt(-10)
sleep(1)
pantilthat.pan(10)
sleep(1)
pantilthat.tilt(10)
sleep(1)
camera.wait_recording(5)
camera.stop_recording()

