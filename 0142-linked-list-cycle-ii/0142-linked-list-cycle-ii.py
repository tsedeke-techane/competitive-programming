# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer:
                cycle_entrance = head
                while cycle_entrance != slow_pointer:
                    cycle_entrance =  cycle_entrance.next
                    slow_pointer = slow_pointer.next

                return cycle_entrance

        return None

