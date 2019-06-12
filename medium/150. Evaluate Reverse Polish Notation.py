from model.util import *


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {}
        ops['+'] = lambda x, y: x + y
        ops['-'] = lambda x, y: x - y
        ops['*'] = lambda x, y: x * y
        ops['/'] = lambda x, y: x // y + 1 if (x < 0 and y > 0 and x % y != 0) or (x > 0 and y < 0 and x % y != 0) else x // y
        for s in tokens:
            if s in ops:
                b = stack.pop()
                a = stack.pop()
                f = ops[s]
                c = f(a, b)
                stack.append(c)
            else:
                stack.append(int(s))

        return stack[0]

p(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


