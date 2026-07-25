class Solution:

    def sorting(self, arr1, arr2):

        arr = []
        i = 0
        j = 0

        while i<=len(arr1) or j<=len(arr2):
            if (i==len(arr1)) &  (j==len(arr2)):
                return arr
            elif (i==len(arr1)):
                arr = arr+arr2[j:]
                j=len(arr2)
            elif (j==len(arr2)):
                arr = arr+arr1[i:]
                i=len(arr1)
            elif arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
            


    def spliting(self, nums):
        # print(nums)
        if len(nums) == 1:
            return nums

        l=0
        r=len(nums)-1
        m=(l+r)//2
        # print(l, m , r)
        arr1 = self.spliting(nums[:m+1])
        arr2 = self.spliting(nums[m+1:])

        arr = self.sorting(arr1, arr2)

        return arr



    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # arr = self.spliting(nums)
        # arr = sorted(nums)
        nums.sort()
        # print(arr)

        final_result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pass
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j < k:
                target = -nums[i]
                # print(i, j, k, target, arr[j]+arr[k])
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    final_result.append([nums[i], nums[j], nums[k]])
                    # print('match')
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

        return final_result
