import numpy as np
import cv2
import os


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f[0] == '.':
            yield f


npy_list = list(listdir_nohidden('./npy'))
bmp_list = list(listdir_nohidden('./bmp'))
png_list = list(listdir_nohidden('./png'))
ffmpeg_list = list(listdir_nohidden('./ffmpeg'))

frames = 0
if len(npy_list) == len(bmp_list) == len(png_list):
    frames = len(npy_list)
else:
    print('error!')
    exit()

opencv_frame = []
ffmpeg_frame = []
for i in range(frames):
    npy = np.load('./npy/' + npy_list[i])
    bmp = cv2.imread('./bmp/' + npy_list[i][:-3] + 'bmp')
    png = cv2.imread('./png/' + npy_list[i][:-3] + 'png')
    ffmpeg = cv2.imread('./ffmpeg/' + npy_list[i][:-3] + 'png')

    if (npy == bmp).all() and (npy == png).all() and (npy == bmp).all():
        if (npy == ffmpeg).all():
            pass
        else:
            ffmpeg_frame.append(i)
    else:
        opencv_frame.append(i)

if opencv_frame is []:
    pass
else:
    print(f'In opencv, {opencv_frame} are different!')

if ffmpeg_frame is []:
    pass
else:
    print(f'In ffmpeg, {ffmpeg_frame} are different!')

