class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,0,0]
        for n in nums:
            bucket[n] += 1

        print(bucket)

        i = 0
        for n in range(len(bucket)):
            for j in range(bucket[n]):
                nums[i] = n
                i+=1
        