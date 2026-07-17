class Solution:

    def check(self, v, target):

        if v < target:
            return 1
        elif v > target:
            return -1
        else:
            return 0


    def binarysearch(self, arr, l, r, target):

        while l<=r:
            m=(l+r)//2
            print('*-*-*', l, m , r)
            v = self.check(arr[m], target)
            if v < 0:
                r=m-1
            elif v > 0:
                l=m+1
            else:
                return m
        return -1


    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            # print(l, m, r)
            if nums[m] < nums[r]:
                r=m
            elif nums[m] > nums[r]:
                l=m+1
            else:
                print(m, nums[m])
                if (nums[m] <= target) & (target <= nums[-1]):
                    print('1---', l, r)
                    l=m
                    r=len(nums)-1
                    a = self.binarysearch(nums, l, r, target)
                else:
                    print('2---', l, r)
                    l=0
                    r=m-1
                    a = self.binarysearch(nums, l, r, target)

                return a     
        