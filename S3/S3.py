# Найти кол-во уникальных значений в списке
# a = [1,1,2,0,-1,3,4,4]
# b=set(a)
# print (len(b))
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
    
# print(b)

# # Переписать порядок чисел в массиве (сдвинуть вправо)
# a = [1,2,3,4,5]
# b=a.copy()
# k=2
# for i in range(len(a)):
#     if i +k <len(a):
#          a[i]= b[i-k] # "-" сдвинет вправо, "+" влево
#     else:
#          a[i] = b[i-k-len(a)]
# print(a)


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

a=[{"V": "S001"}, 
   {"V": "S002"}, 
   {"VI": "S001"},
    {"VI": "S005"}, 
    {"VII": " S005 "}, 
    {" V ":" S009 "}, 
    {" VIII ":" S007 "}]

b = set()

for i in a:
    for j in i.values():
        b.add(j.strip())

print(b)
