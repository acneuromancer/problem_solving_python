def binary_search(a_list, n):
    low = 0
    top = len(a_list) - 1
    found = False

    if a_list == []:
        return False

    while low <= top and not found:
        mid = (low + top) // 2

        if a_list[mid] == n:
            found = True
        elif a_list[mid] > n:
            top = mid - 1
        else:
            low = mid + 1

    return found

def binary_search_rec(a_list, n):
    low = 0
    top = len(a_list) - 1

    if a_list == []:
        return False

    mid = (low + top) // 2

    if a_list[mid] == n:
        return True

    if a_list[mid] > n:
        return binary_search_rec(a_list[:mid], n)

    return binary_search_rec(a_list[mid+1:], n)


print(binary_search_rec([-10, 3, 4, 5, 6, 1000, 3000], 1000))
print(binary_search_rec([-10, 3, 4, 5, 6, 1000, 3000], -5000))
print(binary_search_rec([-10, 3, 4, 5, 6, 1000, 3000], -10))
print(binary_search_rec([], 1000))
