import sys

debug=1

def p(s):
    try:
        if debug == 1:
            if isinstance(s, str):
                print(s)
            elif isinstance(s, list):
                print(map(str, s))
            else:
                print("{}".format(s))
    except:
        pass


def sort_list_maopao(nums):
    N = len(nums)
    if N <= 1:
        return
    for i in range(N):
        flag = False
        for j in range(N - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                flag = True

        if not flag:
            return



if __name__ == "__main__":
    nums = [6, 4, 5, 9, 7, 3]
    p(nums)
    sort_list_maopao(nums)
    p(nums)