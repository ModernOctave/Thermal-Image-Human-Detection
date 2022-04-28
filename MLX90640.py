import board
import busio
import adafruit_mlx90640
import cv2
import numpy as np

class MLX90640_Sensor:
    def __init__(self):
        print("MLX90640-Driver: Initializing sensor")
        i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
        self.mlx = adafruit_mlx90640.MLX90640(i2c)
        print("MLX90640-Driver: Sensor address detected on I2C - ", [hex(i) for i in mlx.serial_number])
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ
        print("MLX90640-Driver: Sensor initialized")
        self.raw_frame = [0] * 768

    def getFrame(self):
        try:
            self.mlx.getFrame(self.raw_frame)
        except ValueError:
            pass
        self.frame = np.reshape(self.raw_frame, (24, 32))
        cv2.normalize(self.frame, self.frame, 255, 0, cv2.NORM_MINMAX)
        return self.frame, cv2.resize(self.frame, (480, 640))