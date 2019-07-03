from model.util import *


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        line_map = {}

        N = len(points)
        if N <= 1:
            return N
        new_points = []
        points_map = {}
        max_num = 0
        for p in points:
            key = "{}-{}".format(p[0], p[1])
            if key in points_map:
                points_map[key] += 1
            else:
                points_map[key] = 1
                new_points.append(p)
        for _, v in points_map.items():
            max_num = max(max_num, v)

        def gcd(a, b):
            is_neg = False
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                is_neg = True
            a = abs(a)
            b = abs(b)
            if a % b == 0:
                if is_neg:
                    return -a//b, 0
                else:
                    return a//b, 0
            small = min(a, b)
            g = 1
            m, n = a, b
            if not m:
                g = n
            elif not n:
                g = m
            elif m == n:
                g = m
            else:
                while m % n:
                    m, n = n, m % n
                g = n
            if is_neg:
                return -a//g, b // g
            else:
                return a//g, b//g

        for i in range(1, len(new_points)):
            x1 = new_points[i][0]
            y1 = new_points[i][1]
            tmp_map = {}
            for j in range(i):
                x2 = new_points[j][0]
                y2 = new_points[j][1]
                kb = (0, 0, 0, 0)
                if x1 == x2:
                    kb = [0, x1, 0, 0]
                else:
                    k1 = y1 - y2
                    k2 = x1 - x2
                    b1 = y2 * x1 - y1 * x2
                    b2 = x1 - x2
                    k1, k2 = gcd(k1, k2)
                    b1, b2 = gcd(b1, b2)
                    kb = [k1, k2, b1, b2]
                key = "-".join(map(str, kb))
                if key in tmp_map:
                    continue
                else:
                    tmp_map[key] = 1
                if key in line_map:
                    line_map[key] += points_map["{}-{}".format(x1, y1)]
                else:
                    line_map[key] = points_map["{}-{}".format(x1, y1)] + points_map["{}-{}".format(x2, y2)]
        for (_, v) in line_map.items():
            max_num = max(max_num, v)
        return max_num
p(Solution().maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
# p(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
