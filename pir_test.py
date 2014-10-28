import time

try:
    import RPi.GPIO as GPIO
except:
    print("RPi.GPIO is not installed or could not be found.")


# Settings
sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

while True:
    time.sleep(.1)
    prevState = currState
    currState = GPIO.input(sensorPin)
    if currState != prevState:
        print "GPIO pin {0} is {1}".format(sensorPin, "HIGH" if currState else "LOW")
