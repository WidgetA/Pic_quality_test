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
    if img is None:
        continue
    else:
        pass
    cv2.imwrite(f'./bmp/test{frame_count}.bmp', img)
    cv2.imwrite(f'./png/test{frame_count}.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    np.save(f'./npy/test{frame_count}.npy', img)
    frame_count += 1

os.system("ffmpeg -i ./test_video/test_video.mp4 -f image2 ./ffmpeg/test%d.png")