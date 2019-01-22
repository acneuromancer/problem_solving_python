def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        swap = False
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swap = True
        if not swap:
            return

def bubble_sort_2(numbers):
    while True:
        swapped = False
        for i in range(0, len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break

def bubble_sort_3(numbers):
    exchanges = True
    pass_num = len(numbers) - 1

    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                exchanges = True
        pass_num -= 1


numbers = [15, -1000, 30, 500, 3000, -1500, 20, 1]
bubble_sort_3(numbers)
print(numbers)
