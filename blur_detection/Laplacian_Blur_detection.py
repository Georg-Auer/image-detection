# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:53:07 2019

@author: Georg
"""

import cv2
 
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
    
image = cv2.imread('picture2.jpg') #,0 to load pic in gray, if neccessary

#print('Original Dimensions : ',image.shape)
#scale_percent = 10 # percent of original size
#width = int(image.shape[1] * scale_percent / 100)
#height = int(image.shape[0] * scale_percent / 100) 
#dim = (width, height)
# resize image
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#print('Resized Dimensions : ',resized.shape) 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
print(fm)

