# Selection sort

This chapter talks about arrays and linked lists, and compares the pros and cons between these two data structures.

## Arrays vs Linked lists

| Operations | Arrays | Linked Lists |
|:----------:|:------:|:------------:|
|   Reading  |  O(1)  |     O(n)     |
|  Insertion |  O(n)  |     O(1)     |
|  Deletion  |  O(n)  |     O(1)     |

## Selection sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 
