
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def _sum(self,li):
        s = []
        node = li
        while node is not None:
            s.append(str(node.val))
            node = node.next
        return int(''.join(s[::-1]))

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v = self._sum(l1) + self._sum(l2)
        s = str(v)[::-1]
        l3 = ListNode(s[0])
        print l3
        head = l3
        for i in range(1,len(s)):
            newNode = ListNode(int(s[i]))
            l3.next = newNode
            l3 = newNode
        return head

if __name__ == '__main__':
    s = Solution()
    