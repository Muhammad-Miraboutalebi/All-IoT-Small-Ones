#importing
from machine import Pin,ADC
from time import sleep
#binding the LEDs
redLed = Pin (2 , Pin.OUT)
yellowLed = Pin (4 , Pin.OUT)
greenLed = Pin (16 , Pin.OUT)
#turn-off
redLed.off()
yellowLed.off()
greenLed.off()
#use the sensor
yl69 = ADC(0)
#set the light rates
while True:
  #read and print the sensor info
  print(yl69.read())
  a=yl69.read()
  #some Ifs
  if a >= 1000:
     redLed.on()
  elif a >= 600:
      yellowLed.on()
  else:
      greenLed.on()
  #a sleep for rest
  sleep(1)
  #reset
  redLed.off()
  yellowLed.off()
  greenLed.off()
