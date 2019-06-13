from model.util import *


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        status = [0] * len(s)
        i = 0
        max_size = 0
        for ch in s:
            if ch == "(":
                stack.append(i)
            else:
                if len(stack) < 1:
                    i += 1
                    continue
                pos = stack.pop()
                status[pos] = status[i] = 1
            i += 1
        i = 0
        for n in status:
            if n == 1:
                i += 1
                max_size = max(max_size, i)
            else:
                i = 0
        return max_size
p(Solution().longestValidParentheses(")()())()()("))

