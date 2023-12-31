﻿from logger import input_note, print_note, filter_note, change_note, delete_note

def interface():
    while True:
        print('''Выберите режим работы с программой
                1 - Создать новую заметку
                2 - Показать все заметки
                3 - Показать заметки по заданным параметрам
                4 - Внести изменения в заметку
                5 - Удалить заметку
                6 - Выход
                ''')
        comand = input('Введите команду: ')
        if comand == '1':
            input_note()
        elif comand == '2':
            print_note()
        elif comand == '3':
            print('Введите параметры поиска через ";". Для поиска по дате вводите в формате dd-mm-yyyy: ')
            filterString = input()
            filter_note(filterString)
        elif comand == '4':
            change_note()
        elif comand == '5':
            delete_note()
        elif comand == '6':
            break
        else:
            print('Введите корректную комманду')