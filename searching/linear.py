def sequential_search(a_list, n):
    found = False
    index = 0

    while index < len(a_list) and not found:
        if a_list[index] == n:
            found = True
        else:
            index += 1

    return found

def ordered_seq_search(a_list, n):
    found = False
    stop = False
    index = 0

    while index < len(a_list) and not found and not stop:
        if a_list[index] == n:
            found = True
        elif a_list[index] > n:
            stop = True
        else:
            index += 1

    return found



print(sequential_search([1, 2, 3, 4, 5, 6], 4))
print(sequential_search([1, 2, 3, 4, 5, 6], 10))

print(ordered_seq_search([-10, 3, 4, 5, 6, 1000, 3000], 1000))
print(ordered_seq_search([-10, 3, 4, 5, 6, 1000, 3000], -500))
