# 1) Имеется список чисел numbers, который содержит значения от 1 до 100.
# 2) Вам нужно создать новый список squared_numbers, в который войдут квадраты всех четных чисел из numbers.
# 3) Затем создайте список cubed_numbers, содержащий кубы всех чисел из squared_numbers, которые делятся на 3.
# 4) Вывести сумму всех чисел из cubed_numbers.


numbers = list(range(1,101))
squared_numbers = []
for number in numbers:
    if number % 2 == 0;
        # squared_numbers.append(number ** 2) Это первый вариант решения " в лоб"


# squared_numbers = [ number ** 2 for number in numbers if number % 2 == 0 ]   Это второй вариант решения    "лист комплихеншн"

squared_numbers = list(map(lambda result: result** 2, filter(lambda number: number % 2 == 0, numbers))) Это решение через высшие функции
