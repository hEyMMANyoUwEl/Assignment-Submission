#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    flag,frame=cap.read()
    zeros=np.zeros((frame.shape[0],frame.shape[1]), np.uint8)
    b,g,r=cv2.split(frame)
    blue=cv2.merge([b,zeros,zeros])
    green=cv2.merge([zeros,g,zeros])
    red=cv2.merge([zeros,zeros,r])
    if flag:
        cv2.imshow("RED_FRAME",red)
        cv2.imshow("Green_Frame",green)
        cv2.imshow("Blue_Frame",blue)
        k=cv2.waitKey(1)
        if k == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

