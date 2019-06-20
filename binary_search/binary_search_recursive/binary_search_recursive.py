

def binary_search_recursive(arr, val, start, end):
    """searches arr for val between and including the indices start and end.

    Parameters:
        arr (array): array to search.
        val (type used in array): value to search for in arr.
        start (int): start index to search for val in arr.
        end (int): end index to search for val in arr.

    Returns:
        (int) : index of val in arr if val is found.
                Otherwise returns -1 if val cannot be found in arr.
    """

    #base case, we've searched the entire array
    if end < start:
        return -1

    mid = ((end - start) // 2) + start

    #we found the value we want. Hurray!
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        #search lower half of the array
        return binary_search_recursive(arr, val, start, mid - 1)
    elif arr[mid] < val:
        #search upper half of the array
        return binary_search_recursive(arr, val, mid + 1, end)
