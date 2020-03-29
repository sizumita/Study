import cv2
c = cv2.VideoCapture(0)
c.read()
r, img = c.read()
cv2.imwrite('capture1.jpg', img)
c.release()
