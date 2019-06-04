from model.util import *

#
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         size = 0
#         mp = 0
#         mq = 0
#         for i, ch in enumerate(s):
#             p = i - 1
#             q = i + 1
#             t = 1
#             while p >= 0 and q < len(s) and s[p] == s[q]:
#                 t += 2
#                 if t > size:
#                     size = t
#                     mp = p
#                     mq = q
#                 p -= 1
#                 q += 1
#
#
#         for i, ch in enumerate(s):
#             p = i
#             q = i + 1
#             t = 0
#             while p >= 0 and q < len(s) and s[p] == s[q]:
#                 t += 2
#                 if t > size:
#                     size = t
#                     mp = p
#                     mq = q
#                 p -= 1
#                 q += 1
#
#
#         return s[mp:mq+1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ''
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
        	if i - maxLen >= 1 and s[i-maxLen-1 : i+1] == s[i-maxLen-1:i+1][::-1]:
        		start = i - maxLen - 1
        		maxLen += 2
        		continue

        	if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
        		start = i - maxLen
        		maxLen += 1
        return s[start:start+maxLen]

p(Solution().longestPalindrome("abcbcba"))
