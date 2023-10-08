#связь между view и db
from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
           add_info(get_info())
        if ans == 2:
            har=search()
            get_info(har)
        if ans == 3:
            file="text.txt"
            f_name = change_info()
            s_name = input("Введите новое имя контакта: ")
            rename(file,f_name,s_name)
        if ans == 4:
            delete_info(del_name())
        if ans == 5:
            print(book_view())
        if ans == 6:
            break
           


main()