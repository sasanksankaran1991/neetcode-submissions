class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        right = max(piles)
        left = 1

        while left <= right:
            mid = left + (right-left)//2

            count = 0
            for i in range (n):
                a = piles[i]//mid
                mod = piles[i]% mid
                if mod ==0:
                    count += max(a,1)
                else:
                    count+= max(a+1,1)
            
            
            if count <= h:
                right = mid-1
            else:
                left = mid+1

        
        return right+1