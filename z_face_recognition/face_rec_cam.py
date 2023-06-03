#IMPORT
import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
#INITIALIZE
facenet = FaceNet()
current_path = os.getcwd().replace("\\", "/") + "/z_face_recognition"
faces_embeddings = np.load(current_path + "/faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
detector = cv.CascadeClassifier(current_path + "/haarcascade_frontalface_default.xml")
model = pickle.load(open(current_path + "/svm_model_160x160.pkl", 'rb'))

cap = cv.VideoCapture("C:/Users/dongu/OneDrive/Tài liệu/NguyenAnh.mp4")
# WHILE LOOP
while cap.isOpened():
    _, frame = cap.read()
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray_img, 1.3, 5)
    for x,y,w,h in faces:
        img = rgb_img[y:y+h, x:x+w]
        img = cv.resize(img, (160,160)) # 1x160x160x3
        img = np.expand_dims(img,axis=0)
        ypred = facenet.embeddings(img)
        face_prob = model.predict_proba(ypred)
        max_prob = np.max(face_prob)
        if max_prob < 0.6:
            final_name = "unknown"
            text = "{}: {:.2f}%".format(final_name, max_prob*100)
        else:
            face_name = model.predict(ypred)
            final_name = encoder.inverse_transform(face_name)[0]
            text = "{}: {:.2f}%".format(final_name, max_prob*100)
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        cv.putText(frame, text, (x,y-30), cv.FONT_HERSHEY_SIMPLEX,
                1, (0,255,0), 3)
    # Thay đổi kích thước khung hình trước khi hiển thị
    # frame = cv.resize(frame, (800, 500)) # Chỉnh kích thước khung hình tại đây
    cv.imshow("Face Recognition:", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows