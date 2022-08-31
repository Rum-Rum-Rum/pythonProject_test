from datetime import datetime
import random
start = datetime.now()
err = 0
for i in range(0, 100):
    action = random.randint(1, 3)
    if action == 1:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        ex = f'{a}*{b}'
        ans = a * b
    if action == 2:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        if b > a:
            t = a
            a = b
            b = t
        ex = f'{a}-{b}'
        ans = a - b
    if action == 3:
        a = random.randint(0, 20)
        b = random.randint(0, 10)
        ex = f'{a}+{b}'
        ans = a + b
    while True:
        try:
            answer = int(input(f"{i+1}: {ex}= "))
        except ValueError:
            print('Введите число')
        else:
            break
    if int(answer) != ans:
        err = err + 1
    print(int(answer), int(answer) == ans)
stop = datetime.now()
print(f'----------------------------')
print(f'Oшибок:{err}')
# Кол-во времени между датами.
delta = stop - start
timedelta_seconds = delta.total_seconds()
print('Время выполнения:', str(timedelta_seconds).split(".")[0], 'Сек.')