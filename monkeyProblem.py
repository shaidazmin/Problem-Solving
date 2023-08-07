# from functools import reduce

# n = int(input())

# height = reduce(lambda h, i: h + 3 if i % 2 != 0 else h - 1.2, range(n), 0)

# print(height)
n = int(input())
height = 0.0
for i in range(n):
    if i % 2 != 0:
        height = height + 3
    else:
        height = height - 1.2
print("{:.6f}".format(height))
