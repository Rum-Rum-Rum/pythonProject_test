#with open('L:\\1\\dataset_3363_4 (4).txt', 'r') as file:
#    data = []
 #   for line in file:
 #       if line not in data:
 #           data.append(line.strip().split(';'))


#data.pop(-1)
#print(data)
data = [['Петров', 85, 92, 78], ['Сидоров', 100, 88, 94], ['Иванов', 58, 72, 85]]


sumMiddle = 0
for el in data:
    sumMiddle = (int(el[1]) + int(el[2]) + int(el[3])) / 3
print(round(sumMiddle,9))

sumL = 0
sumM = 0
sumH = 0

for el in data:
    sumL += int(el[1])
    sumH += int(el[2])
    sumM += int(el[3])
sumL /= len(data)
sumM /= len(data)
sumH /= len(data)
print(round(sumL,9), round(sumH,9), round(sumM,9),)
