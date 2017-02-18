import cv2
from circle_detective import hough_gradient

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

def get_eyes(gray):
    eyes = eye_cascade.detectMultiScale(gray, 1.05, 6, minSize=(20,20))
    return eyes

def mark_eyes(gray, frame, x, y, w, h):
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    eyes = get_eyes(roi_gray)

    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        
    return len(eyes)

