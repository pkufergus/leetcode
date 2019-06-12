from model.util import *


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s) - 9):
            if i < 0:
                return []
            seq = s[i:i + 10]
            if seq in d:
                d[seq] = 1
            else:
                d[seq] = 0

        return [x for x in d if d[x] == 1]

p(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))