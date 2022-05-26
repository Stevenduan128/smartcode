import cv2
cap = cv2.VideoCapture(0)
while True:
    res,frame = cap.read()
    cv2.imshow('me',frame)
    k = cv2.waitKey(20)
    if(k==ord('q')):
        cv2.destroyAllwindows()
