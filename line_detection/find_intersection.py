#https://stackoverflow.com/questions/46565975/find-intersection-point-of-two-lines-drawn-using-houghlines-opencv

import cv2
import numpy as np
from collections import defaultdict
import os
#os.chdir(r'C:\Users\Georg\Documents\Python Scripts\exercises')

def find_lines(filename):
    print("finding lines.. ")
    img_big = cv2.imread(filename)
    # x1 = 500
    # y1 = 340
    # x2 = 780
    # y2 = 620
    # img = img_big[y1:y2, x1:x2]
    # cv2.imwrite(filename + "_cropped.jpg", img=img)

    # changed from img to img_big, to analyze the raster where there is only one crossing
    gray = cv2.cvtColor(img_big, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    adapt_type = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    thresh_type = cv2.THRESH_BINARY_INV

    edges = cv2.Canny(blur, 60, 150, apertureSize=3)

    bin_img = cv2.adaptiveThreshold(edges, 255, adapt_type, thresh_type, 11, 2)

    #tresh is maybe the lenght?
    #should fit to pixel size
    # old script used rho, theta, thresh = 2, np.pi/180, 400
    rho, theta, thresh = 2, np.pi/180, 200
    lines = cv2.HoughLines(bin_img, rho, theta, thresh)
    try:
        print(f"there where {len(lines)} lines found")
    except:
        print("no lines found")
    
    return lines


def segment_by_angle_kmeans(lines, k=2, **kwargs):
    """Groups lines based on angle with k-means.
    Uses k-means on the coordinates of the angle on the unit circle 
    to segment `k` angles inside `lines`.
    """

    # Define criteria = (type, max_iter, epsilon)
    default_criteria_type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    criteria = kwargs.get('criteria', (default_criteria_type, 10, 1.0))
    flags = kwargs.get('flags', cv2.KMEANS_RANDOM_CENTERS)
    attempts = kwargs.get('attempts', 10)

    # returns angles in [0, pi] in radians
    angles = np.array([line[0][1] for line in lines])
    # multiply the angles by two and find coordinates of that angle
    pts = np.array([[np.cos(2*angle), np.sin(2*angle)]
                    for angle in angles], dtype=np.float32)

    # run kmeans on the coords
    labels, centers = cv2.kmeans(pts, k, None, criteria, attempts, flags)[1:]
    labels = labels.reshape(-1)  # transpose to row vec

    # segment lines based on their kmeans label
    segmented = defaultdict(list)
    for i, line in zip(range(len(lines)), lines):
        segmented[labels[i]].append(line)
    segmented = list(segmented.values())
    return segmented


def intersection(line1, line2):
    """Finds the intersection of two lines given in Hesse normal form.
    Returns closest integer pixel locations.
    See https://stackoverflow.com/a/383527/5087436
    """
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return [[x0, y0]]


def segmented_intersections(lines):
    """Finds the intersections between groups of lines."""

    intersections = []
    for i, group in enumerate(lines[:-1]):
        for next_group in lines[i+1:]:
            for line1 in group:
                for line2 in next_group:
                    intersections.append(intersection(line1, line2)) 

    return intersections

# use the created function to find calibration points (x,y) for a single image
def find_intersection_point(filename):
    #find the lines in a cropped part of the picture
    lines = find_lines(filename)

    # Seperation of lines into horizontal and vertical
    # What's nice is here we can specify an arbitrary number of groups
    # by specifying the optional argument k (by default, k = 2 - therefore not specified here).
    segmented = segment_by_angle_kmeans(lines)

    intersections = segmented_intersections(segmented)
    print("Intersections found at:")
    print(intersections)

    coordinates_mean = np.array(np.mean(intersections, axis=0))
    return coordinates_mean, lines, intersections;

# Only relevant if run as __main__
if __name__ == '__main__':
    print("This module can find intersection points on pictures.")
    print(f"Current directory is {os.getcwd()}")

    #this is just for getting picturenames from one folder
    from os import listdir
    from os.path import isfile, join        
    #mypath = r'C:\SPOC\DOC\Calibration\images\set'
    #mypath = r'C:\\Users\\Georg\\Documents\\Python Scripts\\delta_bot\\calibration\\cal'
    mypath = (os.path.join(os.getcwd(), "detection/line_detection/2,5plan"))
    #C:\Users\Georg\Documents\Python Scripts\delta_bot\dustbin
    os.chdir(mypath)
    # get names of pictures in a folder
    print(f"Searching files in directory {os.getcwd()}")
    picturenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    # only use the first image, for testing
    filename = picturenames[4]
    print(f"Analyzing {filename}")
    #filename = "position_2_20201013-134609.jpg"
    mean, lines, intersections = find_intersection_point(filename)
    print(mean)
    print(intersections)
    print(lines)
    #cv_image = np.array((lines.getRows(), lines.getCols()) )
    #filename = "find_intersections"
    #cv2.imwrite(filename, img=cv_image)

    #cv.view =

else:
    print("Intersection finding module loaded:")

