def find_max_frequency(s):
    char_count = [0] * 26 
    for char in s:
        char_count[ord(char) - ord('a')] += 1

    max_count = max(char_count)
    max_char = chr(char_count.index(max_count) + ord('a'))

    return max_char, max_count

input_str = input()
max_char, max_count = find_max_frequency(input_str)
print(f"{max_char} {max_count}")
