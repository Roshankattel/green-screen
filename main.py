import cv2 
import numpy as np 

img = np.zeros((1080,1920,3),np.uint8) 
img[:] = (0, 255, 0)
cv2.imwrite("green.jpg", img)
cv2.imshow("Green Image",img)
cv2.waitKey(0)