# Задача 2: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# x + y = S
#   x * y = P
#   x = S - y (S-y)*(y)== P

S = int(input('Введите  сумму чисел: '))
P = int(input('Введите произведение чисел: '))
c = 0
for x in range (0, 1000):
    if c: break
    for y in range (0, 1000):
        if x + y == S and x * y == P:
            c = 1
            print(x)
            print(y)
            break
else:
    print('Ошибка.Введите другие числа! ')  