import base64
import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
from mtcnn import MTCNN


# @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string)])
def face_rec_encoded_imgs(encoded_imgs):
    result = []
    facenet = FaceNet()
    current_path = os.getcwd().replace("\\", "/") + "/z_face_recognition"
    faces_embeddings = np.load(current_path + "/faces_embeddings_done_4classes.npz")
    Y = faces_embeddings['arr_1']
    encoder = LabelEncoder()
    encoder.fit(Y)
    detector = MTCNN()
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
        faces = detector.detect_faces(rgb_img)
        face_detected = len(faces) > 0    
        if not face_detected:
            result.append(['unknown: 100%', ""])
            final_name = "unknown"
            text = "{}".format(final_name)
            font = cv.FONT_HERSHEY_TRIPLEX
            font_scale = 0.5
            thickness = 1
            # Get the size of the text
            (text_width, text_height), _ = cv.getTextSize(text, font, font_scale, thickness)
            # Adjust the position of the text based on the size of the image
            text_x = int(rgb_img.shape[1] / 2 - text_width / 2)
            text_y = int(rgb_img.shape[0] / 2 - text_height / 2)
            # Draw the text
            cv.putText(rgb_img, text, (text_x, text_y), font, font_scale, (0, 255, 0), thickness)
            continue
        else:    
            for face in faces:
                x,y,w,h = face['box']
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
                # Draw bounding box and label on image
                font = cv.FONT_HERSHEY_TRIPLEX
                font_scale = 0.5
                thickness = 1
                # Get the size of the text
                (text_width, text_height), _ = cv.getTextSize(text, font, font_scale, thickness)
                # Adjust the position of the text based on the size of the bounding box
                text_x = x + int((w - text_width) / 2)
                text_y = y + h + int(text_height * 1.5)
                # Draw the bounding box and text
                cv.rectangle(rgb_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv.putText(rgb_img, text, (text_x, text_y), font, font_scale, (0, 255, 0), thickness)
            facial_recognition_information.append(text)
            if img is not None and len(img.shape) > 0 and img.shape[0] > 0 and img.shape[1] > 0: 
                rgb_img = cv.cvtColor(rgb_img, cv.COLOR_BGR2RGB)
                encoded_string = base64.b64encode(cv.imencode('.jpg', rgb_img)[1]).decode('utf-8')
            facial_recognition_information.append(encoded_string)
            result.append(facial_recognition_information)
    return result

