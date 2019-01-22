def quick_sort(numbers):
    pass

def quick_sort_helper(numbers, first, last):
    pass

def partition(numbers, first, last):
    pivot_value = numbers[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and numbers[left_mark] <= pivot_value:
            left_mark += 1
        while numbers[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            numbers[left_mark], numbers[right_mark] = numbers[right_mark], numbers[left_mark]

    numbers[first], numbers[right_mark] = numbers[right_mark], numbers[first]

    return right_mark
