'''
The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list
and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted 
portion until the entire list is sorted.

Time Complexity: O(n^2)
Space Complexity: O(1) not considering the list to be ordered, otherwise it would be O(n).
'''

def selection_sort(my_list):

    # Iterate through all the list
    for i in range(len(my_list) - 1):
        # Consider element in ith position is currenlty the smallest
        smallest_index = i
        # Iterate through the rest of the array
        for j in range( i + 1, len(my_list)):
            if my_list[j] < my_list[smallest_index]:
                # Update the index with smallest number
                smallest_index = j
        # Once the index with smallest number has been set, swap with ith element
        my_list[i], my_list[smallest_index] = my_list[smallest_index], my_list[i]
     
    return my_list


my_list = [8, 5, 1, 4, 7, 3, 10, 2, 9, 6]
print(selection_sort(my_list))