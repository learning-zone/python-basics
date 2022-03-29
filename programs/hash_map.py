""" Create a hash map. """

class HashMap(object):

    def __init__(self):
        """ Creates hash list of lists. """

        # In a 64-bit system, creates 64 lists in a list
        self.hash = [[] for x in range(64)]


    def hashing(self, key):
        """ Hashes a key and returns the hashed index. """

        value = 0

        # Gets the total ASCII value of the key
        for char in key:
            value += ord(char)

        # Returns index of range(0, 64) for each of the 64 slots
        index = value % 64

        return index


    def find_val(self, key):
        """ Finds the key and returns the value in hashmap, if none returns keyerror. """

        index = self.hashing(key)
        position = self.hash[index]

        if position != []:
        # Loops through items at hashed index to return tuple value
            for item in position:
                if item[0] == key:
                    return item[1]
            raise KeyError('Key does not exist.')

        else:
            raise KeyError('Key does not exist.')


    def update_or_add(self, key, val):
        """ Updates or adds a new key value pair. """

        index = self.hashing(key)
        position = self.hash[index]

        # Loops through items at hashed index
        # If the position is not empty
        if position != []:
            # Update the value if the key exists
            for item in position:
                if item[0] == key:
                    item[1] = val
                    break
            # If no key exists
            position.append((key, value))

        # If list is empty
        else:
            position.append((key, value))


    def delete(self, key):
        """ Takes a key and deletes the key and value from the hashmap. """

        index = self.hashing(key)
        position = self.hash[index]

        if position != []:
            for i, item in enumerate(position):
                if item[0] == key:
                    del position[i]
                    break
            raise KeyError('Key does not exist.')

        else:
            raise KeyError('Key does not exist.')



