# #Task 22
# def common_elements(n, m, set1, set2):

#     set1 = set(set1)
#     set2 = set(set2)
 
#     common = set1.intersection(set2)

#     result = sorted(list(common))
    
#     return result

# n = int(input("n = "))
# m = int(input("m = "))

# set1 = []
# set2 = []

# print("set1: ")
# for i in range(n):
#     element = int(input())
#     set1.append(element)

# print("set2: ")
# for i in range(m):
#     element = int(input())
#     set2.append(element)


# result = common_elements(n, m, set1, set2)
# print(result)




# #Task 24

# def max_berry_harvest(berry_counts):
#     n = len(berry_counts)
#     max_harvest = 0

#     for i in range(n):
        
#         harvest = berry_counts[i] + berry_counts[(i + 1) % n] + berry_counts[(i - 1) % n]
#         max_harvest = max(max_harvest, harvest)

#     return max_harvest

# n = int(input("Количество кустов черники: "))
# print("Количество ягод на каждом кусте черники:")
# berry_counts = [int(input()) for _ in range(n)]

# result = max_berry_harvest(berry_counts)
# print(result)