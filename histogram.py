# import the necessary packages
# https://stackoverflow.com/questions/38636520/histogram-of-my-cam-in-real-time
# python 3 behaves differently then python2: "/" results in floats, "//" in ints!!
# https://stackoverflow.com/questions/1282945/python-integer-division-yields-float

import cv2
import numpy as np

# Create window to display image
cv2.namedWindow('colorhist', cv2.WINDOW_AUTOSIZE)

# Set hist parameters
hist_height = 64
hist_width = 256
nbins = 32
bin_width = hist_width/nbins

camera_id = 0 # type fo webcam [0 built-in | 1 external]
cameraWidth = 320
cameraHeight = 240

if camera_id == 0:
   cameraId = "PC webcam"
elif camera_id == 1:
   cameraId = "External webcam"

camera = cv2.VideoCapture(camera_id)

# set camera image to 320 x 240 pixels
camera.set(3,cameraWidth)
camera.set(4,cameraHeight)

cameraInfo = "Image size (%d,%d)" % (camera.get(3),camera.get(4))

# initialize mask matrix
mask = np.zeros((cameraHeight,cameraWidth),  np.uint8)
cameraWidth = int(cameraWidth)
cameraHeight = int(cameraHeight)
# print(cameraWidth/2)
# print(cameraHeight/2)
# print(int(cameraHeight/2))
# draw a circle in mask matrix
cv2.circle(mask,(int(cameraWidth/2),int(cameraHeight/2)), 50, 255, -1)

# Create an empty image for the histogram
h = np.zeros((hist_height,hist_width))

# Create array for the bins
bins = np.arange(nbins,dtype=np.int32).reshape(nbins,1)

while True:
   # grab the current frame 
   (grabbed, frame) = camera.read()

   if not grabbed:
      "Camera could not be started."
      break

   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # Calculate and normalise the histogram
   hist_hue = cv2.calcHist([hsv],[0],mask,[nbins],[0,256])
   cv2.normalize(hist_hue,hist_hue,hist_height,cv2.NORM_MINMAX)
   hist=np.int32(np.around(hist_hue))
   pts = np.column_stack((bins,hist))

   # Loop through each bin and plot the rectangle in white
   for x,y in enumerate(hist):
      cv2.rectangle(h,(int(x*bin_width),y),(int(x*bin_width) + int(bin_width-1),hist_height),(255),-1)

   # Flip upside down
   h=np.flipud(h)

   # Show the histogram
   cv2.imshow('Color Histogram',h)
   h = np.zeros((hist_height,hist_width))

   frame = cv2.bitwise_and(frame,frame,mask = mask)
   cv2.putText(frame, cameraInfo, (10, 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

   cv2.imshow(cameraId, frame)            
   key = cv2.waitKey(1) & 0xFF

   # if the `q` key is pressed, break from the loop
   if key == ord("q"):
      break

camera.release()
cv2.destroyAllWindows()