import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass

class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        c = 1
        last = s[0]
        out = ""
        for i in range(1, len(s)):
            if s[i] == last:
                c += 1
            else:
                out += "{}{}".format(c, last)
                last = s[i]
                c = 1
        out += "{}{}".format(c, last)
        return out

p(Solution().countAndSay(10))
p(Solution().countAndSay(11))
