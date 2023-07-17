from djitellopy import tello
import cv2
import keyboard
import time

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
i = 1
while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (720, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if keyboard.is_pressed("a"):
        print("You pressed 'a'.")
        cv2.imwrite("picture"+str(i)+".png", img)
        time.sleep(2)
        i = i+1
