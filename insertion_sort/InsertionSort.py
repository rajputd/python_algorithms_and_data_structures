def insertionSort(arr):
    output = arr[:]

    #go through each element
    for index in range(1, len(output)):
        #grab current element
        current = output[index]

        #get last index of sorted output
        j = index

        #shift up all sorted elements that are greater than current one
        while j > 0 and output[j - 1] > current:
            output[j] = output[j - 1]
            j = j - 1

        #insert current element at newly created space
        output[j] = current

    return output



