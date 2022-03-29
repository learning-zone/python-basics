def get_products_of_all_ints_except_at_index(lst):
    """ Takes a list of integers and returns a list of the products except the integer at that index. Do not use division.

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index([1, 0, 3, 4])
    [0, 12, 0, 0]
    """

    # Runtime: O(n^2)
    # Spacetime: O(n^2)

    products = []

    for a in range(len(lst)):
        product = 1

        for b in range(len(lst)):
            if a != b:
                product *= lst[b]
        products.append(product)

    return products

# Testing
# a = 0
# product = 1
# b = 0
# skip
# b = 1
# product = 1 * 7
# b = 2
# product = 1 * 7 * 3
# b = 3
# product = 1 * 7 * 3 * 4

# products = [84]

# a = 1
# product = 7

# b = 0
# product = 7 * 1



def get_products_of_all_ints_except_at_index_optimized(lst):
    """ Takes a list of integers and returns a list of the products except the integer at that index. Do not use division.

    >>> get_products_of_all_ints_except_at_index_optimized([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index_optimized([1, 0, 3, 4])
    [0, 12, 0, 0]
    """

    # Runtime: O(n)
    # Spacetime: O(n)

    products = []
    product = 1
    product_reverse = 1
    products_before = []
    products_after = []

    for i in range(len(lst)):
        products_before.append(product)
        product *= lst[i]

    for i in range(len(lst)-1, -1, -1):
        products_after.append(product_reverse)
        product_reverse *= lst[i]

    for i in range(len(products_before)):
        products.append(products_after[-i-1] * products_before[i])

    return products


# Testing
# lst = [1, 7, 3, 4]

# first for loop
# i = 0
# products_before = [1]
# product = 1
# i = 1
# products_before = [1, 1]
# product = 7
# i = 2
# products_before = [1, 1, 7]
# product = 21
# i = 3
# products_before = [1, 1, 7, 21]
# product = 84
# i = 4

# second for loop
# i = 3
# products_after = [1]
# product_reverse = 4
# i = 2
# products_after [1, 4]
# product_reverse = 12
# i = 1
# products_after = [1, 4, 12]
# product_reverse = 84
# i = 0
# products_after = [1, 4, 12, 84]
# product_reverse = 84
# i = -1




if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED"

