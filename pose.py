import cv2 as cv 
import mediapipe as mp 
import time

mpHands = mp.solutions.hands 
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv.VideoCapture('WIN_20241025_19_49_56_Pro.mp4')
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results1 = hands.process(imgRGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape 
            print(id,lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx, cy), 10, (255,0,0), cv.FILLED)

    if results1.multi_hand_landmarks:
        for handLms in results1.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape 
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx, cy)
                if id ==10: # numbers on the hand
                    cv.circle(img, (cx,cy), 25, (255,0,255), cv.FILLED)

            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)



    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)

    cv.imshow('Image',img)
    cv.waitKey(1)