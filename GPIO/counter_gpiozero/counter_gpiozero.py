from gpiozero import LEDBoard, Button
from time import sleep

leds = LEDBoard(18, 19, 20, 21)
button = Button(25)

cnt = 0

def counter(num):

  leds.off()    

  if (num & 8): leds[0].on()
  if (num & 4): leds[1].on()
  if (num & 2): leds[2].on()
  if (num & 1): leds[3].on()


while True:
  if (cnt > 15): cnt = 0

  if button.is_pressed:
    sleep(0.3)
    counter(cnt)
    print(cnt)
    cnt += 1

    