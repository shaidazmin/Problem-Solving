def rotate_string(s):
    return s[1:] + s[0]

input_str = input()

result = rotate_string(input_str)
print(result)
