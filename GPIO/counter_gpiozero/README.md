## 영상 링크
https://youtu.be/-BAtlQOke2w

## 과제 설명

![image](https://github.com/user-attachments/assets/9ba4a49a-aa84-4beb-bb9c-99aba5e74bd3)

## 회로사진

![count](https://github.com/user-attachments/assets/d36faf96-9fa5-49bc-b086-6aeffa93d401)

## 코드

```bash
#!/bin/bash
pin1=18
pin2=19
pin3=20

pinctrl set $pin1 op
pinctrl set $pin2 op
pinctrl set $pin3 op


while true; do
  for i in $(seq 0 7); do
    firstLed=$(((i & 4) >> 2))
    secondLed=$(((i & 2) >> 1))
    thirdLed=$((i & 1))

    if (($firstLed)); then
        pinctrl set "$pin1" dh
    fi
    if (($secondLed)); then
       pinctrl set "$pin2" dh

    fi
    if (($thirdLed)); then
        pinctrl set "$pin3" dh
    fi
    printf "%d %d %d\n" ${firstLed} ${secondLed} ${thirdLed}

    sleep 1

    pinctrl set "$pin1" dl
    pinctrl set "$pin2" dl
    pinctrl set "$pin3" dl
  done
done
```
