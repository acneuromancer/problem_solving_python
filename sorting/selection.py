def selection_sort_max(numbers):
    for fill_slot in range(len(numbers)-1, 0, -1):
        pos_of_max = 0

        for location in range(1, fill_slot+1):
            if numbers[location] > numbers[pos_of_max]:
                pos_of_max = location

        numbers[fill_slot], numbers[pos_of_max] = numbers[pos_of_max], numbers[fill_slot]

        print(numbers)

def selection_sort_min(numbers):
    for fill_slot in range(0, len(numbers)-1):
        pos_of_min = fill_slot

        for location in range(fill_slot+1, len(numbers)):
            if numbers[location] < numbers[pos_of_min]:
                pos_of_min = location

        numbers[fill_slot], numbers[pos_of_min] = numbers[pos_of_min], numbers[fill_slot]

        print(numbers)



numbers = [15, -1000, 30, 500, 3000, -1500, 20, 1]
selection_sort_min(numbers)
print(numbers)
