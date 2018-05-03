import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer

def cleanAndExit():
    GPIO.cleanup()
    sys.exit()

hx = HX711(5, 6)
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(-7)
hx.reset()
hx.tare()
GPIO.output(24,True)
while True:
    try:
        
        val = hx.get_weight(5)
        print("Weight on mat:")
        print (val)
        hx.power_down()
        hx.power_up()
        time.sleep(0.5)
            
        time.sleep(2) # to stabilize PIR sensor
        
        if GPIO.input(23):
            sen_pir= True
            time.sleep(5)
            
        if val > -20000:
            sen_load = True
            print("Have a good day!")
            print("Hey! You got up!! GOOD MORNING ^.^ ")
            time.sleep(5)
            
        
            if sen_pir is True and sen_load is True:
                time.sleep(0.5)
                GPIO.output(24,False)
                sys.exit()
            
        else:
            time.sleep(0.5)
                #GPIO.output(24,True)
        time.sleep(0.1)
        
    
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


