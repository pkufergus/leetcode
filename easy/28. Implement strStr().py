import sys

def p(s):
    # print(s)
    pass

int_max = 2 ** 32 - 1

class Solution(object):
    def is_same(self, haystack, start, needle):
        for i in range(0,len(needle)):
            p("com {} {}".format(haystack[i + start - len(needle) + 1], needle[i]))
            if haystack[i + start - len(needle) + 1] != needle[i]:
                return False
        return True

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_sum = 0
        n_size = len(needle)
        for n in needle:
            # print("n={} {}".format(n, ord(n)))
            n_sum = (n_sum * 10 + ord(n)) % int_max

        p(n_sum)
        if len(haystack) < len(needle):
            return -1
        sum = 0
        for i in range(0, len(needle)):
            sum = (sum * 10 + ord(haystack[i])) % int_max
        p("sum={}".format(sum))
        if sum == n_sum and self.is_same(haystack, n_size - 1, needle):
            return 0

        for i in range(n_size, len(haystack)):
            sum = (sum - (ord(haystack[i - n_size]) * (10 ** (n_size -1))) % int_max) * 10 + ord(haystack[i])
            sum = sum % int_max
            p("sum={}".format(sum))
            if sum == n_sum and self.is_same(haystack, i, needle):
                return i - n_size + 1
        return -1

i = Solution().strStr("mississippi", "mississippi")
print i
