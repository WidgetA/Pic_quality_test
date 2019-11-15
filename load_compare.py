import numpy as np
import cv2
import os


def listdir_nohidden(path):
    for f in os.listdir(path):
        if f[0] == '.':
            yield f


npy_list = list(listdir_nohidden('./npy'))
bmp_list = list(listdir_nohidden('./bmp'))
png_list = list(listdir_nohidden('./png'))
ffmpeg_list = list(listdir_nohidden('./ffmpeg'))

frames = 0
if len(npy_list) == len(bmp_list) == len(png_list):
    frames = len(npy_list)
else:
    pass

wrong_frame = []
for i in range(frames):
    npy = np.load(npy_list[i])
    bmp = cv2.imread(bmp_list[i])
    png = cv2.imread(png_list[i])
    ffmpeg = cv2.imread(ffmpeg_list[i])

    if (npy == bmp).all() and (npy == png).all() and (npy == ffmpeg).all():
        wrong_frame.append(i)
    else:
        continue

    print(f'frame {i} has finished!')

print(f'{wrong_frame} are different!')
