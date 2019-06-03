import sys

debug=1

def p(s):
    try:
        if debug == 1:
            if isinstance(s, str):
                print(s)
            elif isinstance(s, list):
                print(map(str, s))
    except:
        pass

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        k = i if i > j else j
        c = [0] * (k + 1)
        t = 0
        while i >= 0 and j >= 0:
            sum = int(a[i]) + int(b[j]) + t
            c[k] = sum % 2
            t = sum // 2
            i -= 1
            j -= 1
            k -= 1
        while i >= 0:
            sum = int(a[i]) + t
            c[k] = sum % 2
            t = sum // 2
            i -= 1
            k -= 1
        while j >= 0:
            sum = int(b[j]) + t
            c[k] = sum % 2
            t = sum // 2
            j -= 1
            k -= 1
        if t == 1:
            return "1" + "".join(map(str, c))
        return "".join(map(str, c))

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str:w
        """
        return bin(int(a, 2) + int(b, 2))[2:]

p(Solution().addBinary2("1010", "1011"))