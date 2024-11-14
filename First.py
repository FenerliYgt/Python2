from ultralytics import YOLO
import cv2 as cv 
import cvzone as cvz 
import math 

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

model = YOLO('yolov8n.pt')

classNames = ["Me"]



while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:

            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)

            w,h = x2-x1,y2-y1
            cvz.cornerRect(img,(x1,y1,w,h))

            conf = math.ceil((box.conf[0]*100))/100

            cls = int(box.cls[0])

            if cls < len(classNames):
                class_name = classNames[cls]
            else:
                class_name = "Unknown"


            print()

            cvz.putTextRect(img, f'{class_name} {conf}',(max(0,x1),max(35,y1)))


    cv.imshow('Image',img)
    cv.waitKey(1)