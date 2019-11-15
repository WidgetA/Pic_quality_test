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

wrong_frame = []
for i in range(frames):
    npy = np.load('./npy/' + npy_list[i])
    bmp = cv2.imread('./bmp/' + bmp_list[i])
    png = cv2.imread('./png/' + png_list[i])
    ffmpeg = cv2.imread('./ffmpeg/' + ffmpeg_list[i])

    print(npy.shape)
    print(bmp.shape)

print(f'{wrong_frame} are different!')
