3. 某班學生人數不詳，欲輸入每一個學生成績，當輸入 -1 時表示結束輸入，然後顯示出全班人數、及格人數、不及格人數、以及全班平均值。

scores = []
total_students = 0
pass_count = 0
fail_count = 0

print("請輸入每個學生的成績（輸入 -1 結束）：")

while True:
    score = float(input("請輸入成績: "))
    if score == -1:
        break
    scores.append(score)
    total_students += 1
    if score >= 60:
        pass_count += 1
    else:
        fail_count += 1

if total_students > 0:
    average_score = sum(scores) / total_students
else:
    average_score = 0

print(f"全班人數: {total_students}")
print(f"及格人數: {pass_count}")
print(f"不及格人數: {fail_count}")
print(f"全班平均值: {average_score:.2f}")
