def binary_search(my_list, target):

    left = 0
    right = len(my_list) - 1

    while left <=right:

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