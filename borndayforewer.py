"""
(МОДУЛЬ 5) В проекте создать новый модуль borndayforewer.py
13.Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:
Просим пользователя ввести год рождения А.С. Пушкина до тех пор пока он не ввел правильный год,
после этого спрашиваем день рождения до тех пор, пока он не ввел верный день.
После верного ответа выводим в терминал 'Верно' и выходим из программы
"""

pyshkin_berth_year = 1977
answer_year = ''
while answer_year != pyshkin_berth_year:
       answer_year = (int(input('В каком году родился А.С. Пушкин?')))
       if answer_year == pyshkin_berth_year:
              break
       print('Неверно')

pyshkin_berth_day = 10
answer_day = ''
while answer_day != pyshkin_berth_day:
        answer_day = int(input('Какого числа родился А.С. Пушкин?'))
        if answer_day == pyshkin_berth_day:
            break
        print('Неверно')
print('Верно')