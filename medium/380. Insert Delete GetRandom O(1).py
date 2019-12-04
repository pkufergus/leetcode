import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.size = 0
        self.dataset = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataset:
            return False
        if self.size < len(self.nums):
            self.dataset[val] = self.size
            self.nums[self.size] = val
            self.size += 1
        else:
            self.nums.append(val)
            self.dataset[val] = self.size
            self.size += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dataset:
            return False
        index = self.dataset[val]
        self.dataset.pop(val)
        if index == self.size - 1:
            self.size -= 1
        else:
            self.nums[index] = self.nums[self.size - 1]
            self.dataset[self.nums[index]] = index
            self.size -= 1
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.size < 1:
            return -1
        r = random.randint(0, self.size - 1)
        return self.nums[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()