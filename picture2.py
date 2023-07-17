from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())


def TakePhoto(me):
    me.streamoff()
    me.streamon()
    img = me.get_frame_read().frame
    # print(img)
    img = cv2.resize(img, (360, 240)) # optional
    cv2.imshow("photo", img)  # optional display photo
    cv2.waitKey(0)

# # example condition, it can also just be called normally like "TakePhoto"

"""
if (1 + 1) == 2:
    TakePhoto(me)
"""

# # another example, with an actual used if statement

"""
bat = me.get_battery()

if bat < 50:
    TakePhoto(me)
else:
    print("battery too low (for ex)")
"""

# # for now, we'll call it just like this for testing:

TakePhoto(me)

# </>