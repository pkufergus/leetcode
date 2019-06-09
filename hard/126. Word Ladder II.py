from model.util import *


class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def is_trans(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff >= 2:
                        break
            return True if diff == 1 else False

        def backtrace(k, prev_map, cur_list):
            if k == -1:
                cur_list.append(beginWord)
                cur_list.reverse()
                ret_list.append(cur_list)
                return

            tmp_list = [x for x in cur_list]
            tmp_list.append(wordList[k])
            for prev in prev_map[k]:
                backtrace(prev, prev_map, tmp_list)

        n = len(wordList)
        str2pos = {}
        leftdict = {}
        max_dist = 2**32
        dist = [max_dist] * n
        ret_list = []
        prev_map = {}

        dist_map = {}
        dist_map[1] = []
        for i, s in enumerate(wordList):
            str2pos[s] = i
            leftdict[s] = i
            dist[i] = 1 if is_trans(beginWord, s) else max_dist
            if dist[i] == 1:
                dist_map[1].append(i)
                prev_map[i] = [-1]

        if endWord not in str2pos:
            return ret_list
        t = str2pos[endWord]

        while len(leftdict) > 0:
            #find min dict
            v = -1
            min_dist = max_dist
            for k in leftdict:
                i = str2pos[k]
                if dist[i] < min_dist:
                    min_dist = dist[i]
                    v = i


            if v < 0:
                break
            if v == t:
                break
            word = wordList[v]
            leftdict.pop(word)

            for i, w in enumerate(word):
                for j in range(ord('a'), ord('z') + 1):
                    if j == ord(w):
                        continue
                    new_word = word[:i] + chr(j) + word[i + 1:]
                    if new_word in leftdict:
                        pos = leftdict[new_word]
                        if dist[pos] >= dist[v] + 1:
                            dist[pos] = dist[v] + 1
                            if pos in prev_map:
                                prev_map[pos].append(v)
                            else:
                                prev_map[pos] = [v]

        if dist[t] >= max_dist:
            return ret_list

        backtrace(t, prev_map, [])
        return ret_list

p(Solution().findLadders("hit", "cog",  ["hot","dot","dog","lot","log","cog"]))

# p(Solution().ladderLength("hot", "dog",  ["hot","dog"]))


