import RPi.GPIO as GPIO
from time import sleep 
import os

ledPin = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

ledPWM = GPIO.PWM(ledPin, 100)
ledPWM.start(0)
attention = 0
reverse = False

os.system('clear')
while True:
    if attention > 10:
        ledPWM.ChangeDutyCycle(min(100, attention))
    else: 
        ledPWM.ChangeDutyCycle(0)

    if reverse:
        attention -= 1
    else:
        attention += 1
    sleep(0.1)

    if attention >= 100:
        reverse = True
    elif attention <= 0:
        reverse = False
    print ("\rValue: {}".format(attention)),
        
