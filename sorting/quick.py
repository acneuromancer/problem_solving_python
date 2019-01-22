def quick_sort(numbers):
    quick_sort_helper(numbers, 0, len(numbers)-1)

def quick_sort_helper(numbers, first, last):
    if first < last:
        split_point = partition(numbers, first, last)
        quick_sort_helper(numbers, first, split_point-1)
        quick_sort_helper(numbers, split_point+1, last)

def partition(numbers, first, last):
    pivot_value = numbers[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and numbers[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and numbers[right_mark] >= pivot_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            numbers[left_mark], numbers[right_mark] = numbers[right_mark], numbers[left_mark]

    numbers[first], numbers[right_mark] = numbers[right_mark], numbers[first]

    return right_mark


numbers = [3000, 0, -1, 25, 10, 8]
quick_sort(numbers)
print(numbers)
