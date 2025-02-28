# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
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

        reversed_head = prev
        original_head = head

        maxTwin = 0
        while reversed_head:
            currSum = original_head.val + reversed_head.val         
            maxTwin = max(maxTwin, currSum)
            original_head = original_head.next
            reversed_head = reversed_head.next

        return maxTwin

