# В базе магазина электроники есть список видеокарт компании NVIDIA разных
# поколений. Вместо полных названий хранятся только числа, которые обозначают
# модель и поколение видеокарты. Недавно компания выпустила новую линейку
# видеокарт. Самые старшие поколения разобрали за пару дней.
# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.
# Пример:
# Количество видеокарт: 5
# Видеокарта 1: 3070
# Видеокарта 2: 2060
# Видеокарта 3: 3090
# Видеокарта 4: 3070
# Видеокарта 5: 3090
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]

# n = int(input("Введите кол-во видеокарт: "))

# list1 = []
# list2 = []
# max = 0
# for i in range(n):
#     list1.append(int(input("Введите номер видеокарты: ")))
#     if list1[i] > max:
#         max = list1[i]
# print(list1)      
# for i in range(n): 
#     if list1[i] != max:
#         list2.append(list1[i])
# print(list2)        

# Задача 2. Кино
# Илья зашёл на любительский киносайт, на котором пользователи оставляют
# рецензии на фильмы. Их список:
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская
# рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить
# часть фильмов в список любимых, чтобы позже прочитать рецензии на них.
# Напишите программу, в которой пользователь вводит фильм. Если кинокартина
# есть в перечне, то добавляется в список любимых. Если её нет, то выводится
# ошибка. В конце выведите весь список любимых фильмов.
# Пример:
# Сколько фильмов хотите добавить? 3
# Введите название фильма: Леон
# Введите название фильма: Безумный Макс
# Ошибка: фильма Безумный Макс у нас нет :(
# Введите название фильма: Мементо
# Ваш список любимых фильмов: Леон, Мементо

# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# lovefilms = []
# countfilms = int(input("Сколько фильмов вы хотите добавить?: "))

# for i in range(countfilms):
#     n = input("Введите название фильма: ")
#     if n in films:
#         lovefilms.append(n)
#     else:
#         print(f'Ошибка: фильма {n} у нас нет : ( ')
# print(f'\nВаш список любимых фильмов: {lovefilms}')         

# Задача 3. Сортировка
# Дан список из N чисел. Напишите программу, которая сортирует элементы
# списка по возрастанию и выводит их на экран. Дополнительный список
# использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort
# Постарайтесь придумать и написать как можно более эффективный алгоритм
# сортировки.
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]


# list_1 = [1,5,3,-1,9,11,-8]
# print(list_1)

# for i in range(len(list_1) - 1):
#     for j in range(len(list_1) - 1 - i):
#         if list_1[j] > list_1[j + 1]:
#             list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]              

# print(list_1)

# Задача 4. Товары
# В базе данных магазина вся необходимая информация по товарам делится на
# два словаря: первый отвечает за коды товаров, второй — за списки количества
# разнообразных товаров на складе:

# Напишите программу, которая рассчитывает общую стоимость позиций для
# каждого товара на складе и выводит эту информацию на экран.
# Результат работы программы:
# Лампа — 27 штук, стоимость 1134 рубля.
# Стол — 54 штуки, стоимость 27 860 рублей.
# Диван — 3 штуки, стоимость 3550 рублей.
# Стул — 105 штук, стоимость 10 311 рублей.


# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }

# store = {
# '12345': [
# {'quantity': 27, 'price': 42},
# ],
# '23456': [
# {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520},
# ],
# '34567': [
# {'quantity': 2, 'price': 1200},
# {'quantity': 1, 'price': 1150},
# ],
# '45678': [
# {'quantity': 50, 'price': 100},
# {'quantity': 12, 'price': 95},
# {'quantity': 43, 'price': 97},
# ],
# }


# for item_name in goods.keys():
#     item_code = goods[item_name]

#     total_quantity = 0
#     total_cost = 0

#     for entry in store[item_code]:

#         total_quantity += entry['quantity']

#         total_cost += entry['price'] * entry['quantity']

#     print('{} — {} штук, стоимость {} рубля(ей).'.format(item_name,
#     total_quantity, total_cost))

# Задача 5. Пицца
# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и
# сколько заказывал у них в определённый период. Вам нужно структурировать
# эту информацию и определить, сколько всего пицц купил каждый заказчик.
# На вход в программу подаётся N заказов. Каждый заказ представляет собой
# строку вида «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по
# алфавиту. Учитывайте, что один человек может заказать одну и ту же пиццу
# несколько раз.
# Пример
# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
# Иванов:
# Мексиканская: 2
# Мясная: 3
# Пепперони: 3
# Петров:
# Де-Люкс: 2
# Интересная: 5

orders_count = int(input('Введите количество заказов: '))
database = dict()
for i_order in range(orders_count):
    customer, pizza_name, count = input('{} заказ: '.format(i_order+ 1)).split()
    count = int(count)
    if customer not in database:
        database[customer] = {pizza_name: count}
    else:

        if pizza_name in database[customer]:
            database[customer][pizza_name] += count
        else:
            database[customer][pizza_name] = count
for customer in sorted(database.keys()):
    print('{}:'.format(customer))
    for pizza_name in sorted(database[customer].keys()):
        print(' {}: {}'.format(pizza_name,
        database[customer][pizza_name]))