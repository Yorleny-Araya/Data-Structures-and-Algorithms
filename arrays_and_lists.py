import array
import numpy as np

my_array1 = array.array('i')
my_array2 = array.array('i', [1,2,3,4])

# print(my_array2)

# O(1) time complexity to create an empty array
# np_array1 = np.array([], dtype=int)

# print(np_array1)

# O(N) time complexity
# O(N) space complexity
# np_array2 = np.array([3,1,4,2])

# print(np_array2)

# Inserting in an array
my_array2.insert(0,6) # O(N) time complexity, O(1) space complexity

# print(my_array2)

my_array2.insert(2, 6)

# print(my_array2)

my_array2.insert(6, 6)

# print(my_array2)

# O(N) time complexity
def traverseArray(array):
    for i in array:
        print(i)

# traverseArray(my_array2)

# print(my_array2[2])

# O(1) time complexity
def accessElement(array, index):
    if index > len(array) - 1:
        print("There's not any element on that index")
    else:
        print("Element: ", array[index])

accessElement(my_array2, 4)