from teachable_machine import TeachableMachine
import cv2 as cv
import time

cap = cv.VideoCapture(0)
model = TeachableMachine(model_path="keras_model.h5",
                         labels_file_path="labels.txt")

image_path = "screenshot.jpg"

while True:
    _, img = cap.read()
    cv.imwrite(image_path, img)
    # time.sleep(1)
    result = model.classify_image(image_path)

    print("class_name:::", result["class_name"])

    cv.imshow("Video Stream", img)

    cv.waitKey(1)
