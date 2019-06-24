def bubbleSort(arr):
    #copy the original array
    output = arr[:]

    #set up start condition for loop
    sorted = False
    while sorted == False:
        sorted = True

        for index in range(1,len(output)):
            #if adjacent elements are out of order
            if output[index - 1] > output[index]:
                #prepare to go through array one more time
                sorted = False

                #swap current value with the previous one
                temp = output[index]
                output[index] = output[index - 1]
                output[index - 1] = temp
    return output
