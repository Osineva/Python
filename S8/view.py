#функции для работы с пользователем

def select_op():
    op = int(input('Выберите действие:\n1.Добавить контакт\n2.Показать контакт\n3.Изменить контакт\n'
                   '4.Удалить контакт\n5.Показать все контакты\n6.Выход\n'))
    return op

def get_info():
    name = input("Введите ФИО: \n")
    tel = input("Введите телефон: \n")
    data = name+ " "+tel
    return data
def search():
    return input("Введите ФИО или телефон\n")
def del_name():
    d_name = input("Введите ФИО: \n")
    d_file = "text.txt"
def change_info():
    name = input("Введите ФИО: \n")
    tel = input("Введите телефон: \n")
    data = name+ " "+tel
    return data

    
    
