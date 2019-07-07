def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        #sort halves of array above and below the partition
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def partition(arr, low, high):
    #pick last value in array as pivot value
    pivot = high

    #move all elements less than pivot to the left of i
    i = low
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    #move pivot to i, this sorts the pivot value to the rest of the array
    arr[i], arr[pivot] = arr[pivot], arr[i]

    return i