import cv2

def hough_gradient(frame, gray):
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.05, 10)

	if circles is not None:
		circles = np.round(circles[0, :]).astype("int") 

	for (x, y, r) in circles:
	    # draw the circle in the output image, then draw a rectangle
	    # corresponding to the center of the circle
	    cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
	    cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
