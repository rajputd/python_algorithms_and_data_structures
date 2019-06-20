def binary_search_iterative(arr, val, start, end):
    """searches arr for val.

    Parameters:
        arr (array): array to search.
        val (type used in array): value to search for in arr.

    Returns:
        (int) : index of val in arr if val is found.
                Otherwise returns -1 if val cannot be found in arr.
    """

    #while the size of the search space is greater than 0
    while start <= end:
        mid = ((end - start) // 2) + start

        if arr[mid] == val:
            #we found what we want. Yay!
            return mid
        elif arr[mid] > val:
            #search bottom half of search space
            end = mid - 1
        elif arr[mid] < val:
            #search top half of search space
            start = mid + 1

    #couldn't find the value
    return -1
