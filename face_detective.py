import cv2

def get_faces(gray):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=1,
                minSize=(30, 30),
                flags= 0
            )
    return faces

def mark_faces(frame):
    # Draw a rectangle around the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = get_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)