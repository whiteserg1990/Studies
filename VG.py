import datetime
#Как проверить високосный ли год?
'''
Стандартный год состоит из 365 дней, а високосный из 366 дней.

Правила определения:
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400.
Иными словами, если год делится на 4 без остатка, но делится на 100 только с остатком,
то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный.
'''
current_date = datetime.date.today()
year = current_date.year                # проверяемая переменная
'''Задание 1. Проверка с условиями if-else

'''
year = 2024

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

print(f"{year} год — високосный" if is_leap else f"{year} год — невисокосный")




'''Задание 2. Проверка с дополнительными условиями elif
'''
year = 2023

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

print(f"{year} год — високосный" if is_leap else f"{year} год — невисокосный")


'''Задание 3. Проверка с помощью логических операторов в одну строку if
'''
year = 2025

print(f"{year} год — високосный" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else f"{year} год — невисокосный")


'''Задание 4. Проверка с применением специальной функции модуля calendar
Найдите ее самостоятельно....
'''
import calendar

year = 2026

if calendar.isleap(year):
    print(f"{year} год - високосный")
else:
    print(f"{year} год - невисокосный")


