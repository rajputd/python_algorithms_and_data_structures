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
            #if there are unsorted elements remaining in the right and left halves
            if left_index < len(left) and right_index < len(right):
                #if the left array has the smaller value
                if left[left_index] <= right[right_index]:
                    #add that value into the output array and continue
                    output[i] = left[left_index]
                    left_index += 1
                else:
                    #otherwise move the value in the right half to the output array
                    output[i] = right[right_index]
                    right_index += 1
            #else if we have inserted all the values in one array then insert the rest from the other
            elif left_index < len(left):
                output[i] = left[left_index]
                left_index += 1
            else:
                output[i] = right[right_index]
                right_index += 1

    return output