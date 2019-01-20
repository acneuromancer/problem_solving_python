def insertion_sort(numbers):
    for index in range(1, len(numbers)):
        current_value = numbers[index]
        pos = index

        while pos > 0 and numbers[pos-1] > current_value:
            numbers[pos] = numbers[pos-1]
            pos -= 1

        numbers[pos] = current_value

        print(numbers)
        

numbers = [3000, 10, -500, 9, 15, 300, 250]
insertion_sort(numbers)
print(numbers)
