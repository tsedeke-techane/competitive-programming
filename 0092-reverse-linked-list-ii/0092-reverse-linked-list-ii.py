# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        pre_node = dummy
        for _ in range(1, left):
            pre_node = pre_node.next

        reverse_begin = pre_node.next
        curr = reverse_begin
        prev = None

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        pre_node.next = prev
        reverse_begin.next = curr

        return dummy.next


