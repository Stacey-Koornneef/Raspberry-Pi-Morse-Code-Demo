from guizero import App, PushButton, Text
import RPi.GPIO as GPIO
import time


def a():

    GPIO.output(12, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(12, GPIO.LOW)

    time.sleep(0.5)

    GPIO.output(12, GPIO.HIGH)

    time.sleep(1)

    GPIO.output(12, GPIO.LOW)

def b():

    GPIO.output(12, GPIO.HIGH)

    time.sleep(1)

    GPIO.output(12, GPIO.LOW)

    time.sleep(0.5)

    for i in range(0,3):
        
        GPIO.output(12, GPIO.HIGH)

        time.sleep(0.5)

        GPIO.output(12, GPIO.LOW)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

app = App(title = "Raspberry Pi Morse Code")
aButton = PushButton(app, command=a, text = "A")
flashLight = PushButton(app, command=b, text = "B")
app.display()

GPIO.cleanup()
