def reverse_str(str):
    if len(str) == 1:
        return str[0]

    last = len(str) - 1
    return str[last] + reverse_str(str[0:last])


def reverse_str_2(str):
    if str == "":
        return str

    return reverse_str_2(str[1:]) + str[0]


print(reverse_str_2("Hello World!"))
print(reverse_str_2("abcdefgh"))
print(reverse_str_2("xyz"))
