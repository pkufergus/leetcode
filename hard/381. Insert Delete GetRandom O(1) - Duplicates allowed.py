import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataset = {}
        self.nums = []


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataset:
            self.nums.append(val)
            self.dataset[val].add(len(self.nums) - 1)
            return False
        self.nums.append(val)
        self.dataset[val] = set([len(self.nums) - 1])
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dataset:
            return False
        indexset = self.dataset[val]
        r = indexset.pop()
        self.nums[r] = self.nums[-1]
        rm_index = len(self.nums) - 1
        self.dataset[self.nums[r]].add(r)
        if rm_index in self.dataset[self.nums[r]]:
            self.dataset[self.nums[r]].remove(rm_index)
        if len(self.dataset[val]) < 1:
            self.dataset.pop(val)
        self.nums.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        r = random.randint(0, len(self.nums) - 1)
        return self.nums[r]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()