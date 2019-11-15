import cv2
import numpy as np
import os

video = './test_video/test_video.mp4'

cap = cv2.VideoCapture(video)
cap.set(cv2.CAP_PROP_FRAME_COUNT, 4)
ret = True
frame_count = 1
while ret:
    ret, img = cap.read()
    frame_count += 1
    cv2.imwrite(f'./test_video/test{frame_count}.bmp', img)
    cv2.imwrite(f'./test_video/test{frame_count}.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    np.save(f'./test_video/test{frame_count}.npy', img)

os.system("ffmpeg -i ./test_video/test_video.mp4 -f image2 ./ffmpeg/test%d.png")