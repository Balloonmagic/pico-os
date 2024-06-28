#loading message
print("loading..........")
#requried packages
print("loading requiured packages")
import machine
print("machine loaded")
import os
import sys
print("os and sys loaded")
import time as ti
print("time loaded")
#led blink on startup
from machine import Pin, SoftI2C
print("finished loading packages")
led = Pin(25, Pin.OUT)

led.toggle()

ti.sleep(1)

led.toggle()
ti.sleep(2)
start_ready=1

#checking startup

if start_ready == 1:
    print("startup succsesfull hello world")
    
    
else:
    print("startup unsucseful shutting down in 5 seconds, exit code 1")
    ti.sleep(5)
    sys.exit(1)
    
#cmd while loop
print("/help for help and /exit to exit")
while start_ready == 1:
    cmd=input("OS.py:")

    
    if cmd == "/help":
        
        print("/blink - blinks the led once , /toggle - turns the led on and off , /scan - scans for i2c devices , /help - list commands , /exit - exits the os")
        
        
    elif cmd == "/exit":
        print("exiting")
        sys.exit(0)
       
    elif cmd == "/blink":
        led.toggle()
        ti.sleep(1)
        led.toggle()
        
    elif cmd == "/toggle":
        led.toggle()
        
        
        
    #scanner i2c
    elif cmd == "/scan":
        print("scanning...")
        i2c = SoftI2C(scl=Pin(1,5), sda=Pin(1,4))

        print('I2C SCANNER')
        devices = i2c.scan()

        if len(devices) == 0:
          print("No i2c device found.")
        else:
          print('i2c devices found:', len(devices))

          for device in devices:
            print("I2C hexadecimal address: ", hex(device))
        
        
        
        
        
    

        
                
                
