#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input("Введите кол-во элементов: "))
list_1 = []
for i in range(1,n + 1):
    list_1.append(i)
print(list_1)   
m = int(input("Введите число для проверки кол-ва в массиве: ") )
count = 0

for i in range(len(list_1)):
    if m == list_1[i]:
        count += 1

print(count)
