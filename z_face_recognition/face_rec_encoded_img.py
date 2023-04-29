import base64
import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
import matplotlib.pyplot as plt

class FaceRecEncodedImg():
    def __init__(self, encoded_img):
        self.encoded_img = encoded_img
        self.facenet = FaceNet()
        self.current_path = os.getcwd().replace("\\", "/") + "/z_face_recognition"
    
    # @tf.function(autograph=False, jit_compile=True, experimental_relax_shapes=True, experimental_compile=True, reduce_retracing=True)
    def face_rec_encoded_img(self):
        facial_recognition_information = []
        faces_embeddings = np.load(self.current_path + "/faces_embeddings_done_4classes.npz")
        Y = faces_embeddings['arr_1']
        encoder = LabelEncoder()
        encoder.fit(Y)
        haarcascade = cv.CascadeClassifier(self.current_path + "/haarcascade_frontalface_default.xml")
        model = pickle.load(open(self.current_path + "/svm_model_160x160.pkl", 'rb'))
        # decoded image 
        decoded_image = base64.b64decode(self.encoded_img)
        img_array = np.frombuffer(decoded_image, np.uint8)
        img = cv.imdecode(img_array, cv.IMREAD_COLOR)
        rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = haarcascade.detectMultiScale(gray_img, 1.3, 5)
        for x,y,w,h in faces:
            img_face = rgb_img[y:y+h, x:x+w]
            img_face = cv.resize(img_face, (160,160)) # 1x160x160x3
            img_face = np.expand_dims(img_face,axis=0)
            ypred = self.facenet.embeddings(img_face)
            face_prob = model.predict_proba(ypred)
            max_prob = np.max(face_prob)
            if max_prob < 0.75:
                final_name = "unknown"
                text = "{}: {:.2f}%".format(final_name, max_prob*100)
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
            return facial_recognition_information
        else:
            return None
        