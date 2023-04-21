def highest_product_of_three(list_of_ints):
    """ Takes a list of integers and returns the highest product of three of the integers. The input list_of_ints will always have at least three integers.

    >>> highest_product_of_three([1,2,3,4,5])
    60

    >>> highest_product_of_three([1,2,3,4,-5])
    24

    >>> highest_product_of_three([-10,-10,1,3,2])
    300

    >>> highest_product_of_three([10,2,5])
    100

    >>> highest_product_of_three([5,4,3,2,1])
    60

    """

    # Runtime: O(n)
    # Spacetime: O(1)

    highest_product = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    highest = list_of_ints[0]
    lowest = list_of_ints[0]
    highest_two = list_of_ints[0] * list_of_ints[1]
    lowest_two = list_of_ints[0] * list_of_ints[1]

    if len(list_of_ints) == 3:
        return highest_product


    for i in range(2,len(list_of_ints)-1):
        product = list_of_ints[i] * list_of_ints[i + 1]
        current_num = list_of_ints[i]

        if current_num > highest:
            highest = current_num
            if product > highest_two:
                highest_two = product
        elif current_num < lowest:
            lowest = current_num
            if product < lowest_two:
                lowest_two = product

    if highest_two * highest > lowest_two * lowest:
        highest_product = highest_two * highest
    elif highest_two * highest < lowest_two * lowest:
        highest_product = lowest_two * lowest
    elif highest_two * lowest < lowest_two * highest:
        highest_product = lowest_two * highest
    else:
        highest_product = highest_two * lowest

    return highest_product




if __name__ == "__main__":
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
