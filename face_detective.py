import numpy as np
import cv2
import time
from eye_detective import mark_eyes
from alert_authorities import text_alerts
import subprocess

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time_threshold = 1.5
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

    # Draw a rectangle around the faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = get_faces(gray)

    txt = False
    sleep = None
    focused = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        txt = is_texting((x,y,w,h), frame)
        num_eyes = mark_eyes(gray, frame, x, y, w, h)
        sleep = is_sleeping(num_eyes)
        focused = is_focused(num_eyes)

        if txt:
            alert_driver(texting=True)

    return txt, sleep, focused


def is_focused(num_eyes):
    if num_eyes == 2:
        return True
    return False

def is_sleeping(num_eyes):
    global time1
    global time2
    global time_thresholdq
    global iteration

    if num_eyes <= 0:
        if time1 == None:
            time1 = time.time()
        else:
            time2 = time.time()
            if (time2 - time1) > time_threshold:
                print("alerted")
                alert_driver()
                time1 = None
                return True
            return None
    else:
        time1 = None
        time2 = None
        iteration = 1
        return False
    
    return None


def is_texting(face, frame):
    global txt_time1
    global txt_time2
    global times_txting
    global max_txting

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
        subprocess.Popen(['say', '"Get off your phone!"'])
        return

    
    subprocess.Popen(['say', '"Wake up!"'])
    """
    elif iteration == 2:
        subprocess.Popen(['say', '"Richie, are you sure you are okay?"'])
    elif iteration == 3:
        subprocess.Popen(['say', '"Holy guacamole, are you okay?"'])
    elif iteration == 4:
        subprocess.Popen(['say', 'You are going to die! Wake up!'])
    elif iteration >= 5:
        please = "please " * (iteration-4)
        subprocess.Popen(['say', please + " are you okay?"])
    """
    if iteration == 3:
        print("Texting")
        
    iteration += 1
