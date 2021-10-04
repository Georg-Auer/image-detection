import cv2
# https://stackoverflow.com/questions/16746473/opencv-find-bounding-box-of-largest-blob-in-binary-image
# Load image, grayscale, Gaussian blur, and Otsu's threshold
image = cv2.imread('test2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours and sort using contour area
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    # Highlight largest contour
    cv2.drawContours(image, [c], -1, (36,255,12), 3)
    break

cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()