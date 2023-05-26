"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

1. Открыть файл (есть)
2. Сохранить файл (есть)
3. Показать тк (есть)

5. Найти контакт (есть)
6. Изменить контакт (есть)
7. Удалить контакт
8. Выход из программы (есть)
"""
import json
import os

# data = {'id': {'name': '', 'phone': ''}}

data = {}
menu = {'1': 'Открыть файл', 
        '2': 'Сохранить файл', 
        '3': 'Показать тк', 
        '4': 'Добавить контакт',
        '5': 'Найти контакт',
        '6': 'Изменить контакт',
        '7': 'Удалить контакт',
        '8': 'Выход из программы'}

def addContact():
    contact_id = max(data.keys()) + 1 if len(data) > 0 else 1
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    data[contact_id] = {'name': name, 'phone': phone} 

def saveContact(data):
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        write_file.write(json.dumps(data)) # сбрасывает данные в файл

def readContact():
    with open("data_file.json", "r", encoding='utf-8') as read_file:
        temp = json.loads(read_file.read())
    for key, value in temp.items():
        data[int(key)] = value
    return data

def changeContact():
    print(data)
    id_contact = int(input('Какой id контакта поменять? '))
    print(data[id_contact])
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    if len(name) > 0:
        data[id_contact]['name'] = name
    if len(phone) > 0:
        data[id_contact]['phone'] = phone

def findContact():
    command = int(input('Меню: \n1. Искать по id \n2. Искать по имени \n3. Искать по телефону \n:'))
    match command:
        case 1: 
            print(data[int(input('Введите id: '))])
        case 2:
            fn = input('Введите имя: ').lower()
            for key, values in data.items():
                if values['name'].lower().find(fn) != -1:
                    print(key, values)
        case 3:
            fn = input('Введите номер телефона: ')
            for key, values in data.items():
                if values['phone'].find(fn) != -1:
                    print(key, values)            
                    
# def deleteContact():

def menuContacts(menu):
    for key, item in menu.items():
        print(key, item)

comand = 0
data = readContact()
while comand != 8:
    print('--------')
    menuContacts(menu)
    comand = int(input('Введите команду: '))
    match comand:
        case 1: 
            data = readContact()
        case 2:
            saveContact(data)
        case 3: 
            print(data) # сделать отдельную ф-цию
        case 4:
            addContact()
            saveContact(data)
        case 5:
            findContact()
        case 6:
            changeContact()
            saveContact(data)
        case 7:
            pass # удалить контакт
        case 8:
            break
