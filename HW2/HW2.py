# #Task 10
# n = int(input())

# #1 - решка
# #0 - герб

# количество_решек = 0
# количество_гербов = 0

# for i in range(n):
#     состояние = int(input())
#     if состояние == 0:
#         количество_решек += 1
#     else:
#         количество_гербов += 1

# мин_переворотов = min(количество_решек, количество_гербов)

# print(мин_переворотов)

# # Task 12

# S = int(input('S = '))
# P = int(input('P = '))

# for X in range(1, 1001):
#     for Y in range(1, 1001):
#         if X + Y == S and X * Y == P:
#             print(X, Y)
#             exit()
# print("Нет решения")

# #Task 14

# N = int(input("N = "))
# power_of_two = 1

# while power_of_two <= N:
#     print(power_of_two)
#     power_of_two *= 2

k = 'ноутбук'
k = k.upper()


print(k)