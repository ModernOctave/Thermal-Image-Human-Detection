import sys
from PIL import Image
import cv2 as cv
import glob
import tensorflow as tf
import numpy as np
from time import time

START_BUFFER = 10

human_image_paths = glob.glob("dataset/human/*.jpg")
print("Found {} human images".format(len(human_image_paths)))
no_human_image_paths = glob.glob("dataset/no_human/*.jpg")
print("Found {} no-human images".format(len(no_human_image_paths)))
image_paths = human_image_paths + no_human_image_paths
print("Total images: {}".format(len(image_paths)))

model = tf.saved_model.load(sys.argv[1])
time_total = 0

expected = True
fps = 0
for i, image_path in enumerate(image_paths):
    image = np.split(cv.imread(image_path), 3, axis=2)[0]
    start = time()
    if model([image]) > 0.5:
        human = True
    else:
        human = False
    end = time()
    cv.imshow("image", image)
    cv.waitKey(1)
    if i > START_BUFFER:
        time_total += end - start
        fps = (i-START_BUFFER)/time_total
    if i == len(human_image_paths):
        expected = False
    print(f"Human detected: {human}/{expected} | FPS: {fps}")
