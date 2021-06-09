import cv2
import numpy as np
import imutils

img = cv2.imread('het-cam-test.jpg',1)

# # only use the red component, because structure is red
# # https://stackoverflow.com/questions/39903809/wrong-color-reading-an-image-with-opencv-python
# blue,green,red = cv2.split(img)
# img = red

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

r = resized.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 2] = 0
cv2.imshow("red image",r)

cv2.imshow("resized image",resized)

gray = cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 60, 150, apertureSize=3)
#edges = cv2.Canny(gray, 1, 90, apertureSize=3)

#somehow working
edges = cv2.Canny(gray, 19, 25, apertureSize=3)

# img = im.copy()
# lines = cv2.HoughLines(edges,2,np.pi/180,200)

cv2.imshow("grayscale",gray)
cv2.imshow("edge detection",edges)

lines = cv2.bitwise_not(edges)
cv2.imshow("line detection",lines)

# press space bar to close everything
cv2.waitKey(0)
cv2.destroyAllWindows()