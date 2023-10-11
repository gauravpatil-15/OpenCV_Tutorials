import cv2
import numpy as np
import math

flag = False
ix = -1
iy = -1

def draw (event, x, y, flags, params):
  # print(event)
  global flag, ix, iy

  if event == 1:
    flag = True
    ix = x
    iy = y

  elif event == 0:

    if flag == True:
      cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=[0,0,255], thickness=-1)
      # cv2.circle(img, center=(ix,iy),radius=round(math.sqrt( pow((x-ix),2) + pow((y-iy),2) )),color=(255,0,0),thickness=-1)
      
  elif event == 4:
    flag = False
    cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=[0,0,255], thickness=-1)
    # cv2.circle(img, center=(ix,iy),radius=math.sqrt( pow((x-ix),2) + pow((y-iy),2) ),color=(255,0,0),thickness=-1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

img = np.zeros((512,512,3))

while True:

  cv2.imshow("window",img)

  if cv2.waitKey(1) & 0xFF == ord('x'):
    break

cv2.destroyAllWindows()
