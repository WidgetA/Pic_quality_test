import numpy as np
import cv2

npy = np.load('./test.npy')
bmp = cv2.imread('./test.bmp')
png = cv2.imread('./0001.png')
npy1 = np.load('./test1.npy')

print((npy == bmp).all())
print((bmp == png).all())
print((npy == png).all())
print((npy == npy1).all())
