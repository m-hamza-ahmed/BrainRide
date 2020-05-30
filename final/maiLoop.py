import RPi.GPIO as GPIO
import os
from time import sleep
from headsetDataParser import Parser

# Setting up GPIO and PWM
in1 = 24
in2 = 23
en = 25
temp1=1

# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

# Set up PWM contorllers
p = GPIO.PWM(en,1000)
p.start(40)


# Boolean variables to keep track of car's movements
CAR_MOVING = False
FORWARD = True


def main():
    print ("I am in main")
    # Initialize parser
    p = Parser()

    # Initialize loop variables
    spectra = []
    iteration = 0

    # Logic to check if disconnected
    disconnectCounter = 0
    disconnectLastAttention = 0

    firstRound = True
    blinks = 0

    # Main loop
    while True:
        p.update()
        if p.sending_data:
            iteration += 1        
            # Get attention and meditation
            attention = p.current_attention
            meditation = p.current_meditation

            # Save previous value and see if the headset is disconnected. (Let's say after 300 same values)
            if firstRound:
                disconnectLastAttention = attention
                firstRound = False
            else:
                if disconnectLastAttention == attention:
                    disconnectCounter += 1
                else:
                    disconnectLastAttention = attention
                    disconnectCounter = 0
            
            # If same values were recieved 300 times, then we have a problem
            if disconnectCounter >= 300:
                print("\nHeadset has been taken off by the user. Please put it back on...")
                print("Attention: " + str(p.current_attention))
                sleep(1)
                attention = 0
                meditation = 0

            if not p.current_blink_strength == 0:
                debugf.write("Blinked: " + str(p.current_blink_strength))
                blinks += 1

            # Print job
            os.system('clear')
            print ("Poor signal: " + str(p.poor_signal))
            print ("Blink: " + str(blinks))

            temp = ''
            print ("Current attention: "),
            for i in range(0, 50):
                if i <= (attention/2):                
                    temp = temp + '>'
                else:
                    temp = temp + '-'
            print (temp)
            attentionUpdted(attention)

            temp = ''
            print ("Current meditation: "),
            for i in range(0, 50):
                if i <= (meditation/2):                
                    temp = temp + '>'
                else:
                    temp = temp + '-'
            print (temp)

            if len(p.current_vector)>7:
                m = max(p.current_vector)
                for i in range(7):
                    value = p.current_vector[i] *100.0/m
        else:
            print ("Brainsense headset is not sending data...")

def attentionUpdted(attention):
    # the attention we have is between 45-95 = 60 intervals
    # We have 1000 intervals of the PWM duty cycle but it is spread between 0-100
    # The motor is running between 45-95.

    if attention >= 45:
        # Set duty cycle
        p.ChangeDutyCycle(attention)
        if not CAR_MOVING:
            if FOWARD:
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                CAR_MOVING = True
    elif attention < 45:
        if CAR_MOVING:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            CAR_MOVING = False

if __name__ == "__main__":
    main()