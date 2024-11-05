# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# Мое решение

# n = int(input("Введите число n: "))
# fact = 1
# count = 2
# while count <= n :
#     fact = fact * count
#     count += 1
# print(fact)  
# 
# Препод  

n = int(input())
i = 1
result = 1
while i <= n:
    result*= i
    i += 1
print(result)    