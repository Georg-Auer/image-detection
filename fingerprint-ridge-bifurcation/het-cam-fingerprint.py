import fingerprint_feature_extractor
import cv2
import numpy as np
# read the input image -->
# You can enhance the fingerprint image using the "fingerprint_enhancer" library
# img = cv2.imread('vasc-part-invert.jpg', 0) #this works!!!
img = cv2.imread('color-test-mask-tiny.jpg', 0) 

# img = cv2.imread("het-cam-test-cropped-RGB-invert.jpg", 0)
# img = cv2.imread("het-cam-test-cropped-RGB.jpg", 0)
# img = cv2.imread("het-cam-test-cropped.jpg", 0)

FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, showResult=True)

print(FeaturesTerminations)
print(FeaturesBifurcations)