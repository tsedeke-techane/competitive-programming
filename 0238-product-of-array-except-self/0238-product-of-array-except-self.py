class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        ans[0]=1
        pr=1
        for i in range(len(nums)):
            if i!=0:
                ans[i]=pr
            pr*=nums[i]
        pr=1
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                ans[i]*=pr
            pr*=nums[i]
        return ans
