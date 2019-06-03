
import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == "":
            return 0
        size = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == " " and size == 0:
                continue
            if ch != " ":
                size += 1
            else:
                break
        return size

p(Solution().lengthOfLastWord("a"))