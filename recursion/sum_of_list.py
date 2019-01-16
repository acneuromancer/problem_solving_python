def list_sum(num_list):
    sum = 0

    for num in num_list:
        sum += num

    return sum


def list_sum_recursive(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursive(num_list[1:])


numbers = list(range(1, 101))
print('The sum of the numbers between 1 and 100:')
print(list_sum(numbers))
print(list_sum_recursive(numbers))
