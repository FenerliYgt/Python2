import cv2 as cv 
import mediapipe as mp 
import time 

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    finger_count = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 4 and lm.y<handLms.landmark[2].y:
                    finger_count +=1
                    cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 8 and lm.y<handLms.landmark[6].y:
                    finger_count +=1
                    cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)

    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 12 and lm.y<handLms.landmark[10].y:
                    finger_count +=1
                    cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 16 and lm.y<handLms.landmark[14].y:
                    finger_count +=1
                    cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)



    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 20 and lm.y<handLms.landmark[18].y:
                    finger_count +=1
                    cv.circle(img, (cx,cy), 10, (255,0,255), cv.FILLED)


        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cv.putText(img, f'Fingers: {finger_count}', (100,100), cv.FONT_HERSHEY_PLAIN, 5, (0,255,255),10)


    cTime = time.time()
    fps = 1/(cTime-pTime) if cTime-pTime >0 else 0
    pTime = cTime

    cv.putText(img,f'FPS: {int(fps)}', (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)

    cv.imshow('Hand Tracking',img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()


    

    