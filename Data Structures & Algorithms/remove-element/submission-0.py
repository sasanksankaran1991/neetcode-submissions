class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j+1]
                nums.pop(-1)
            else:
                i += 1
        print(nums)
        return len(nums)