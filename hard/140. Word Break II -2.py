from model.util import *

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        ret = []
        word_map = {}
        mem = {}
        for word in wordDict:
            word_map[word] = 1

        def bt(left_s):
            res = []
            if left_s == "":
                return []
            if left_s in mem:
                return mem[left_s]
            for i in range(len(left_s)):
                if left_s[0:i + 1] in word_map:
                    if i + 1 == len(left_s):
                        res.append(left_s)
                    else:
                        rest_ret = bt(left_s[i + 1:])
                        for rest in rest_ret:
                            res.append(left_s[0:i + 1] + " " + rest)
            mem[left_s] = res
            return res

        ret = bt(s)
        return ret

p(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))