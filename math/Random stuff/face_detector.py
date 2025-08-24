import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trained_smile_data = cv2.CascadeClassifier('smile.xml')


#img = cv2.imread('Leo.png')
webcam = cv2.VideoCapture("meme.mp4")
#webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()
    
    if not successful_frame_read:
        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(frame_grayscale)
    
    for(x, y, w, h) in face_coordinates: #0 means the first face it detects since its the first in the list
        cv2.rectangle(frame, (x, y) ,(x+w, y+h), (0, 255, 0), 2)# image, coordinates, grubość

        the_face = frame[y:y+h ,x:x+w]

        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smile_coordinates = trained_smile_data.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)


        for(x_, y_, w_, h_) in smile_coordinates: #0 means the first face it detects since its the first in the list
            cv2.rectangle(the_face, (x_, y_) ,(x_+w_, y_+h_), (0, 0, 255), 2)# image, coordinates, grubość

        if len(smile_coordinates) > 0:
            cv2.putText(frame, 'Smile :)', (x, y+h+40), fontScale=3, fontFace = cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    

    cv2.imshow('Clever', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

webcam.release()
cv2.destroyAllWindows()
print("Works")