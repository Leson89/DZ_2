"""

(МОДУЛЬ 6) В проекте создать новый модуль victory.py
15. Используя любые средства написать программу викторина:
Выбрать минимум 5 известных людей и узнать их год рождения. Программа должна по очереди спрашивать у пользователя год
рождения знаменитости. После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает

пользователя хочет ли он начать игру сначала, если да - то повторяем все сначала, если ответ нет - выходим из программы

- В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости
"""
start_game = 'нет'
answer_player = ''
while answer_player != start_game:
        correct_answer = 0
        wrong_answer = 0

        lomanosov_birthday = 1711
        answer_lomanosov_birthday = int(input('Год рождения М.В. Ломоносова ?'))
            # Правильный ответ 1711
        if answer_lomanosov_birthday == lomanosov_birthday:
            correct_answer += 1
        elif answer_lomanosov_birthday != lomanosov_birthday:
            wrong_answer += 1
            # Правильный ответ 1934
        gagarin_birthday = 1934
        answer_gagarin_birthday = int(input('Год рождения Ю.А. Гагарина ?'))

        if answer_gagarin_birthday == gagarin_birthday:
            correct_answer += 1
        elif answer_gagarin_birthday != gagarin_birthday:
            wrong_answer += 1
            # Правильный ответ 1685
        bah_birthday = 1685
        answer_bah_birthday = int(input('Год рождения И.С. Баха ?'))

        if answer_bah_birthday == bah_birthday:
            correct_answer += 1
        elif answer_bah_birthday != bah_birthday:
            wrong_answer += 1
            # Правильный ответ 1770
        bethoven_birthday = 1770
        answer_bethoven_birthday = int(input('Год рождения Л. ван Бетховена ?'))
        if answer_bethoven_birthday == bethoven_birthday:
            correct_answer += 1
        elif answer_bethoven_birthday != bethoven_birthday:
            wrong_answer += 1
            # Правильный ответ 1814
        lermontov_birthday = 1814
        answer_lermontov_birthday = int(input('Год рождения М.Ю. Лермонтова ?'))
        if answer_lermontov_birthday == lermontov_birthday:
            correct_answer += 1
        elif answer_lermontov_birthday != lermontov_birthday:
            wrong_answer += 1
            # Правильный ответ 1840
        chaikovski_birthday = 1840
        answer_chaikovski_birthday = int(input('Год рождения П.И. Чайковского ?'))
        if answer_chaikovski_birthday == chaikovski_birthday:
            correct_answer += 1
        elif answer_chaikovski_birthday != chaikovski_birthday:
            wrong_answer += 1

        print('Процент правильных ответов:', correct_answer * 100 / 6, '%')
        print('Процент не правильных ответов:', wrong_answer * 100 / 6, "%")
        print('Правильных ответов:', correct_answer)
        print('Неправильных ответов:', wrong_answer)
        answer_player = input('Хотите начать игру заново? да/нет')
        if answer_player == start_game:
            break

























