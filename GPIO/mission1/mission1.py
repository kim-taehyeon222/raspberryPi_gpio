
from gpiozero import LEDBoard, Button
from time import sleep

leds = LEDBoard(18, 19, 20, 21)
button = Button(25)

while True:
  if button.is_pressed:
    leds.on()
    
  else:
    leds.off()
