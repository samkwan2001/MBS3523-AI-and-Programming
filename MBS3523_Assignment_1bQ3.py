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
        black_image = np.zeros(img.shape, np.uint8)
        half_black_image = np.zeros((round(img.shape[0] / 2), img.shape[1], img.shape[2]), np.uint8)
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        half_black_image[0:0 + img.shape[0], 0:0 + img.shape[1]] = img
        half_black_image[0:0 + img.shape[0], img.shape[1]:img.shape[1] + img.shape[1]] = cv2.flip(img, 1)
        black_image[0:0 + half_black_image.shape[0], 0:0 + half_black_image.shape[1]] = half_black_image
        black_image[half_black_image.shape[0]:half_black_image.shape[0] + half_black_image.shape[0],
        0: 0 + half_black_image.shape[1]] = cv2.flip(half_black_image, 0)
        cv2.imshow("Multiple outputs", black_image)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
