import cv2
import time
from eye_detective import mark_eyes

import subprocess

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time_threshold = 3
time1 = None
time2 = None
iteration = 1

def get_faces(gray):
    faces = faceCascade.detectMultiScale(gray, 1.3, 3)
    return faces

def mark_faces(frame):
    num_eyes = 0
    global time1
    global time2
    global time_threshold
    global iteration

    # Draw a rectangle around the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = get_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        num_eyes = mark_eyes(gray, frame, x, y, w, h)

    if num_eyes <= 0:
        print("No eyes")
        if time1 == None:
            time1 = time.time()
        else:
            time2 = time.time()
            if (time2 - time1) > time_threshold:
                alert_driver()
                time1 = None
    else:
        print("Eyes")
        time1 = None
        time2 = None
        iteration = 1

def alert_driver():
    global iteration
    
    if iteration == 1:
        subprocess.run(['say', '"Are you okay?"'])
    elif iteration == 2:
        subprocess.run(['say', '"Richie, are you okay?"'])
    elif iteration == 3:
        subprocess.run(['say', '"Holy Shit, are you okay? Please be okay!"'])
    elif iteration == 4:
        subprocess.run(['say', 'Motherfucker, wake up!'])
    elif iteration >= 5:
        please = "please " * (iteration-4)
        subprocess.run(['say', please + " are you okay?"])

    print("Alerted")
    iteration += 1