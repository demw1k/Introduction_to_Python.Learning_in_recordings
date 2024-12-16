# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# stroka = input()
# print(stroka)
# stroka = stroka.split()
# print(stroka)

stroka = input().split()
res = {}

for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end=' ')
    else:
        print(i, end=' ')

    res[i] = res.get(i , 0)
    print(res)    