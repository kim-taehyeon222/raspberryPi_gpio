# DOMINO

## 영상링크
https://youtu.be/iARiDyatvzQ

## 과제 설명
![image](https://github.com/user-attachments/assets/d8e6c858-66ed-4842-bc60-9e593b28cdf2)


## 회로
![domi](https://github.com/user-attachments/assets/05af6732-84de-47c7-99c0-d49fb588354d)


## 코드

```bash
#!/bin/bash

pin=18

pinctrl set 18 op
pinctrl set 19 op
pinctrl set 20 op
pinctrl set 21 op


while true; do
  if [ $pin -eq 22 ]; then
    pin=18
    sleep 1
    continue
  fi
  pinctrl set $pin dh
  sleep 1
  pinctrl set $pin dl
  pin=$((pin + 1))
done
```
