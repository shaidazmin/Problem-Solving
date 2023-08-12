def isBinary(sr):
    for char in str(int(sr)):
        if char not in [0,1]:
            return 0
    return 1

# Correct Solution is 

def isBinary(str):
    #code here
    for char in str:
        if char != '0' and char != '1':
            return False
    return True

print(isBinary(0o0111100110101100))

# print( 0 in [1,0])