# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

#First

list_1 = list(input("Введите массив: "))
print(list_1)
count = 0

for i in range(1,len(list_1)):
    if list_1[i] > list_1 [i -1]:
        count += 1
print(count)     

#Second

# list_1 = [0, -1, 5, 2, 3]
# print(list_1)
# count = 0

# for i in range(1,len(list_1)):
#     if list_1[i] > list_1 [i -1]:
#         count += 1
# print(count)  