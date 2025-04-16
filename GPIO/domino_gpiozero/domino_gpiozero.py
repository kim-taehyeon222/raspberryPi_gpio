from gpiozero import LEDBoard, Button
from time import sleep

leds = LEDBoard(18, 19, 20, 21)
button = Button(25)

def domino():
  for led in leds:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

while True:
  if button.is_pressed:
    domino()
  