# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Step 1: Find the middle of the list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # prev now points to the head of the reversed second half
        reversed_head = prev
        original_head = head
        
        # Step 3: Compare both halves
        while reversed_head:  
            if original_head.val != reversed_head.val:
                return False
            original_head = original_head.next
            reversed_head = reversed_head.next
        
        return True
