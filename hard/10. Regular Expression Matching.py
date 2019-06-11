from model.util import *


class Solution(object):
    d = {}


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        if s == "":
            if len(p) == 1:
                return False
            if p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        if len(s) == 1:
            if p == "":
                return False
            if p == s or p == ".":
                return True
            if len(p) <= 1:
                return False
            if p[1] == "*":
                if p[0] == ".":
                    return self.isMatch(s, p[2:]) or self.isMatch("", p[2:])
                else:
                    return self.isMatch(s, p[2:]) or (p[0] == s[0] and self.isMatch("", p[2:]))
            else:
                if p[0] == s[0] or p[0] == ".":
                    return self.isMatch("", p[1:])
                return False
        # if s + "-" + p in self.d:
        #     return self.d[s + "-" + p]
        if len(p) <= 1:
            return False
        if p[1] == "*":
            if p[0] == ".":
                flag = False
                for i in range(len(s) + 1):
                    flag = self.isMatch(s[i:], p[2:])
                    if flag:
                        break
                # self.d[s + "-" + p] = flag
                return flag
            else:
                flag = False
                flag1 = self.isMatch(s, p[2:])
                for i in range(len(s)):
                    if p[0] == s[i]:
                        flag = self.isMatch(s[i + 1:], p[2:])
                    else:
                        break
                    if flag:
                        break
                # self.d[s + "-" + p] = flag or flag1
                return flag or flag1
        else:
            if p[0] == ".":
                if len(s) >= 1:
                    flag2 = self.isMatch(s[1:], p[1:])
                    # self.d[s + "-" + p] = flag2
                    return flag2
                else:
                    return False
            else:
                if len(s) == 0:
                    return False
                if s[0] == p[0]:
                    flag = self.isMatch(s[1:], p[1:])
                    # self.d[s + "-" + p] = flag
                    return flag
                else:
                    # self.d[s + "-" + p] = False
                    return False

#"aabcbcbcaccbcaabc"
#".*a*aa*.*b*.c*.*a*"
# p(Solution().isMatch("mississippi", "mis*is*p*."))
# p(Solution().isMatch("a", "ab*"))
# p(Solution().isMatch("", "a*"))
# p(Solution().isMatch("aaaaab", "a*b"))
# p(Solution().isMatch("ab", ".*"))
# p(Solution().isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))
p(Solution().isMatch("ab", ".*..c*"))




