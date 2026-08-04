from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i: int, total: int):
            if total == target:
                res.append(path.copy())
                return
            if i == len(nums) or total > target:
                return

            # choose nums[i]
            path.append(nums[i])
            dfs(i, total + nums[i])  # can reuse same number
            path.pop()

            # skip nums[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return res