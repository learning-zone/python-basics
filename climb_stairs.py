import unittest


def climb_stairs(n):
    """ A fox needs to climb n number of steps. It can jump up 1 step, 2 steps, or 3 steps at a time. How many possible ways are there to get to the top of n steps? """

    if n == 0 or n == 1:
        return 1

    if n == 2:
        return 2

    return climb_stairs(n-1) + climb_stairs(n-2) + climb_stairs(n-3)

# Runtime: O(3^n)


def climb_stairs_dp(n):
    """ A fox needs to climb n number of steps. It can jump up 1 step, 2 steps, or 3 steps at a time. How many possible ways are there to get to the top of n steps? Solve with dynamic programming using the memoization method. """

    cache = { 2: 2, 1: 1, 0: 1 }

    if n in cache:
        return cache[n]

    cache[n] = climb_stairs(n-1) + climb_stairs(n-2) + climb_stairs(n-3)
    return cache[n]

# Runtime: O(n)


def climb_stairs_tab(n, steps):
    """ A fox needs to climb n number of steps. It can jump up X steps (array of possibilities) at a time. How many possible ways are there to get to the top of n steps? Solve with dynamic programming using the tabulation method. """
    result = [0 for x in range(n)]
    result[0] = 1

    for i in range(len(steps)):
        for j in range(steps[i], len(steps)):
            sum = 0
            for k in range(0, i+1):
                sum += result[j - steps[k]];
            result[j] = sum

    return result[n]



class Testing(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(6), 24)
        self.assertEqual(climb_stairs(8), 81)

    def test_climb_stairs_dp(self):
        self.assertEqual(climb_stairs_dp(6), 24)
        self.assertEqual(climb_stairs_dp(8), 81)

    def test_climb_stairs_tab(self):
        self.assertEqual(climb_stairs_tab(6, [1, 2, 3]), 24)
        self.assertEqual(climb_stairs_tab(10, [2, 3, 5]), 14)





if __name__ == '__main__':
    unittest.main()
