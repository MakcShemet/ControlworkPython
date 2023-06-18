from logger import input_note, print_note, filter_note, change_note, delete_note

def interface():
    print('''Выберите режим работы с программой
                add - Создать новую заметку
                print all - Вывести все заметки
                serch - Найти и показать заметку
                change - Внести изменения в заметку
                del - Удалить заметку
                exit - Выход
                ''')
    comand = input('Введите команду: ')
    if comand == 'add':
        input_note()
    elif comand == 'print all':
        print_note()
    elif comand == 'serch':
        print('Введите параметры поиска через ";": ')
        filterString = input()
        filter_note(filterString)
    elif comand == 'change':
        change_note()
    elif comand == 'del':
        delete_note()