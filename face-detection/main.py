# Detect faces of images

import cv2
import os
import time

image_path = 'E:/BKDN/ky6/PBL5/code/face-detection/imgs'
face_detector = cv2.CascadeClassifier('E:/BKDN/ky6/PBL5/code/face-detection/haarcascade/haarcascade_frontalface_alt.xml')
# def getFaces(image_path):
#     img = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=5)
#     count = 0
#     for (x, y, w, h) in faces:
#         img_face = cv2.resize(img[y+3: y+h-3, x+3: x+w-3], (64, 64))
#         cv2.imwrite(image_path.replace('imgs', 'imgs_face').split('.jpg')[0] + '_{}.jpg'.format(count), img_face)
#         # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         count += 1

# for what_else in os.listdir(image_path):
#     what_else_path = os.path.join(image_path, what_else)
#     for sub_what_else in os.listdir(what_else_path):
#         img_path = os.path.join(what_else_path, sub_what_else)
#         # print(img_path)
#         imgs_face_path  = what_else_path.replace('imgs', 'imgs_face')
#         if not os.path.isdir(imgs_face_path):
#             os.mkdir(imgs_face_path)
#             # print(imgs_face_path)
#         if img_path.endswith('.jpg'):
#             getFaces(img_path)

# cv2.destroyAllWindows()

# Face detect using webcam 
cam = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame =  cam.read()
    faces =face_detector.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    time.sleep(0.5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi = cv2.resize(frame[y+2: y+h-2, x+2:x+w-2], (100, 100)) 
        cv2.imwrite('E:/BKDN/ky6/PBL5/code/face-detection/imgs_roi/roi_{}.jpg'.format(count), roi)
        # Draw a Rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 0, 0), 2)
        count += 1
    cv2.imshow('FRAME', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()

