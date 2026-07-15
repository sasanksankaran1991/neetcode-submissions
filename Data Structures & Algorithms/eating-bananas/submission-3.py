import math
import numpy as np
class Solution:
    
    def check_correct(self, piles, k, h):
        
        min_val = 0
        for x in piles:
            a = math.ceil(x / k)
            min_val+=a

        if min_val > h:
            return (1, min_val)
        elif min_val <= h:
            return (-1, min_val)


    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = 1000000000

        
        min_mid = np.inf
        max_k = -1
        while low <= high:
            mid = (low+high)//2
            output, min_val = self.check_correct(piles, mid, h)

            if output > 0:
                low = mid +1
            elif output < 0:
                if (mid < min_mid) & (min_val >= max_k):
                    min_mid = mid
                    min_k = min_val
                high = mid -1
        
        return min_mid


