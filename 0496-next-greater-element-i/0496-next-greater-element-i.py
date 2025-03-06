class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng_element = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                ng_element[stack.pop()] = num
            stack.append(num)
        
        return [ng_element.get(num, -1) for num in nums1]
