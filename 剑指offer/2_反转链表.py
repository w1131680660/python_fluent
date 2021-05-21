#
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        cur, prev = head, None
        # prev 是反转后的下一节点
        # cur 是当前节点位置
        # cur.next 当前的下一节点
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

z = [1,2,3,4,5]
p = Solution.reverseList()
