
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retlist = None
        head = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while not l1 is None and not l2 is None:
            if head is None:
                if l1.val < l2.val:
                    head = l1
                    l1 = l1.next
                else:
                    head = l2
                    l2 = l2.next
                retlist = head
            else:
                if l1.val < l2.val:
                    retlist.next = l1
                    l1 = l1.next
                else:
                    retlist.next = l2
                    l2 = l2.next
                retlist = retlist.next

        if not l1 is None:
            retlist.next = l1
        if not l2 is None:
            retlist.next = l2
        return head

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

l2 = ListNode(5)
l2.next = ListNode(5)
l2.next.next = ListNode(6)

head=Solution().mergeTwoLists(l1, l2)

while not head is None:
    print head.val
    head = head.next