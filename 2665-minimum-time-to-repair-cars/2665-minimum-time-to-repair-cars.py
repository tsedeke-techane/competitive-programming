class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def count_repaired(time):
            count = 0
            for rank in ranks:
                count += int(sqrt(time / rank)) 
            return count
        
        left, right = 1, ranks[0] * cars * cars
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            repaired = count_repaired(mid)  
            
            if repaired >= cars:  
                ans = mid
                right = mid - 1
            else:  
                left = mid + 1

        return ans  
