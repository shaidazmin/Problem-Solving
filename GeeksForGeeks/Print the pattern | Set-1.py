def printPattern(N):
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            for k in range(i):
                print(j, end=' ')
        print("$", end='')
    print()


printPattern(3)

# def reverseString(s):
#     print(' '.join(s.split()[::-1]))

# reverseString("I love my country")

