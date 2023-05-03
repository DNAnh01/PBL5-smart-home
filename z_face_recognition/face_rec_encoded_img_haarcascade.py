import base64
import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet


def face_rec_encoded_imgs(encoded_imgs):
    result = []
    facenet = FaceNet()
    current_path = os.getcwd().replace("\\", "/") + "/z_face_recognition"
    faces_embeddings = np.load(current_path + "/faces_embeddings_done_4classes.npz")
    Y = faces_embeddings['arr_1']
    encoder = LabelEncoder()
    encoder.fit(Y)
    detector = cv.CascadeClassifier(current_path + "/haarcascade_frontalface_default.xml")
    model = pickle.load(open(current_path + "/svm_model_160x160.pkl", 'rb'))
    for encoded_img in encoded_imgs:
        facial_recognition_information = []
        text = ""
        encoded_string = ""
        # decoded image 
        decoded_image = base64.b64decode(encoded_img)
        img_array = np.frombuffer(decoded_image, np.uint8)
        img = cv.imdecode(img_array, cv.IMREAD_COLOR)
        rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray_img, 1.3, 5)
        face_detected = len(faces) > 0    
        if not face_detected:
            result.append(['unknown: 100%', ""])
            continue
        else:    
            for x,y,w,h in faces:
                img_face = rgb_img[y:y+h, x:x+w]
                img_face = cv.resize(img_face, (160,160)) # 1x160x160x3
                img_face = np.expand_dims(img_face,axis=0)
                ypred = facenet.embeddings(img_face)
                face_prob = model.predict_proba(ypred)
                max_prob = np.max(face_prob)
                if max_prob < 0.75:
                    final_name = "unknown"
                    text = "{}: {:.2f}%".format(final_name, 100)
                else:
                    face_name = model.predict(ypred)
                    final_name = encoder.inverse_transform(face_name)[0]
                    text = "{}: {:.2f}%".format(final_name, max_prob*100)
                cv.rectangle(rgb_img, (x,y), (x+w,y+h), (0,0,255), 3)
                cv.putText(rgb_img, text, (x,y-30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
            facial_recognition_information.append(text)
            if img is not None and len(img.shape) > 0 and img.shape[0] > 0 and img.shape[1] > 0: 
                rgb_img = cv.cvtColor(rgb_img, cv.COLOR_BGR2RGB)
                img_resized = cv.resize(rgb_img, (500, 700)) # Resize image for display
                encoded_string = base64.b64encode(cv.imencode('.jpg', img_resized)[1]).decode('utf-8')
            facial_recognition_information.append(encoded_string)
            result.append(facial_recognition_information)
    return result
        
import base64
current_path = os.getcwd().replace("\\", "/") + "/z_face_recognition"
path = current_path + "/test_img/NguyenAnh_test.jpg"
def encode_img(path):
    with open(path, "rb") as image_file:
        print(image_file)
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return [encoded_string]
print(face_rec_encoded_imgs(encoded_imgs=encode_img(path=path)))

