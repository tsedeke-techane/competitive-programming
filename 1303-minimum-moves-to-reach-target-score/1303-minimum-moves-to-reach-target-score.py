class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        
        move = 0

        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                
                target //= 2
                move += 1
                maxDoubles -= 1
            
            elif target % 2 != 0:
                target -= 1
                move += 1

            elif maxDoubles == 0:
                move += target - 1
                target = 0
            
        return move
                
