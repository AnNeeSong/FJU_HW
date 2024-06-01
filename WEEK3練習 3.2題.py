2. 九九乘法表
不換行列印的方法：  `print(x, end='')`

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i}*{j}={i*j}\t', end='')
    print()
