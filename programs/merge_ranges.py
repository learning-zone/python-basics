def merge_ranges(lst):
    """ In HiCal, a meeting is stored as tuples of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am. For example:
    (2, 3) # meeting from 10:00 - 10:30 am
    (6, 9) # meeting from 12:00 - 1:30 pm
    Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

    >>> merge_ranges([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5)])
    [(0, 5)]

    >>> merge_ranges([(0, 3), (3, 5), (7, 8)])
    [(0, 5), (7, 8)]

    >>> merge_ranges([(1, 5), (2, 3)])
    [(1, 5)]
    """

    # time: O(nlogn)
    # space: O(n)


    meeting_times = sorted(lst)

    merged_range = [meeting_times[0]]

    for start, end in meeting_times[1:]:
        last_start, last_end = merged_range[-1]

        if last_end >= start:
            merged_range[-1] = (last_start, max(last_end, end))
        else:
            merged_range.append((start, end))






    return merged_range








if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print 'All tests passed!'
