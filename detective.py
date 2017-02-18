import cv2
import sys
from face_detective import mark_faces

class Detective():
    def __init__(self):
        pass

    def track_faces(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            frame = cv2.resize(frame,None,fx=0.4, fy=0.4, interpolation = cv2.INTER_CUBIC)
            mark_faces(frame)
            
            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    d = Detective()
    d.track_faces()