# MISSION2

## 영상링크
[https://youtu.be/pSx9a5qAqPE](https://youtu.be/DCULCoJIndA)

## 회로

![KakaoTalk_20250423_001833586](https://github.com/user-attachments/assets/f081863c-eb1c-4c79-afcb-7154b1c9baa2)



## 코드

```python

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


```
