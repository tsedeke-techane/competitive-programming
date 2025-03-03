# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_s = ListNode()
        dummy_l = ListNode()

        s_tail = dummy_s
        l_tail = dummy_l
        
        while head:
            if head.val < x:
                s_tail.next = head
                s_tail = s_tail.next

            else:
                l_tail.next = head
                l_tail = l_tail.next

            head = head.next

        s_tail.next = dummy_l.next
        l_tail.next = None

        return dummy_s.next