def shell_sort(numbers):
    n = len(numbers)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2


numbers = [3000, 0, -1, 25, 10, 8]
shell_sort(numbers)
print(numbers)
