# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Node(object):
    def __init__(self, x, pos):
        self.val = x
        self.pos = pos
    def __lt__(self, other):
        return self.val < other.val

class SmallHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, val):
        heapq.heappush(self.arr, val)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return heapq.heappop(self.arr)

    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        smallheap = SmallHeap()
        head = cur = None

        for i in range(k):
            if lists[i]:
                smallheap.heap_insert(Node(lists[i].val, i))
                lists[i] = lists[i].next
        flag = True
        while flag:
            flag = False
            topnode = smallheap.get_top()
            if not topnode:
                break
            else:
                flag = True
                smallheap.heap_pop()
                if head:
                    cur.next = ListNode(topnode.val)
                    cur = cur.next
                else:
                    head = cur = ListNode(topnode.val)
                if lists[topnode.pos]:
                    smallheap.heap_insert(Node(lists[topnode.pos].val, topnode.pos))
                    lists[topnode.pos] = lists[topnode.pos].next
        return head


