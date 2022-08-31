with open('L:\\1\\dataset_3380_6.txt', 'r') as file:
    lst = []
    for line in file:
        if line not in lst:
            lst.append(line.split())
print(lst)

dic1 = {}

#lsl = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
#for i in lsl:
#    print(i)
#    if i not in dic1.items():
#        dic1[i] = '-'
#print(dic1)

#dicn = {i:'-' for i in range(1,12)}
#print(dicn)

cs1 = 0
num1 = 0
for i in lst:
    for j in lst:
        if int(j[0]) == 1:

            cs1 += 1
            num1 += float(j[2])
            med = num1 / cs1
            dic1[int(j[0])] = int(med)

cs2 = 0
num2 = 0
for j in lst:
        if int(j[0]) == 2:
            cs2 += 1
            num2 += float(j[2])
            med = num2 / cs2
            dic1[int(j[0])] = med

cs3 = 0
num3 = 0
for j in lst:
        if int(j[0]) == 3:
            cs3 += 1
            num3 += float(j[2])
            med = num3 / cs3
            dic1[int(j[0])] = med

cs4 = 0
num4 = 0
for j in lst:
        if int(j[0]) == 4:
            cs4 += 1
            num4 += float(j[2])
            med = num4 / cs4
            dic1[int(j[0])] = med

cs5 = 0
num5 = 0
for j in lst:
        if int(j[0]) == 5:
            cs5 += 1
            num5 += float(j[2])
            med = num5 / cs5
            dic1[int(j[0])] = med

cs6 = 0
num6 = 0
for j in lst:
        if int(j[0]) == 6:
            cs6 += 1
            num6 += float(j[2])
            med = num6 / cs6
            dic1[int(j[0])] = med

cs7 = 0
num7 = 0
for j in lst:
        if int(j[0]) == 7:
            cs7 += 1
            num7 += float(j[2])
            med = num7 / cs7
            dic1[int(j[0])] = med

cs8 = 0
num8 = 0
for j in lst:
        if int(j[0]) == 8:
            cs8 += 1
            num8 += float(j[2])
            med = num8 / cs8
            dic1[int(j[0])] = med

cs9 = 0
num9 = 0
for j in lst:
        if int(j[0]) == 9:
            cs9 += 1
            num9 += float(j[2])
            med = num9 / cs9
            dic1[int(j[0])] = med

cs10 = 0
num10 = 0
for j in lst:
        if int(j[0]) == 10:
            cs10 += 1
            num10 += float(j[2])
            med = num10 / cs10
            dic1[int(j[0])] = med

cs11 = 0
num11 = 0
for j in lst:
        if int(j[0]) == 11:
            cs11 += 1
            num11 += float(j[2])
            med = num11 / cs11
            dic1[int(j[0])] = med

#print(dic1)

#print(sorted(dic1))

#sort_t = sorted(dic1.items(), key=lambda x: x[0])
#dict(sort_t)
#print(dict(sort_t))

#for key, value in dic1.items():
#       print(sorted(int(key), value))

#print("The original dictionary: ", dic1)

#sorting by key
#a = dict(sorted(dic1.items(), key=lambda x: int(x[0])))

#print("After sorting by key: ", a)