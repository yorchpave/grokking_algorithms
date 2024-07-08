'''
Quick sort is a sorting algorithm tha uses Divide & Conquer approach.
It does this by selecting a random element in the array (a.k.a pivot)
and moves all smaller elements in the array to the left, and all greater
elements in the array to the right (partitioning). This algorithm is then
repeated (hence it's recursive) with the left and right subarrays. Once 
these are sorted, they can be merged like: left_sub_array + pivot + right_sub_array

Time Complexity: O(n log n) -- avg time. Worst case is O(n^2) but very rare (list would
need to be already sorted and pick the first element of the array as the pivot)
Space Complexity: O(log n) -- size of the call stack on avg
'''

def quick_sort(my_list):

    # TBD
    pass


my_list = [8, 5, 1, 4, 7, 3, 10, 2, 9, 6]
print(quick_sort(my_list))