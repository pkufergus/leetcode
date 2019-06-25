from model.util import *


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ret = []
        N = len(s)
        dp = [ [] for i in range(N)]
        if not wordDict:
            return ret
        word_set = set(wordDict)
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        for i in range(N):
            for j in range(max(0, i - max_len), i + 1):
                if s[j:i + 1] in word_set:
                    if j == 0:
                        dp[i].append(-1)
                    else:
                        if len(dp[j - 1]) > 0:
                            dp[i].append(j - 1)
        def bt(k, indexs):
            if k == -1:
                if len(indexs) <= 1:
                    ret.append(s)
                    return
                tmp = s[:indexs[1] + 1]
                for i in range(2, len(indexs) + 1):
                    if i == len(indexs):
                        tmp += " " + s[indexs[i - 1] + 1:]
                        continue
                    else:
                        tmp += " " + s[indexs[i - 1] + 1:indexs[i] + 1]
                ret.append(tmp)
                return
            for j in dp[k]:
                bt(j, [j] + indexs)

        bt(N - 1, [])

        return ret

# p(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

p(Solution().wordBreak("abcd",["a","abc","b","cd"]))
p(Solution().wordBreak("a",["a"]))
