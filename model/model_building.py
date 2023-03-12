import numpy as np
import os
from PIL import Image
import tensorflow
from tensorflow.keras import layers
from tensorflow.keras import models
import cv2

face_detector = cv2.CascadeClassifier('E:/BKDN/ky6/PBL5/code/face-detection/haarcascade/haarcascade_frontalface_alt.xml')


# TRAIN_DATA = 'model\dataset\\train-data'
# TEST_DATA = 'model\dataset\\test-data'

# Xtrain = []
# ytrain = []

# # Xtrain = [(matranhinh1, ohe1), (matranhinh2, ohe2), .... ]

# # Xtrain = [x[0] for i, x in enumerate(Xtrain)]


# Xtest = []
# ytest = []


# dict = {'posNguyenAnh': [1, 0, 0, 0], 
#         'posNgocAnh':   [0, 1, 0, 0],
#         'posHongVan':   [0, 0, 1, 0],
#         'posNhuQuynh':  [0, 0, 0, 1],
#         'testNguyenAnh':[1, 0, 0, 0], 
#         'testNgocAnh':  [0, 1, 0, 0],
#         'testHongVan':  [0, 0, 1, 0],
#         'testNhuQuynh': [0, 0, 0, 1]}



# def getData(dirData, lstData):
#     for whatever in os.listdir(dirData):
#         whatever_path = os.path.join(dirData, whatever)
#         lst_filename_path = []
#         for filename in os.listdir(whatever_path):
#             filename_path = os.path.join(whatever_path, filename)
#             label = filename_path.split('\\')[3]
#             img = np.array(Image.open(filename_path))
#             lst_filename_path.append((img, dict[label]))
#         lstData.extend(lst_filename_path)
#     return lstData

# Xtrain = getData(TRAIN_DATA, Xtrain)
# for i in range(10):
#     np.random.shuffle(Xtrain)
# print(Xtrain[20])

# model_training = models.Sequential([
#     layers.Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.15),

#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.20),

#     layers.Conv2D(128, (3, 3), activation='relu'),
#     layers.MaxPool2D((2, 2)),
#     layers.Dropout(0.20),

#     layers.Flatten(input_shape=(32, 32, 3)),
#     layers.Dense(1000, activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(4, activation='softmax'), # chính là cái dự đoán cuối cùng, 10 dense -> 10 classes
# ])
# # model_training.summary()

# model_training.compile(optimizer='adam',
#                             loss='categorical_crossentropy',
#                             metrics=['accuracy'])
# model_training.fit(np.array([x[0] for _, x in enumerate(Xtrain)]), np.array([y[1] for _, y in enumerate(Xtrain)]), epochs=10) # thông thường lặp epochs = 250

# model_training.save('model-PBL5-smart-home.h5')

models = models.load_model('model-PBL5-smart-home.h5')

lstResult = ['Nguyen Anh', 'Ngoc Anh', 'Hong Van', 'Nhu Quynh']

cam = cv2.VideoCapture('???')
while True:
    ret, frame =  cam.read()
    faces =face_detector.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    # time.sleep(0.5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        # roi = cv2.resize(frame[y+2: y+h-2, x+2:x+w-2], (100, 100)) 
        # cv2.imwrite('E:/BKDN/ky6/PBL5/code/face-detection/imgs_roi/roi_{}.jpg'.format(count), roi)
        roi = cv2.resize(frame[y:y+h, x:x+w], (128, 128)) # face detect using video
        result = np.argmax(models.predict(roi.reshape((-1, 128, 128, 3))))
        # Draw a Rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 0, 0), 2)
        cv2.putText(frame, lstResult[result], (x+15, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imshow('FRAME', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()




