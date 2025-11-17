import pigpio
import time

pi = pigpio.pi()

pin = 19

angle = 10

pi.set_servo_pulsewidth(pin, 1500 + angle*10)
time.sleep(1)

pi.set_servo_pulsewidth(pin, 0)
pi.stop()