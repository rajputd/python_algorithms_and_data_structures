def selectionSort(arr):
	length = len(arr)

	#for each element in the array
	for i in range(length):

		#find the minimum element in the unsorted elements
		min_val = arr[i]
		min_index = i
		for j in range(i, length):
			if arr[j] < min_val:
				min_val = arr[j]
				min_index = j

		#swap current element with the minimum found earlier
		arr[i], arr[min_index] = arr[min_index], arr[i]

