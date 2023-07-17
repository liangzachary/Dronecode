import cv2
from djitellopy import Tello
from datetime import datetime

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

now = datetime.now()
str()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

cv2.imwrite("picture"+"-"+dt_string+".png", frame_read.frame)

tello.land()
