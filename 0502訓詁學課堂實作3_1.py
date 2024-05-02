# -*- coding: utf-8 -*-
"""0502訓詁學課堂實作3-1
## 課堂練習

1. 寫程式計算 1 ~ 100 中的所有奇數和
- 寫法1

x = sum(range(1, 101, 2))
print(x)

- 寫法2
sum = 0
for x in range(1,101):
    if x % 2 != 0:
        sum = sum + x
print(sum)

- 寫法3
sum = 0
for x in range(1,101):
    if x % 2 == 0:
        continue #continue放棄本次「重複動作」，重新回到迴圈開頭做下一次動作。
    sum = sum + x
print(sum)

- 寫法4
sum = 0
for x in range(1,101,2):
    sum = sum + x

print(sum)