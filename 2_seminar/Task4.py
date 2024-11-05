# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

#First

# allarbuz = int(input())
# arbuzmin = 0
# arbuzmax = 0
# for i in range(allarbuz):
#     print("Введите вес арбуза")
#     weight = int(input())
#     arbuzmin1 = weight
#     if weight > arbuzmax:
#         arbuzmax = weight
    
#     if arbuzmin == 0 :        
#         arbuzmin = arbuzmin1
#     elif arbuzmin > weight:
#         arbuzmin = weight
    
# print(arbuzmin, " - этот теще", arbuzmax, "- а этот нам =)")            

#Second

n = int(input())
max = -1
min = 30001
for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x

print(min,max)