class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set()
        for x in nums:
            nums_set.add(x)

        start_list = []
        for x in nums_set:
            if x-1 not in nums_set:
                start_list.append(x)

        max_counter = 0
        for x in start_list:
            next_val = x
            counter = 1
            while next_val+1 in nums_set:
                counter+=1
                next_val = next_val+1
            if counter > max_counter:
                max_counter = counter

        return max_counter
        
        