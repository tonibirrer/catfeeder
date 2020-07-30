import RPi.GPIO as GPIO
import time

PIN = 18
PWMA1 = 6
PWMA2 = 13
PWMB1 = 20
PWMB2 = 21
D1 = 12
D2 = 26
PWM = 50

def set_motor(A1,A2):
    GPIO.output(PWMB1,A1)
    GPIO.output(PWMB2,A2)

def forward():
    GPIO.output(PWMB1,1)
    GPIO.output(PWMB2,0)

def stop():
    set_motor(0,0)

def snack():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(PIN, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(PWMB1, GPIO.OUT)
        GPIO.setup(PWMB2, GPIO.OUT)
        GPIO.setup(D1, GPIO.OUT)
        GPIO.setup(D2, GPIO.OUT)
        p1 = GPIO.PWM(D2, 100)
        p1.start(100)
        time.sleep(1)
        stop()
        forward()
        time.sleep(20)
        stop()
        GPIO.cleanup()
        return "All good. Nom Nom!"
    except Exception as e:
        return u"Error: {0} Check Cat Cam if feeding was done.".format(e)

if __name__ == "__main__":
    print(snack())


