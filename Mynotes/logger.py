import os
import datetime
from note_create import title, note_text

filename = 'Mynotes\\notes.csv'
def print_note():    
    if os.path.exists(filename):
        print('\nВывод данных из файла: ')
        with open(filename, 'r', encoding = 'utf-8') as file:
            list_note = file.readlines()
            for el in list_note:
                print(el, end="")
    else:
        print('Файла не существует')

def input_note():
    print('Введите данные для записи в файл: ')
    name = title()
    note = note_text()
    with open(filename, 'r', encoding = 'utf-8') as file:
        if os.stat(filename).st_size != 0:
            lines = file.readlines()            
            id = int(len(lines))
            with open(filename, 'a', encoding = 'utf-8') as file:
                id+=1
                file.write(f'{id}; {name}; {note}; {datenote}\n')        
        else:
            with open(filename, 'a', encoding = 'utf-8') as file:
                id = 1
                file.write(f'{id}; {name}; {note}; {datenote}\n')
        print('Заметка успешно сохранена')

def filter_note(filter_string):
    with open(filename, 'r', encoding = 'utf-8') as file:
        listNote = file.readlines()
        listFilter = filter_string.split(';')       
        is_found = False
        for el in listNote:
            count = 0
            temprecord = el.split(';')
            for record in temprecord:
                for elFilter in listFilter:
                    if elFilter.lower() in record.lower() and len(elFilter.lower().strip()) == len(record.lower().strip()):
                        count += 1
            if count == len(listFilter):
                is_found = True
                print(el)
        if not is_found:
            print('Таких записей не найдено')

def change_note():
    with open(filename, 'r', encoding = 'utf-8') as file:
        findedString = file.readlines()
        index = 1
        for el in findedString:            
            print(f'{index} {el}', end='')
            index +=1
        numString = int(input('Введите номер записи, которую хотите изменить: '))
        if numString-1 in range(len(findedString)):
            print('Введите новые данные: ')
            name = title()
            note = note_text()
            findedString[numString-1] = f'{name}; {note}\n'
            with open(filename, 'w', encoding = 'utf-8') as file:
                file.writelines(findedString)
                print('Изменения успешно сохранены')
        else:
            print('Такой заметки в файле не существует')
    
def delete_note():
    with open(filename, 'r', encoding = 'utf-8') as file:
        deletedString = file.readlines()
        for el in deletedString:            
            print(f'{el}', end='')
        numString = int(input('\nВведите id заметки, которую хотите удалить: '))
    if numString-1 in range(len(deletedString)):
        with open(filename, 'w', encoding = 'utf-8') as file:        
            del deletedString[numString-1]
            file.writelines(deletedString)
            print('Заметка успешно удалена')
    else:
        print('Такой заметки в файле не существует')