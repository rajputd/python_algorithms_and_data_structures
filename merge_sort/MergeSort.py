def mergeSort(arr):
    output = arr[:]

    #base case when input array cannot be split any further
    if len(output) == 1 or len(output) == 0:
        return output
    else:
        #find middle of the array
        midpoint = len(output) // 2

        #split array in half and sort the halves
        left = mergeSort(output[0:midpoint])
        right = mergeSort(output[midpoint:])

        #merge the two halves together
        left_index = 0
        right_index = 0
        for i in range(len(output)):
            if left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    output[i] = left[left_index]
                    left_index += 1
                else:
                    output[i] = right[right_index]
                    right_index += 1
            elif left_index < len(left):
                output[i] = left[left_index]
                left_index += 1
            else:
                output[i] = right[right_index]
                right_index += 1

    return output