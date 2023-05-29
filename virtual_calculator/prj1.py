
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8,maxHands=1)
hands, img = detector.findHands(img, flipType=False)   #Hand Detection





