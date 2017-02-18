import cv2
import subprocess

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_faces(gray):

    faces = faceCascade.detectMultiScale(gray, 1.3, 3)
    return faces

def mark_faces(frame):
    # Draw a rectangle around the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = get_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

def alert_driver():
    subprocess.run('say "Are you okay?"')