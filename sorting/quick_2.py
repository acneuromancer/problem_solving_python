def partition(arr, low, high):
    pivot_index = low - 1
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] <= pivot:
            pivot_index += 1
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    pivot_index += 1
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return pivot_index


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr)-1)
print('sorted array: ', arr)
