def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # loop over all array values until item is found
    if index == len(array):
        return None # not found
    if array[index] == item:
        return index # found
    # recursively calls itself iterating index
    return linear_search_recursive(array, item, index + 1)

# returns center item!! not just any time.
def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # defines our pointers
	left = 0
	right = len(array) - 1

    # while left is less then or equal to right
	while left <= right:
        # define new middle as the center of our array
		middle = (left + right) // 2
        # if we find the item, return middle
		if array[middle] == item:
			return middle # found
        # else if the item is less then our middle item
		elif item < array[middle]:
            # redefine right pointer as middle minus one
			right = middle - 1
        # else if the item is greater then our middle item
		elif item > array[middle]:
            # redefine left pointer as middle plus one
			left = middle + 1

	return None # not found




def binary_search_recursive(array, item, left=None, right=None):
    # checks to set default values
	if left is None and right is None:
		left = 0
		right = len(array) - 1

    # defines our new middle
	middle = (left + right) // 2

    # if we get to the center and can't find our item
	if left == middle and array[middle] is not item:
		return None # not found

	if array[middle] == item:
		return middle # found
    # else if, we recursively call our function changing the left/right pointer
	elif item < array[middle]:
		return binary_search_recursive(array,item,left, middle - 1)
	elif item > array[middle]:
		return binary_search_recursive(array,item,middle + 1, right)
