import RPi.GPIO as GPIO                       #Import GPIO library

import time                                   #Import time library

GPIO.setmode(GPIO.BOARD)                      #Set GPIO pin numbering

pir = 7                                    #Associate pin 7 to pir

GPIO.setup(pir, GPIO.IN)                      #Set pin as GPIO in 

def button_callback(channel):
    print("Button was pushed!")

print ("Waiting for sensor to settle")

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback)

time.sleep(2)                   #Waiting 2 seconds for the sensor to initiate

print ("Detecting motion")

while True:

    # if GPIO.input(pir):             #Check whether pir is HIGH

    #     print ("Motion Detected!")

    #      #D1- Delay to avoid multiple detection

    time.sleep(0.1)  #While loop delay should be less than detection delay