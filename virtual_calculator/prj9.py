import cv2
from cvzone.HandTrackingModule import HandDetector


class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width,
                                      self.pos[1] + self.height), (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 5)
            return True
        else:
            return False


cap = cv2.VideoCapture(0)  # define a video capture object
cap.set(3, 1280)  # height
cap.set(4, 720)  # width
detector = HandDetector(maxHands=1)
myequation = ''
delayCounter = 0
# drawing buttons
# Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))
# loop
while (True):
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    # draw all button
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 100), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 100), (50, 50, 50), 3)
    # draw a button
    for button in buttonList:
        button.draw(img)
    if hands:
        lmlist = hands[0]["lmList"]  # List of 21 Landmark points
        # print(lmList)
        length, info, img = detector.findDistance(lmlist[8][0:2], lmlist[12][0:2], img)
        print(length)
        x, y = lmlist[8][0:2]
        if length < 50:
           for i, button in enumerate(buttonList):
               if button.checkClick(x, y):
                        myvalue = buttonListValues[int(i % 4)][int(i / 4)]
                        if myvalue == '=':
                            myequation = str(eval(myequation))
                        else:
                            myequation += myvalue
                        delayCounter = 1
    # avoid duplicates
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0
    # display the result
    cv2.putText(img, myequation, (810, 130), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)
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

