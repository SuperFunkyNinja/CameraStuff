import picamera
from time import sleep
import pantilthat
import threading

def record_video():
    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.start_recording('my_video.h264')
    camera.wait_recording(5)
    camera.stop_recording()

def pan_tilt():
    sleep(1)
    pantilthat.pan(-10)
    sleep(1)
    pantilthat.tilt(-10)
    sleep(1)
    pantilthat.pan(10)
    sleep(1)
    pantilthat.tilt(10)
    sleep(1)

camera_thread = threading.Thread(target=record_video)
pan_thread = threading.Thread(target=pan_tilt)

camera_thread.start()
pan_thread.start()