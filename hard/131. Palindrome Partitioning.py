from model.util import *

class Solution(object):
    def is_palin(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backtrace(self, part_list, left_s, results):
        if left_s == "":
            results.append(part_list)
            return
        for i in range(1, len(left_s) + 1):
            a = left_s[:i]
            if self.is_palin(a):
                # backup_list = [x for x in part_list]
                # part_list.append(a)
                self.backtrace(part_list + [a], left_s[i:], results)
                # part_list = backup_list




    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        if not s:
            return results
        self.backtrace([], s, results)
        return results

p(Solution().partition("aaabb"))


