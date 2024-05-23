"""0523訓詁學課堂實作4.11習題
## 課堂練習

1. 請撰寫一個程式，呼叫一個自訂的函式 `f(x, n)`，計算一個整數 `x` 的 `n` 次方

def f(x, n):
    return x ** n

x = int(input("請輸入任一整數: "))
n = int(input("請輸入任一整數: "))

result = f(x, n)
print(f"{x} 的 {n} 次方是 {result}")