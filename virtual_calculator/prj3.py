import cv2
from cvzone.HandTrackingModule import HandDetector
class Button:
    def __init__(self,pos,width,height,value):
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value

    def draw(self,img):
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width,
                                      self.pos[1] + self.height),(50,50,50),3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

cap = cv2.VideoCapture(0)# define a video capture object
cap.set(3,1280) #height
cap.set(4,720)  #width
detector=HandDetector(maxHands=1)
#drawing buttons
buttonList=[]
for x in range(4):
    xpos=x*100+800
    ypos=100+150
    buttonList.append(Button((xpos,ypos),100,100,'5'))
#loop
while (True):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    #draw a button
    for button in buttonList:
        button.draw(img)
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

