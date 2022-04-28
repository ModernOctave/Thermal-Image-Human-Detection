from MLX90640 import MLX90640_Sensor
import tensorflow as tf
import cv2 as cv
from time import time
import numpy as np

MODEL_PATH = "./models/MLX90640-1"

fps = []
last_time = time()

sensor = MLX90640_Sensor()
model = tf.saved_model.load(MODEL_PATH)

while True:
    last_time = curr_time
    curr_time = time()
    fps.append(1/(curr_time-last_time))
    fps = fps[-10:]
    frame, resized_frame = sensor.getFrame()
    cv.imshow("image", resized_frame)
    cv.waitKey(1)
    if model([frame]) > 0.5:
        print(f"fps: {np.average(fps)} Result: Human detected")
    else:
        print(f"fps: {np.average(fps)} Result: No human detected")