import cv2
from eye_detective import mark_eyes

import subprocess
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_faces(gray):
    faces = faceCascade.detectMultiScale(gray, 1.05, 3, minSize=(100,100))
    return faces

def mark_faces(frame):
    # Draw a rectangle around the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = get_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        mark_eyes(gray, frame, x, y, w, h)

def alert_driver():
    subprocess.run('say "Are you okay?"')