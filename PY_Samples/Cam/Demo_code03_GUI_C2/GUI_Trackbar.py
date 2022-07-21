#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     16.06.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# BGR Control using Trackbars
import numpy as np
import cv2

# create a black image
img = np.zeros([200,350,3], np.uint8)

cap = cv2.VideoCapture(0)

cv2.namedWindow('BGR')
# define a null callback function for Trackbar
def null(x):
 pass
# create three trackbars for B, G and R
# arguments: trackbar_name, window_name, default_value, max_value, callback_fn
cv2.createTrackbar("B", "BGR", 0, 255, null)
cv2.createTrackbar("G", "BGR", 0, 255, null)
cv2.createTrackbar("R", "BGR", 0, 255, null)


while True:
 # read the Trackbar positions
 b = cv2.getTrackbarPos('B','BGR')
 g = cv2.getTrackbarPos('G','BGR')
 r = cv2.getTrackbarPos('R','BGR')
 # change the image colour to Trackbar positions

 ret, frame = cap.read()
 img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)

## img[:] = [b,g,r]
 # display trackbars and image
 cv2.imshow('BGR', img)
 key = cv2.waitKey(1) & 0xFF


 if key == ord('q'):
     break
cv2.destroyAllWindows()