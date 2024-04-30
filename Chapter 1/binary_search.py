'''
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search
interval in half. The idea of binary search is to use the information that the array is sorted and reduce
the time complexity.

Time Complexity: O(log n)
Space Complexity: O(1) not considering the list to be searched, otherwise it would be O(n).

'''
def binary_search(my_list, target):

    # Define left and riht pointer
    left = 0
    right = len(my_list) - 1

    # Iterate through the list until pointers meet
    while left <=right:

        # Look at the middle element and update left and right pointers accordingly
        middle = (left + right) // 2
        guess = my_list[middle]

        if guess == target:
            return guess

        if guess < target:
            right = middle - 1

        if guess > target:
            left = middle + 1

    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 11))