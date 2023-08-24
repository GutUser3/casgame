def bubble_sort(array):
    n = len(array)

    for i in range(n):

        swapped = False

        for k in range(0, n - i - 1):
            if array[k] > array[k + 1]:

                array[k], array[k + 1] = array[k + 1], array[k]
                swapped = True

        if not swapped:
            break


my_list = [25, 87, 2, 78, 50, 152, 9]
bubble_sort(my_list)
print("Sorted list:", my_list)



def binary_search(target, array):
    left, right = 0, len(array) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


sorted_array = sorted([25, 87, 2, 78, 50, 152, 9])
print(sorted_array)
target = 87
result = binary_search(target, sorted_array)
if result != -1:
    print(f"{target} found at index {result}")
else:
    print("Target not found")

