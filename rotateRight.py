# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        it = head
        l = []
        while it:
            l.append(it.val)
            it = it.next
        k = k % len(l)
        m = [0] * len(l)
        for index,v in enumerate(l):
            m[(index + k)%len(l)] = v
        it = head
        for i in m:
            it.val = i
            it = it.next
            
if __name__ == '__main__':
    head = it = ListNode(0)
    l = [1,2]
    for i in l:
        t = ListNode(i)
        it.next = t 
        it = it.next
    k = 2
    solver = Solution()
    solver.rotateRight(head,4)
    it = head
    while it:
        print it.val
        it = it.next