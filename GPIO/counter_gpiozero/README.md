## 영상 링크
[https://youtu.be/-BAtlQOke2w](https://youtu.be/4tV-Uigef2o)

## 과제 설명

![image](https://github.com/user-attachments/assets/9ba4a49a-aa84-4beb-bb9c-99aba5e74bd3)

## 회로사진

![count](https://github.com/user-attachments/assets/d36faf96-9fa5-49bc-b086-6aeffa93d401)

## 코드

```python
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

    
```
