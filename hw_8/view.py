
def employee_to_s():
    return input('Введите информацию для поиска: ')
    

def choose_mode():
    return input('Введите режим работ (1-добавление, 2- поиск, \
        3 - изменить, 4 - удалить) : ')


def new_employee():
    name = input('Введите имя: ')
    post = input('Введите должность: ')
    salary = input('Введите зарплату: ')
    phone_num = input('введите номер: ')
    return f'{name} || {post} || {salary} || {phone_num}'

def show_found(result):
    print('результаты поиска : ')
    for i in result:
        print(i)

def clairification():
    return input("Введите id: ")

def error():
    print('Введено некорректное значение')


# def contact_to_s():
#     return input('Введите информацию для поиска: ')

# def choose_mode():
#     return input('Введите режим работ (1 - добавление, 2 - поиск, 0 - выход): ')

# def new_contact():
#     name = input('Введите имя: ')
#     phone_num = input('Введите номер: ')
#     return f'{name} || {phone_num}'

# def show_found(result):
#     print('Результат поиска: ')
#     for i in result:
#         print(i)