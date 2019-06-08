from model.util import *


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ret = {}
        # ret_list = []
        for s in strs:
            ks = [0]*26
            for ch in s:
                i = ord(ch) - ord('a')
                ks[i]+=1

            finger = ",".join(map(str, ks))
            if finger in ret:
                ret[finger].append(s)
            else:
                ret[finger] = [s]

        return [v for v in ret.values()]

p(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
