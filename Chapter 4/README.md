# Quicksort

This chapter talks about quicksort.

Quicksort is a sorting algorithm. It’s much faster than selection sort 
and is frequently used in real life. For example, the C standard library 
has a function called qsort, which is its implementation of quicksort. 
Quicksort also uses D&C.

- D&C works by breaking a problem down into smaller and smaller 
pieces. If you’re using D&C on a list, the base case is probably an 
empty array or an array with one element.
- If you’re implementing quicksort, choose a random element as the 
pivot. The average runtime of quicksort is O(n log n)!
- The constant in Big O notation can matter sometimes. That’s why 
quicksort is faster than merge sort.
- The constant almost never matters for simple search versus binary 
search, because O(log n) is so much faster than O(n) when your list 
gets big