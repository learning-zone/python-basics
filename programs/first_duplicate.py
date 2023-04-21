"""
Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 3, 3, 1, 5, 2], the output should be
firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be
firstDuplicate(a) = -1.

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

Guaranteed constraints:
1 <= a.length <= 105,
1 <= a[i] <= a.length.

[output] integer

The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.
"""

def first_duplicate(a):
    """

    >>> first_duplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
    6

    >>> first_duplicate([2, 3, 3, 1, 5, 2])
    3

    >>> first_duplicate([1])
    -1

    >>> first_duplicate([2, 1])
    -1

    >>> first_duplicate([2, 2])
    2

    >>> first_duplicate([2, 4, 3, 5, 1])
    -1

    """

    # time: O(n^2)
    # space: O(n)

    lowest_index = len(a)
    for i in range(len(a)):
        num = a[i]
        if num in a[i+1:]:
            index = a[i+1:].index(num) + i + 1
            if index < lowest_index:
                lowest_index = index

    if lowest_index < len(a):
        return a[lowest_index]


    return -1


def first_duplicate_optimized(arr):
    """
    >>> first_duplicate_optimized([8, 4, 6, 2, 6, 4, 7, 1, 5, 8])
    6

    >>> first_duplicate_optimized([2, 3, 3, 1, 5, 2])
    3

    >>> first_duplicate_optimized([1])
    -1

    >>> first_duplicate_optimized([2, 1])
    -1

    >>> first_duplicate_optimized([2, 2])
    2

    >>> first_duplicate([2, 4, 3, 5, 1])
    -1

    """

    # time: O(n)
    # space: O(1)


    for i in range(len(arr)):

        value = arr[abs(arr[i])-1]

        if value >= 0:
            arr[abs(arr[i])-1] = -value
        else:
            return abs(arr[i])

    return -1



if __name__ == "__main__":
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print("All tests passed!")
