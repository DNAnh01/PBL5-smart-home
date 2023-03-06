import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    './src/cascades/data/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)
    for x, y, w, h in faces:
        print(x, y, w, h)
        # The area of gray is interested
        roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        # recognize? deep learned model predict keras tensorflow pytorch scikit learn


        # Draw a Rectangle

        color = (225, 0, 0) # Red Green Blue 0-255
        stroke = 2
        end_cord_x = x + w # width
        end_cord_y = y + h # height

        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # Cut and save face photos "./src/images/my-image.png"
        img_item = "./src/images/my-image.png"
        cv2.imwrite(img_item, roi_gray)
    # Display the resulting frame

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()
