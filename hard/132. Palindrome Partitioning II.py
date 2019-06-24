from model.util import *


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [N] * (N + 1)
        dp[N] = -1
        if N <= 1:
            return 0
        dp[0] = 0
        for i in range(1, N):
            j = 0
            while i + j < N and  i - j >= 0 and s[i - j] == s[i + j]:
                dp[i + j] = min(dp[i + j], dp[i - j - 1] + 1)
                j += 1
            j = 0
            while i + j < N and i - 1 - j >= 0 and s[i - 1 - j] == s[i + j]:
                dp[i + j] = min(dp[i + j], dp[i - j - 2] + 1)
                j += 1
        return dp[N - 1]


p(Solution().minCut("abbabb"))
p(Solution().minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))


