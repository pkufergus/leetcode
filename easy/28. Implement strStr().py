import sys

debug=1

def p(s):
    try:
        if debug == 1:
            print(s)
    except:
        pass

class Solution(object):
    def build_next(self, needle):
        next = [0] * len(needle)
        j = 0
        i = 1
        while i < len(needle):
            while i < len(needle) and needle[i] != needle[j]:
                i += 1
            while i < len(needle) and needle[i] == needle[j]:
                next[i] = j + 1
                j += 1
                i += 1
            if j > 0:
                j = next[j - 1]
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        next = self.build_next(needle)
        p(str(map(str, next)))
        k, t = 0, 0
        while k < len(haystack) and t < len(needle):
            p("k={} {} t= {} {}".format(k, haystack[k], t, needle[t]))
            if haystack[k] == needle[t]:
                k += 1
                t += 1
            else:
                if t > 0:
                    t = next[t - 1]
                else:
                    k += 1
        if t == len(needle):
            return k - t
        return -1

i = Solution().strStr("aabaaabaaac", "aabaaac")
print i
