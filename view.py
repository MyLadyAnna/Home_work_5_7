commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def menu():
    print()
    print('Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    print()
    choice = input('Выберите пункт меню: ')
    return choice

def text_save():
    print()
    print('Файл сохранён')
    print()

def show_contacts(phone_list: list):
    if len (phone_list) < 1:
       print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')

def creat_new_contact():
    name = input('Введите ИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    print()
    return name, phone, comment

def del_contact():
    cont_for_del = input('Введите контакт, который необходимо удалить: ')
    return cont_for_del

def delete_conform(contact: str):
    result = input(f'Вы действительно хотите удалить контакт {contact}? (Yes or No)').lower()
    if result == 'Yes':
        return True
    else:
        return False

def successfull_deleted():
    print()
    print('Контакт успешно удалён.')
    print()

def empty_request():
    print('Контакт не найден')

def many_request():
    print('Введите более точный данные. Найдено более 1 контакта.')

def change_contact():
    cont_for_change =  input('Введите контакт, который хотите изменить: ')
    return cont_for_change

def new_data_for_cont():
    print('Введите новые данные. Если информация остаётся без изменений нажминте Enter.')
    name = input('Введите ИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def successfull_change():
    print()
    print('Контакт успешно изменён.')
    print()

def find_contact():
    find = input ('Ввведите искомый элемент')
    return find

def input_error():
    print()
    print('Ошибка ввода! Введите корректный пункт меню')
    print()

def exit():
    print()
    print('Выход из програмы совершён. До встречи!')
    print()