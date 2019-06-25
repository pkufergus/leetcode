from model.util import *


class Solution(object):
    def contain(self, a, b):
        for i in range(len(a)):
            if a[i] < b[i]:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        fs = [0] * 128
        ft = [0] * 128
        for ch in t:
            ft[ord(ch)] += 1
        pos = -1
        size = 0
        min_size = 2**32
        min_pos = -1
        start = 0
        for i, ch in enumerate(s):
            fs[ord(ch)] += 1
            if self.contain(fs, ft):
                pos = i
                size = i - start + 1
                if size < min_size:
                    min_size = size
                    min_pos = pos
                fs[ord(s[start])] -= 1
                start += 1
                while self.contain(fs, ft):
                    size = i - start + 1
                    if size < min_size:
                        min_size = size
                        min_pos = pos
                    fs[ord(s[start])] -= 1
                    start += 1
        if min_pos < 0:
            return ""
        a = s[min_pos - min_size + 1:min_pos + 1]
        return "".join(a)

p(Solution().minWindow("ADOBECODEBANC", "ABC"))