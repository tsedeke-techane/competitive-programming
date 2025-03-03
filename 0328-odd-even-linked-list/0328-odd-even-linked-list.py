# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd = ListNode()
        dummy_even = ListNode()

        odd_tail = dummy_odd
        even_tail = dummy_even

        parity = True
        while head:
            if parity:
                odd_tail.next = head
                odd_tail = odd_tail.next
                parity = False

            else:
                even_tail.next = head
                even_tail = even_tail.next
                parity = True

            head = head.next

        odd_tail.next = dummy_even.next
        even_tail.next = None

        return dummy_odd.next


