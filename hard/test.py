# coding=utf-8

def count(S, T):
    if not T or not S:
        return None
    s = [0] * len(S)

    ch = T[0]
    if ch == S[0]:
        s[0] = 1
    for i in range(1, len(S)):
        if ch == S[i]:
            s[i] = s[i - 1] + 1
        else:
            s[i] = s[i - 1]
    print(s)
    news = [0] * len(S)
    for i in range(1, len(T)):
        ch = T[i]
        for k in range(len(news)):
            news[k] = 0
        for j in range(i):
            news[j] = 0
        for j in range(i, len(S)):
            if ch == S[j]:
                news[j] = news[j - 1] + s[j - 1]
            else:
                news[j] = news[j - 1]
        for i in range(len(news)):
            s[i] = news[i]
        print(s)
    return s[-1]


S="rabrabtabcdddabacd"
T="rata"

c=count(S, T)
print(c)

