class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        print(l1.val)
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next =l1
                l1 =l1.next
            else:
                prev.next =l2
                l2 = l2.next
            prev  = prev.next
        prev.next = l1 if l1 is not None else l2

        return prehead.next

P =Solution()
P.mergeTwoLists([1,2,4],[1,3,4])