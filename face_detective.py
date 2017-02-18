import numpy as np
import cv2
import time
from eye_detective import mark_eyes

import subprocess

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time_threshold = 3
time1 = None
time2 = None
iteration = 1

txt_time1 = None
txt_time2 = None
max_txting = 3 # How many times you can be caught
times_txting = 0 # How many times you HAVE been caught
txt_wait = 1 # How many seconds to wait until next text check

def get_faces(gray):
    faces = faceCascade.detectMultiScale(gray, 1.05, 3, minSize=(100,100))
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
        txt = is_texting((x,y,w,h), frame)
        num_eyes = mark_eyes(gray, frame, x, y, w, h)

        if txt:
            alert_driver(texting=True)
        

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

def is_texting(face, frame):
    global txt_time1
    global txt_time2
    global times_txting
    global max_txting

    print("Times texting: " + str(times_txting))

    txt_time2 = time.time()

    if txt_time1 and (txt_time2 - txt_time1 < txt_wait):
        return False

    fx, fy, fw, fh = face
    starty = 80
    height, width, channels = frame.shape
    cv2.rectangle(frame, (0, starty), (width, starty + 40), (0, 0, 255), 2)

    if fy > starty:
        txt_time1 = time.time()
        times_txting += 1
        if times_txting >= max_txting:
            times_txting = 0
            return True

    return False

def alert_driver(texting=False):
    global iteration
    
    if texting:
        subprocess.run(['say', '"Get off your phone!"'])
        return

    if iteration == 1:
        subprocess.run(['say', '"Are you okay?"'])
    elif iteration == 2:
        subprocess.run(['say', '"Richie, are you sure you are okay?"'])
    elif iteration == 3:
        subprocess.run(['say', '"Holy guacamole, are you okay?"'])
    elif iteration == 4:
        subprocess.run(['say', 'You are going to die! Wake up!'])
    elif iteration >= 5:
        please = "please " * (iteration-4)
        subprocess.run(['say', please + " are you okay?"])

    print("Alerted")
    iteration += 1