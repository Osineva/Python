#Task 10
n = int(input())

#1 - решка
#0 - герб

количество_решек = 0
количество_гербов = 0

for i in range(n):
    состояние = int(input())
    if состояние == 0:
        количество_решек += 1
    else:
        количество_гербов += 1

мин_переворотов = min(количество_решек, количество_гербов)

print(мин_переворотов)