def apply_operations(s, operations):
    for op in operations:
        t = op[0]
        if t == 1:
            x, c = op[1], op[2]
            s = c + s if x == 1 else s + c
        elif t == 2:
            x, c = op[1], op[2]
            s = s + c if x == 2 else c + s
    return s

# Read input
s = input()
q = int(input())
operations = []

# Read operations
for _ in range(q):
    op = list(input().split())
    t = int(op[0])
    if t == 1:
        x, c = 1, op[1]
        operations.append((1, x, c))
    else:
        x, c = int(op[1]), op[2]
        operations.append((2, x, c))

# Check constraints
if 1 <= len(s) <= 10**5 and all('a' <= c <= 'z' for c in s) and 1 <= q <= 2 * 10**5:
    result = apply_operations(s, operations)
    print(result)
else:
    print("Invalid input! Please check the constraints.")
