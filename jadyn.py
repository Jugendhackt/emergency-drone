import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

def set_pos(pin, value):
    dutycicle = 0.01
    on_time = 0.001 + (value / 1000)
    off_time = dutycicle - on_time
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(on_time)
    GPIO.output(pin, GPIO.LOW)
    
i = float(input())
while True:
    set_pos(17, i)
