""" Create a rate checker which takes actions, for number of occurrences, and seconds, for time in which those actions have occurred. Using a check method return True if it is called at least N times (actions) in up to Q seconds. Otherwise, return False. """

import datetime
from time import sleep


class RateChecker(object):

    def __init__(self, actions, seconds):
        self.actions = actions
        self.seconds = seconds
        self.times = []  # Queue needed to keep track of how many times it's being checked

    def check(self):
        """
        >>> clicks = RateChecker(3, 14)
        >>> clicks.check()
        >>> clicks.check()
        >>> clicks.check()
        >>> clicks.check()
        False

        """
        current_time = datetime.datetime.now().time()
        self.times.append(current_time)  # Append each check time to the queue

        if len(self.times) > self.actions:  # First check if the queue is greater than the number of actions
            return False  # Returning false here gives a quick win

        return datetime.datetime.strptime(str(current_time), "%H:%M:%S.%f") - datetime.datetime.strptime(str(self.times.pop()), "%H:%M:%S.%f") <= datetime.timedelta(seconds=self.seconds)  # Check times in the queue
        # (Slower approach if the queue is really huge, hence why queue length vs. actions should be checked first.)



if __name__ == "__main__":
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "All tests passed!"
