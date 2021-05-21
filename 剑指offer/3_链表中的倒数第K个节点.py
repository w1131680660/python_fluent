
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        cur ,latter= head,head
        for i in range(k):
            if cur:
                cur = cur.next

            else:return None

        while latter:
            cur, latter= cur.next,latter.next
        return latter