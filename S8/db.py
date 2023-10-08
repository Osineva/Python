#функции для работы с базой данных
def add_info(arg):
    with open("text.txt","a", encoding="utf-8") as file:
        file.write(f"{arg}\n") 


def search_info(arg):
    with open("text.txt","r", encoding="utf-8") as file:
        lst = file.readlines()
        res=[]
        count=1
        for i in range(len(lst)):
            if arg in lst[i]:
                res.append(lst[i])
                print(f'{count},{lst[i]}')
                count +=1
        return res
    
def book_view():
    with open("text.txt","r", encoding="utf-8") as file:
        return file.read()
    
def delete_info(del_file, del_name):
    del_file = "text.txt"
    with open("text.txt","r", encoding="utf-8") as file, open("temp.txt","w", encoding="utf-8") as file_1:
        str = file.readline()
        while str:
            name = str.strip().split(',')
            if name != del_name:
                file_1.write(str)
            str=file.readline()
    import os
    os.remove(del_file)
    os.rename("temp.txt", del_file)

def rename(file, f_name, s_name):
    with open("text.txt","r", encoding="utf-8") as file, open("temp.txt","w", encoding="utf-8") as file_1:
        for str in file:
            name, number = str.strip().split(",")
            if name==f_name:
                file_1.write(str)
    import os
    os.remove(file)
    os.rename("temp.txt",file)
