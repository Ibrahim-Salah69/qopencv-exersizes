import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    resizedFrame = cv.resize(frame, (800, 600))
    gray = cv.cvtColor(resizedFrame, cv.COLOR_BGR2GRAY)
    cv.putText(gray, 'Ibrahim Salah', (10, 225),
               cv.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 3)
    cv.imshow('Video', gray)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
