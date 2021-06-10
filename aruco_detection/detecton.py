#This code can be used with python3 and cv2
#to identify custom Aruco codes in connection with part 1
#It will not run in colab but is shorter and easy to understand
import numpy as np
import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)


aruco_dict = aruco.custom_dictionary(0, 4, 1)
#add empty bytesList array to fill with 4 markers later, (first 4 next line)
aruco_dict.bytesList = np.empty(shape = (4, 2, 4), dtype = np.uint8)

#add new marker(s)
#each 1 per row represents a white pixel
#new symbols and letters can be painted this way
mybits = np.array([[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[0] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,0],[1,0,0,1],[1,1,1,0],[1,0,0,0],], dtype = np.uint8)
aruco_dict.bytesList[1] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]], dtype = np.uint8)
aruco_dict.bytesList[2] = aruco.Dictionary_getByteListFromBits(mybits)
mybits = np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[0,1,1,1]], dtype = np.uint8)
aruco_dict.bytesList[3] = aruco.Dictionary_getByteListFromBits(mybits)
#This code can be used with python3 and cv2
#to identify custom Aruco codes in connection with part 1
#It will not run in colab but is shorter and easy to understand

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