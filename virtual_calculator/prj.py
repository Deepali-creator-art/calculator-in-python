import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)# define a video capture object
cap.set(3,1280) #height
cap.set(4,720)  #width
detector=HandDetector(maxHands=1)
while (True):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.rectangle(img, (100, 100), (200, 200), (225, 225, 0), cv2.FILLED)  # RECTANGLE

    cv2.rectangle(img,(100,100),(200,200),(50,50,50),3)
    cv2.putText(img,"9",(100+40,100+60),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)


    cv2.imshow("Image", img)
    # the 'q' button is set as the quitting button you may use any desired button of your choice
    key = cv2.waitKey(1)
    if key != ord('q'):
        continue
    break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
