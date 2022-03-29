from random import *

quotes = ['hi', 'hello', 'goodbye', 'dog', 'cat', 'banana']


class QuoteGenerator(object):

    def __init__(self, quotes):
        self.last_rand_num = -1
        self.quotes = quotes

    def generate_quote(self):
        random_num = randint(0, len(self.quotes)-1)

        if random_num != self.last_rand_num:
            self.last_rand_num = random_num
            return self.quotes[random_num]
        else:
            return self.generator()


generator1 = QuoteGenerator(quotes)
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
print generator1.generate_quote()
