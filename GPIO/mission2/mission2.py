from gpiozero import LEDBoard, Button
from time import sleep

leds = LEDBoard(18, 19, 20, 21)
button = Button(25)

isLedOn = False

while True:
  if button.is_pressed:
    sleep(0.3)    
    if not isLedOn:
      leds.on()
      isLedOn = True
    else:
      leds.off()
      isLedOn = False
