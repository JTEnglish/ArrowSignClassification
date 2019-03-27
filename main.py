#!/usr/bin/env python3

import argparse
import imutils
import cv2

from ArrowClassifier import ArrowClassifier

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to the input image")
    args = vars(ap.parse_args())

    # load the image and resize it to a smaller factor so that
    # the shapes can be approximated better
    image = cv2.imread(args["image"])
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("blur", blurred)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("threshold", thresh)

    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
           cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    ac = ArrowClassifier()

    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)
        direction = ''
        try:
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)
        except:
            continue

        try:
            direction = ac.get_direction(c)
        except ValueError:
            continue

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, direction, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (255, 0, 255), 2)

    # show the output image
    cv2.imshow("Image", imutils.resize(image, width=1000))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()