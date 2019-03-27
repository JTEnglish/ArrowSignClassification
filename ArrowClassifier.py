import cv2
import matplotlib.pyplot as plt

class ArrowClassifier:
    def __init__(self):
        pass
    
    def get_direction(self, contour):
        peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.0265 * peri, True)

        direction = 'Up'

        if len(approx) == 7:
            return direction