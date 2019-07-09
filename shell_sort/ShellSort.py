def shellSort(arr):
	gaps = [701, 301, 132, 57, 23, 10, 4, 1]

	#go through each gap
	for gap in gaps:

		#no point in going through a gap larger than the array
		if gap > len(arr):
			continue

		#perform insertion sort on the sublists created by the gap value
		for start in range(gap):

			#for every element in the current sub-array
			for j in range(start, len(arr), gap):

				#shift elements larger than the current value up one position
				#in the sublist
				current = arr[j]
				sorted_index = j
				while(sorted_index > 0 and arr[sorted_index-gap] > current):
					arr[sorted_index] = arr[sorted_index - gap]
					sorted_index = sorted_index - gap

				#insert current element at the newly created space
				arr[sorted_index] = current
