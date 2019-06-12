from model.util import *


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [""] * len(s)
        n = len(s)
        is_start = 1
        space_num = 0
        end_pos = 0
        for j in range(n):
            if s[j] != " ":
                end_pos = j
                break
        k = 0
        for i in range(len(s) - 1, end_pos - 1, -1):
            if s[i] == " ":
                if is_start:
                    continue
                space_num += 1
                if space_num > 1:
                    continue
            else:
                is_start = 0
                space_num = 0
            a[k] = s[i]
            k += 1

        start = 0
        for i in range(k):
            if a[i] == " ":
                p = start
                q = i - 1
                while p < q:
                    a[p], a[q] = a[q], a[p]
                    p += 1
                    q -= 1
                start = i + 1
        p = start
        q = k - 1
        while p < q:
            a[p], a[q] = a[q], a[p]
            p += 1
            q -= 1


        return  "".join(a[:k])



p(Solution().reverseWords("a good   example"))