#This code can be used with python3 and cv2
#to identify custom Aruco codes in connection with part 1
#It will not run in colab but is shorter and easy to understand
import numpy as np
import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #lists of ids and the corners belonging to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict)
    # draw markers on frame
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    
    # resize frame to show even on bigger screens
    frame = cv2.resize(frame, None, fx = 3, fy = 3)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()