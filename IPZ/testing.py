import cv2
import mediapipe as mp
import time
import Modules.HandTrackingModule as htm

def main():
    pTime = 0

    cap = cv2.VideoCapture(0)
    detector = htm.handDetector(maxHands=1)

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        overlay = img.copy()
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[8])

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        x, y, w, h = 90, 100, 50, 50
        cv2.rectangle(img, (90, 100), (x+w, y+h), (0,0,0), -1)
        alpha = 0.7
        img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
        cv2.putText(img, 'q', (100,140), cv2.FONT_HERSHEY_PLAIN, 3 ,(255,255,255), 2)
        try:
            if lmList[8][1] > 90 and lmList[8][1] < 140 and lmList[8][2] > 100 and lmList[8][2] < 150:
                cv2.putText(img, 'q', (300,140), cv2.FONT_HERSHEY_PLAIN, 3 ,(255,255,255), 2)
        except:
            pass
        cv2.putText(img, str(int(fps)),(0,15), cv2.FONT_HERSHEY_PLAIN, 1 ,(255,0,255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()