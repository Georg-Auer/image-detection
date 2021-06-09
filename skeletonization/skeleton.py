import cv2
import numpy as np

# alternatively, use thinning()
# https://docs.opencv.org/4.4.0/df/d2d/group__ximgproc.html#ga37002c6ca80c978edb6ead5d6b39740c
# dst = cv.ximgproc.thinning(src[,dst[,thinningType]])

img = cv2.imread('het-cam-test-cropped-RGB-invert.jpg',0)
original = cv2.imread('het-cam-test-cropped-RGB-invert.jpg',0)

size = np.size(img)
skel = np.zeros(img.shape,np.uint8)

ret,img = cv2.threshold(img,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False

while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True

winname2 = "Original"
cv2.namedWindow(winname2)        # Create a named window
cv2.moveWindow("Original", 40,50)  # Move it to (40,30)
cv2.imshow(winname2, original)

winname = "skeleton"
cv2.namedWindow(winname)        # Create a named window
cv2.moveWindow("skeleton", 40,200)  # Move it to (40,30)
cv2.imshow(winname, skel)

#cv2.imshow("skel",skel)
# cv2.imshow("original",original)

cv2.waitKey(0)
cv2.destroyAllWindows()