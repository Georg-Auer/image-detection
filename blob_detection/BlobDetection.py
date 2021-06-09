# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:56:40 2019

@author: Georg
"""
#https://www.learnopencv.com/blob-detection-using-opencv-python-c/

#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
#import glob #this is to cycle through folders
import glob, os

def blobdetection(im, i, file):
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds, lower minimum for detection of less contrast
    params.minThreshold = 100
    params.maxThreshold = 200

    # Filter by Area.
    # 6 seems to be the treshold for chemiluminescence blob in ~3000x4000 px jpg
    params.filterByArea = True
    params.minArea = 100

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87
    
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(im)
    #this prints the number of blobs
    nblobs = len(keypoints)
    #print (nblobs)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show blobs
#    cv2.imshow("Keypoints", im_with_keypoints)
#    cv2.waitKey(0)
    print(file.replace('.jpg', ''))
    filename = (f"{nblobs}_blobs_found_in_{file}_analyzed_pic_nr_{i}.jpg")
    cv2.imwrite(filename, img=im_with_keypoints)
    
    return nblobs #return the number of blobs

# for each jpg file with "cells" in the filename, examine the blobs 
i = 0
print(os.getcwd())
working_directory = (os.path.join(os.getcwd(), "delta_microscope/detection/blob_detection/blobs"))
#forward slashes for unix compatibility
print(working_directory)
#os.chdir(r"C:\Users\Georg\Documents\Python Scripts\delta_bot\detection\blob_detection\blobs")
os.chdir(working_directory)
#print (os.getcwd())
#print (os.path.join(os.getcwd(), "", "file.txt"))

# "chemiluminescence_nr2.jpg"
# "*chemi*.jpg"

for file in glob.glob("*chemi*.jpg"):
    print(file)
    #im = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    # take image in 3 color mode
    im = cv2.imread(file, 3)

    # only use the blue component, because chemiluminescence is blue:
    # https://stackoverflow.com/questions/39903809/wrong-color-reading-an-image-with-opencv-python
    blue,green,red = cv2.split(im)
    im = blue

    print (blobdetection(im, i, file)) #print the returned number of blobs
    i += 1
# detect blobs on image