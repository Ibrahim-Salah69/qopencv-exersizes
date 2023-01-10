import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.circle(frame, (50, 400), 30, (100, 20, 200), thickness=3)
    cv.circle(frame, (600, 50), 30, (100, 20, 200), thickness=3)
    cv.circle(frame, (600, 400), 30, (100, 20, 200), thickness=3)
    cv.circle(frame, (50, 50), 30, (100, 20, 200), thickness=3)
    cv.putText(frame, 'Edge Detection', (225, 50),
               cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    Img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur_img = cv.GaussianBlur(Img_gray, (5, 5), 0)
    edge_img = cv.Canny(blur_img, 50, 50)
    cv.imshow('Video', edge_img)
    if cv.waitKey(20) & 0xFF == ord('e'):
        break
