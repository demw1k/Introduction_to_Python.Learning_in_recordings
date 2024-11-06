#Задача из ПРЕЗЕНТАЦИИ
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list1 = list(input("Введите последовательность: "))
print(list1)
print("Введите число сдвига: ")
k = int(input())
list_res = []
k = k -1

for i in range(k):
    list_res.append(list1[len(list1) - k + i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])   
print(list_res)
   

#Задача из видео семинара - УСЛОВИЯ ОТВЕТА РАЗНЫЕ

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

# list1 = list(input("Введите последовательность: "))
# print(list1)
# print("Введите число сдвига: ")
# k = int(input())
# list_res = []

# for i in range(k):
#     list_res.append(list1[len(list1) - k + i])
# print(list_res)

# for i in range(len(list1) - k):
#     list_res.append(list1[i])   
# print(list_res)
