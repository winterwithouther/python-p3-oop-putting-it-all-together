#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if (isinstance(new_size, int)):
            self._size = new_size
            return self._size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

shoe1 = Shoe("addidas", 9)
shoe1.cobble()
print(shoe1.condition)