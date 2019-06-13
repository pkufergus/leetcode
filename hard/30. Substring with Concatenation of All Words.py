from model.util import *


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        N = len(s)
        WORDSLEN = len(words)
        if N <= 0 or WORDSLEN <=0:
            return []
        NW = len(words[0])
        if NW <= 0:
            return []
        NC = N // NW
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        ret_list = []
        for k in range(NW):
            match_num = 0
            cd = d.copy()
            for i in range(NC):
                j = i * NW + k
                if j + NW > N:
                    continue
                w = s[j:j + NW]
                if w in cd:
                    if cd[w] >= 1:
                        cd[w] -= 1
                        match_num += 1
                    else:
                        if match_num <= 0:
                            continue
                        last_w = s[j - match_num * NW: j - match_num * NW + NW]
                        while last_w != w:
                            cd[last_w] += 1
                            match_num -= 1
                            if match_num == 0:
                                break
                            last_w = s[j - match_num * NW: j - match_num * NW + NW]
                else:
                    match_num = 0
                    cd = d.copy()
                if match_num == WORDSLEN:
                    ret_list.append(j - match_num * NW + NW)
                    match_num -= 1
                    last_w = s[j - match_num * NW: j - match_num * NW + NW]
                    cd[last_w] += 1
        return ret_list

p(Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
# p(Solution().findSubstring("barfoofoobarthefoobarman",["foo","bar", "the"] ))


