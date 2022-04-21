import sys
from PIL import Image
import cv2 as cv
import glob
import tensorflow as tf
import numpy as np
from time import time

frame_srcs = glob.glob("../FLIR_ADAS_v2/images_thermal_val/data/*.jpg")
frame_srcs.sort()

model = tf.saved_model.load(sys.argv[1])
time_total = 0

for i, frame_src in enumerate(frame_srcs):
    frame = np.array(Image.open(frame_src))
    frames = (np.expand_dims([frame], axis=-1)/255.).astype(np.float32)
    start = time()
    if model(frames) > 0.5:
        human = True
    else:
        human = False
    end = time()
    cv.imshow("frame",frame)
    cv.waitKey(1)
    if i > 10:
        time_total += end - start
        fps = (i-10)/time_total
        print(f"Human detected: {human} | FPS: {fps}")
