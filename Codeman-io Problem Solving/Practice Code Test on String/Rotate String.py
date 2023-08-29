def rotate_string(s):
    s = s.replace(' ','')
    return ''.join(str(c) for c in s[1:] + s[0])

# input_str = input()

result = rotate_string(' t orpn ')
print(result)
