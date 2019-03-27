import cv2
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class ArrowClassifier:
    pointList = []

    def __init__(self):
        if __debug__:
            print('Debug print statements enabled. Disable with python -O option.\n')

    def __get_midpoint(self, a, b):
        a = (float(a[0]), float(a[1]))
        b = (float(b[0]), float(b[1]))

        return ( (a[0]+b[0])/2, (a[1]+b[1])/2 )

    def __find_concave_regions(self):
        concave_regions = []

        #get pairs of points (i, i+2)
        pt_pairs = []
        for i in range(5):
            pt_pairs.append((self.pointList[i], self.pointList[i+2]))
        #cover the wrap-around cases
        pt_pairs.append((self.pointList[5], self.pointList[0]))
        pt_pairs.append((self.pointList[6], self.pointList[1]))

        for pair in pt_pairs:
            midpt = self.__get_midpoint(pair[0], pair[1])
            pt = Point(midpt[0], midpt[1])

            polygon = Polygon(self.pointList)
            if not polygon.contains(pt):
                concave_regions.append(midpt)

        if len(concave_regions) != 2:
            raise ValueError('Invalid contour shape.')

        if __debug__:
            print('\nConcave region midpoint list:', concave_regions)

        return concave_regions
    
    def get_direction(self, contour):
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.0265 * peri, True)

        direction = 'Up'

        if __debug__:
            print('Size of contour approximation point list:', len(approx))

        if len(approx) == 7:
            for pt in approx:
                self.pointList.append((pt[0][0], pt[0][1]))

            if __debug__:
                print('pointList:', self.pointList)

            cr = self.__find_concave_regions()
            
            return direction
        else:
            raise ValueError('Invalid number of contour approximation points.')