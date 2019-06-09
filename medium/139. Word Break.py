from model.util import *


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = {}
        for word in wordDict:
            d[word] = 1
        flag = [False]*len(s)
        for i, ch in enumerate(s):
            for j in range(i, -1, -1):
                if (flag[j - 1] or j == 0)and s[j:i + 1] in d:
                    flag[i] = True
                    break
        return flag[-1]

p(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# p(Solution().wordBreak("leetcode", ["leet", "code"]))
