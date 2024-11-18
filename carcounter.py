from ultralytics import YOLO
import cv2 as cv 
import cvzone as cvz 
import math 




#cap = cv.VideoCapture(0) #For Webcam
#cap.set(3,1280)
#cap.set(4,720)

cap = cv.VideoCapture("cars.mp4")   #For Videos



model = YOLO('yolov8n.pt')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

vehicle_count = 0

#mask = cv.imread("mask-950x480.png")

while True:
    success, img = cap.read()
    #imgRegion = cv.bitwise_and(img,mask)
    results = model(img,stream=True)

    frame_vehicle_count = 0

    for r in results:
        boxes = r.boxes
        for box in boxes:

            #Bounding Box 
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2) 
            #cv.rectangle(img, (x1,y1),(x2,y2),(100,100,100),3)
            w,h=x2-x1,y2-y1 

            #cvz.cornerRect(img,(x1,y1,w,h),l=9)

            #Confidence 
            conf = math.ceil((box.conf[0]*100))/100
            #cvz.putTextRect(img,f'{conf}',(max(0,x1),max(35,y1)))
            #cvz.putTextRect(img,str(float(conf)),(x1,y1-20))

            #Class Name
            cls = int(box.cls[0])
            #print()
            currentClass = classNames[cls]

            if currentClass == "car" or currentClass == "truck" or currentClass == "bus" or currentClass == "motorbike" and conf > 0.3:
              
              frame_vehicle_count +=1

              cvz.putTextRect(img,f'{currentClass} {conf}',(max(0,x1),max(35,y1)), scale=0.6 ,thickness=1, offset=3  )
              cvz.cornerRect(img,(x1,y1,w,h),l=9)

        vehicle_count += frame_vehicle_count
        cv.putText(img,f'Total vehicles: {vehicle_count}',(50,50), cv.FONT_HERSHEY_SIMPLEX,1,(250,0,0),2)
              


              
            

    cv.imshow('Image',img)
    #cv.imshow('Image Masked',imgRegion)
    cv.waitKey(1)