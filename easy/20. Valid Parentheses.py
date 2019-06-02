import sys


class Solution(object):
    def is_match(self, a, b):
        if a == "(" and b == ")":
            return True
        if a == "[" and b == "]":
            return True
        if a == "{" and b == "}":
            return True
        return False


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch == ")" or ch == "]" or ch == "}":
                if len(stack) > 0:
                    top = stack[len(stack) - 1]
                    if not self.is_match(top, ch):
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        size = len(stack)
        if size == 0:
            return True
        else:
            return False


s="()[]{}["

print(Solution().isValid(s))