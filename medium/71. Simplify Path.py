from model.util import *


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = path.split("/")

        path_list = []

        for s in arr:
            if s == "." or s == "":
                continue
            if s == "..":
                if len(path_list) > 0:
                    path_list.pop()
                continue
            path_list.append(s)
        return "/" + "/".join(path_list)

p(Solution().simplifyPath("/a/../../b/../c//.//../.."))
