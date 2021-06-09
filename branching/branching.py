# from https://answers.opencv.org/question/179532/find-branching-points-in-traces-of-glowing-particles/

import cv2
import numpy

# frame = cv2.imread('sparks.png')
frame = cv2.imread('het-cam-test-cropped-invert.jpg')


if frame is None:
    print('Error loading image')
    exit()

colour_frame = frame

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

rows = frame.shape[0]
cols = frame.shape[1]

branch_locations = []

# start with second column
for i in range(1, cols):
    lit = False
    begin_black_regions = []
    end_black_regions = []

    # start with first row
    if 255 == frame[0, i]:
        lit = True
    else:
        lit = False
        begin_black_regions.append(0)

    # start with second row
    for j in range(1, rows - 1):
        if 255 == frame[j, i] and lit == False:
            lit = True
            end_black_regions.append(j - 1)
        elif 0 == frame[j, i] and lit == True:
            lit = False
            begin_black_regions.append(j)

    # end with last row
    if 0 == frame[rows - 1, i] and lit == False:
        end_black_regions.append(rows - 1)
    elif 0 == frame[rows - 1, i] and lit == True:
        begin_black_regions.append(rows - 1)
        end_black_regions.append(rows - 1)
    elif 255 == frame[rows - 1, i] and lit == False:
        end_black_regions.append(rows - 2)

    for k in range(0, len(begin_black_regions)):
        found_branch = True

        for l in range(begin_black_regions[k], end_black_regions[k] + 1):
            if 0 == frame[l, i - 1]:
                found_branch = False
                break

        if found_branch == True:
            branch_locations.append(complex(i - 1, begin_black_regions[k]))

for i in range(0, len(branch_locations)):
    cv2.circle(colour_frame, (int(branch_locations[i].real), int(branch_locations[i].imag)), 2, (255, 127, 0), 2)

cv2.imshow("Frame", colour_frame)

cv2.waitKey(0)