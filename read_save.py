import cv2
import numpy as np

video = './test_video.mp4'

cap = cv2.VideoCapture(video)
cap.set(cv2.CAP_PROP_FRAME_COUNT, 4)
ret = True
frame_count = 1
while ret:
    ret, img = cap.read()
    frame_count += 1
    cv2.imwrite(f'./test{frame_count}.bmp', img)
    cv2.imwrite(f'./test{frame_count}.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    np.save(f'./test{frame_count}.npy', img)
