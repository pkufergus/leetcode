from model.util import *


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x:x[0])
        intervals_sort = intervals
        ret_list=[]
        if len(intervals_sort) < 2:
            return intervals_sort
        tmp_list = intervals_sort[0]
        for i in range(1, len(intervals_sort)):
            [s, e] = intervals_sort[i]
            [lasts, laste] = tmp_list
            if s > laste:
                ret_list.append(tmp_list)
                tmp_list = [s, e]
            elif e <= laste:
                continue
            else:
                tmp_list = [lasts, e]

        ret_list.append(tmp_list)

        return ret_list


p(Solution().merge([[1,3],[9,16],[8,10],[15,18]]))
