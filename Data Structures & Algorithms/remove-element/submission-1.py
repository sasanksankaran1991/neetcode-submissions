class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # i = 0
        # for x in nums:
        #     if x != val:
        #         i+=1
        # print(i)

        i=0
        j=len(nums)
        while i < j:
            if nums[i] == val:
                nums.pop(i)
                print(i, nums)
                j-=1
            else:
                i+=1

        return len(nums)

