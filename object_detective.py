import cv2

plate_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

def get_plates(gray):
    plates = plate_cascade.detectMultiScale(gray, 1.4, 2)
    return plates

def mark_plates(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = get_plates(gray)

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

