# @author: Dani atalla
# Data: 10/10/21


import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()



cap = cv.VideoCapture(r'your code in here')

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(img, (cx, cy), 2, (255, 0, 0), cv.FILLED)


    # cv.imshow("Image", img)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3,
               (255, 0, 0),3)
    print ('Original Dimensions : ', img.shape)
    scale_percent = 40  # percent of original size
    width = int (img.shape[1] * scale_percent / 100)
    height = int (img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv.resize (img, dim, interpolation=cv.INTER_AREA)
    print ('Resized Dimensions : ', resized.shape)
    cv.imshow ("Resized image", resized)

    cv.waitKey(1)
