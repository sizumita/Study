import cv2
import os
os.remove("capture1.jpg") 
print "go"
c = cv2.VideoCapture(0)
c.read()
r, img = c.read()
cv2.imwrite('capture1.jpg', img)
c.release()
