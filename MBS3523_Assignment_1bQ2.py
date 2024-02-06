import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    while True:
        key = cv2.waitKey(1)
        if key == 27 or key == 'q':
            break
        s, img = cap.read()
        if not s:
            print("cap not success")
            break
        # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Webcam Canny Edges",cv2.Canny(img,100,300))
        cv2.imshow("Webcam", img)
        cv2.imshow("Webcam HSV",cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
        cv2.imshow("Webcam Gaussian Blur",cv2.GaussianBlur(img,(5,5),0))

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
