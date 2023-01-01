import cv2 as cv

img = cv.imread("car.jfif")
resizedImg = cv.resize(img, (800, 600))
cv.imshow("car resized", resizedImg)
cv.imshow("car", img)
cv.waitKey(0)
