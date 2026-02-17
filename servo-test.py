import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


while True:
    for angle in range(1, 180):
        kit.servo[0].angle = angle
        time.sleep(0.01)
    time.sleep(1)

    for angle in range(180, 0, -1):
        kit.servo[0].angle = angle
        time.sleep(0.01)
    time.sleep(1)