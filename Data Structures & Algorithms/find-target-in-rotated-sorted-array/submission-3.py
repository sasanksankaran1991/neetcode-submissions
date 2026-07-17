class Solution:

    def check(self, v, target):

        if v < target:
            return 1
        elif v > target:
            return -1
        else:
            return 0


    def binarysearch(self, arr, target):
        
        l=0
        r=len(arr)-1

        while l<=r:
            m=(l+r)//2
            
            v = self.check(arr[m], target)
            if v < 0:
                r=m-1
            elif v > 0:
                l=m+1
            else:
                return m
        return -1


    def finingtwosortedarray(self, nums):

        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            print(l, m, r)
            if nums[m] < nums[r]:
                r=m
            elif nums[m] > nums[r]:
                l=m+1
            else:
                return nums[:m], nums[m:]



    def search(self, nums: List[int], target: int) -> int:
        
        arr1, arr2 = self.finingtwosortedarray(nums)

        a = self.binarysearch(arr1, target)
        b = self.binarysearch(arr2, target)

        print(a)
        if a >= 0:
            return a
        elif b >= 0:
            return len(arr1)+b
        else:
            return -1


