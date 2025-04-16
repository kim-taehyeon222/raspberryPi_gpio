# DOMINO

## 영상링크
[https://youtu.be/iARiDyatvzQ](https://youtu.be/duDGpxq8KKY)

## 과제 설명
![image](https://github.com/user-attachments/assets/f861db3f-41ae-41a5-b9d8-5762df66d6a2)


## 회로
![domi](https://github.com/user-attachments/assets/05af6732-84de-47c7-99c0-d49fb588354d)


## 코드

```python
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
  
```
