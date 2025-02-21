# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow

        # reverse
        prev = None
        while middle:
            temp =middle.next
            middle.next = prev
            prev = middle
            middle = temp

        reversed_head = prev

        # compare
        original_head = head

        while original_head and reversed_head:
            if original_head.val == reversed_head.val:
                original_head = original_head.next
                reversed_head = reversed_head.next

            else:
                return False

        return True

                
        
        