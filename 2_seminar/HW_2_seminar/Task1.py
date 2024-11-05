# Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

print("Введите кол-во монеток")
n = int(input())
orel = 0
orelcount = 0
reshkacount = 0


for i in range(n):
    print("Какой стороной лежит монета? 1 - орел, 0 - решка")
    storona = int(input())
    if storona == orel:
        orelcount += 1
    else:    
        reshkacount += 1


if orelcount <= reshkacount:
    print(orelcount)
else:
    print(reshkacount)    