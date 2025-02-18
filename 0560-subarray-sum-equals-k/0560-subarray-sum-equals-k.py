class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = Counter()
        arr = [0] + nums 
        count = 0  

        # Compute prefix sums
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        for i in range(len(arr)):
            target = arr[i] - k 

            if target in prefix_map:
                count += prefix_map[target] 
            
            prefix_map[arr[i]] += 1 

        return count
           



