"""A sequence of integers is called a zigzag sequence if each of its elements is either strictly less than both neighbors or strictly greater than both neighbors. For example, the sequence 4 2 3 1 5 3 is a zigzag, but 7 3 5 5 2 and 3 8 6 4 5 aren't.

For a given array of integers return the length of its longest contiguous sub-array that is a zigzag sequence.

Example

For a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6], the output should be
zigzag(a) = 4.

The longest zigzag sub-arrays are [5, 3, 5, 3] and [3, 2, 8, 6] and they both have length 4.

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

Guaranteed constraints:
2 <= a.length <= 25,
0 <= a[i] <= 100.

[output] integer"""



def zigzag(a):
    """
    >>> zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    4

    >>> zigzag([2, 3, 1, 0, 2])
    3

    >>> zigzag([1, 2, 3, 2, 1])
    3

    >>> zigzag([2, 3, 1, 4, 2])
    5

    >>> zigzag([1, 2, 0, 3, 2, 1, 3, 2, 4, 0])
    6

    >>> zigzag([1, 2])
    2

    >>> zigzag([1, 2, 1])
    3

    >>> zigzag([1, 1])
    1

    """

    # time: O(n)
    # space: O(1)

    longest = 1
    curr_length = 1

    if len(a) == 2 and a[0] != a[1]:
        return len(a)


    for i in range(len(a)-2):
        prev = a[i]
        curr = a[i+1]
        nxt = a[i+2]

        if (prev < curr and curr > nxt) or (prev > curr and curr < nxt):
            if nxt == a[-1]:
                curr_length += 2
            else:
                curr_length += 1

            longest = max(longest, curr_length)

        else:
            curr_length += 1
            longest = max(longest, curr_length)
            curr_length = 1

    return longest



def zigzag_recursive(a):
    """
    >>> zigzag_recursive([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    4

    >>> zigzag_recursive([2, 3, 1, 0, 2])
    3

    >>> zigzag_recursive([1, 2, 3, 2, 1])
    3

    >>> zigzag_recursive([2, 3, 1, 4, 2])
    5

    >>> zigzag_recursive([1, 2, 0, 3, 2, 1, 3, 2, 4, 0])
    6

    >>> zigzag_recursive([1, 2])
    2

    >>> zigzag_recursive([1, 2, 1])
    3

    >>> zigzag_recursive([1, 1])
    1

    """

    # time: O(n)
    # space: O(n)


    if len(a) < 2:
        return len(a)

    if len(a) == 2 and a[0] != a[1]:
        return len(a)

    longest = 1
    i = 1
    good = True

    while good and i < len(a) - 1:
        curr = a[i]
        prev = a[i-1]
        nxt = a[i+1]

        if (prev < curr and curr > nxt) or (prev > curr and curr < nxt):
            i +=1
            if i == len(a)-1:
                longest += 1
        else:
            good = False
        longest += 1

    return max(longest, zigzag_recursive(a[i:]))



if __name__ == "__main__":
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "All tests passed"
