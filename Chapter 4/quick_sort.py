'''
Quick sort is a sorting algorithm tha uses Divide & Conquer approach.
It does this by selecting a random element in the array (a.k.a pivot)
and moves all smaller elements in the array to the left of the pivot, and all greater
elements in the array to the right of the pivot (partitioning). This algorithm is then
repeated (hence it's recursive) with the left and right subarrays. Once 
these are sorted, they can be merged like: left_sub_array + pivot + right_sub_array

Time Complexity: O(n log n) -- avg time. Worst case is O(n^2) but very rare (list would
need to be already sorted or contain many duplicates)
Space Complexity: O(log n) -- size of the call stack on avg
'''

def partition(my_list, l, r):
        pivot = my_list[r]
        i = l

        for j in range(l, r):
            if my_list[j] <= pivot:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                i += 1
        
    
        my_list[i], my_list[r] = my_list[r], my_list[i]
        return i

def quick_sort(my_list, l, r):

    if l < r:
        pivot_index = partition(my_list, l, r)
        quick_sort(my_list, l, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, r)

    return my_list

my_list = [8, 5, 1, 4, 7, 3, 10, 2, 9, 6]
print(quick_sort(my_list, 0, len(my_list) - 1))