import cv2

video = cv2.VideoCapture('people.mp4')

car_file = 'car.xml'
people_file = 'people.xml'

car_tracker = cv2.CascadeClassifier(car_file)
people_tracker = cv2.CascadeClassifier(people_file)

while True:

    (read_successful, frame) = video.read()

    if read_successful:

        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    people = people_tracker.detectMultiScale(grayscaled_frame)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Clever', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()
print("Works")
