# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s =int(input("Введите журавликов"))

p = s / 6
s = p
k = (s + p) * 2
print(p, s , k)

# s = int(input("Сколько журавликов сделали дети?"))
# kat = (s / 6) * 4
# pet = s / 6
# ser = s / 6
# print(kat, pet, ser)