with open('L:\\1\\dataset_3363_4 (4).txt', 'r') as file:
    arr = []
    for line in file:
        if line not in arr:
            arr.append(line.strip())

arr = str(arr).replace(";", ",")
print(arr)
#[print(el) for el in arr]

sumMiddle = 0
for el in arr:
    sumMiddle = (el[1] + el[2] + el[3]) / 3
    print(round(sumMiddle,9))

sumL = 0
sumM = 0
sumH = 0

for el in arr:
    sumL += el[1]
    sumH += el[2]
    sumM += el[3]
sumL /= len(arr)
sumM /= len(arr)
sumH /= len(arr)
print(round(sumL,9), round(sumM,9), round(sumH,9))