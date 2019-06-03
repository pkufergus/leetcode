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