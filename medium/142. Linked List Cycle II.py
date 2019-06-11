from model.util import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return None
        if head.next == head:
            return head

        p = head.next
        fastp = head.next.next
        i = 1
        while p and fastp and p != fastp:
            p = p.next
            if fastp.next:
                fastp = fastp.next.next
            else:
                fastp = None
                break
            i += 1
        if not fastp or not p:
            return None
        n = 1
        q = p.next
        while q != p and q:
            q = q.next
            n += 1
        k = head
        frontk = head
        for i in range(n):
            frontk = frontk.next
        i = 0
        while frontk != p:
            k = k.next
            frontk = frontk.next
            i += 1
        q = p
        while k != q:
            k = k.next
            q = q.next
            i += 1
        return k

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next.next
p(Solution().detectCycle(head))
