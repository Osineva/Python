# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# stroka = 'a a a b c a a d c d d'
# stroka_2 = stroka.split(' ')
# slovar = dict()
# for i in stroka_2:
#     if i in slovar:
#         slovar[i]+=1 #увеличили значение на 1
#         print(f'{i}_{slovar[i]}',end=' ')
#     else:
#         slovar[i] =0
#         print(i,end=' ')
    

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = 'She sells sea shells on the sea shore The shells '\
# 'that she sells are sea shells I"m sure.So if she sells sea '\
# 'shells on the sea shore I"m sure that the shells are sea '\
# 'shore shells '

# text.replace('.',' ').lower() #замена значений и смена регистра
# print(text)
# text_red = text.split(' ') #разделили предложения по словам
# text_res = set(text_red) #создали множества
# print(text_res)
# print(len(text_res))#посчитали кол-во различных слов


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# max = -1
# while True:
#     number=int(input())
#     if number > 0:
#         max=number
#     if number == 0:
#         break
# print(max)


# Удаление дубликатов
# Напишите программу, которая выполняет "сжатие массива" – заполняет все копии уже ранее встречавшихся элементов нулями и переставляет все нулевые элементы в конец массива. При этом все оставшиеся элементы располагаются в начале массива в том же порядке, что и в исходном массиве.

# Входные данные
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. Гарантируется, что 0 < N ≤ 10000 .

# Выходные данные
# Программа должна вывести в одну строчку все элементы получившегося массива, разделив их пробелами.

# Примеры
# входные данные
# 6
# 0 1 2 1 2 3
# выходные данные
# 1 2 3 0 0 0

# numbers = list(map(int, input().split(' ')))

# # for i in range(len(numbers)):
# # numbers[i] = int(numbers[i])

# numbers_dup = list(set(numbers))

# if 0 in numbers_dup:
#     numbers_dup.remove(0)
# # numbers_dup.append(0)


# for i in range(len(numbers) - len(numbers_dup)):
#     numbers_dup.append(0)

# print(*numbers_dup)

# Напишите программу, которая отделяет положительные элементы массива от отрицательных: переставляет все положительные (в том же порядке) в начало массива, а все отрицательные (в том же порядке) – в конец массива, все нулевые элементы должны оказаться в середине массива.

# Входные данные
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. Гарантируется, что 0 < N ≤ 10000 .

# Выходные данные
# Программа должна вывести в одну строчку все элементы получившегося массива, разделив их пробелами.

# Примеры
# входные данные
# 6
# 1 -1 2 -2 0 3
# выходные данные
# 1 2 3 0 -1 -2

# import os
# clear = lambda: os.system('cls')
# clear()

# numbers = list(map(int, input().split()))

# numbers_negative = []

# count = 0

# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] < 0:
#         numbers_negative.append(numbers.pop(i))
#     if numbers[i] == 0:
#         numbers.pop(i)
#         count +=1

# print(numbers)

# numbers_negative.reverse()

# numbers += [0*count] + numbers_negative

# print(numbers)




