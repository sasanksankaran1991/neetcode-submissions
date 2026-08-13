class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result_dict = {}
        for x in nums:
            if x in result_dict:
                counter = result_dict[x]
                counter+=1
                result_dict[x] = counter
            else:
                 result_dict[x] = 1

        # result_dict[4] = 2
        # print('0---oo', result_dict)
        
        dummy_list = [[] for n in range(len(nums)+1)]

        for key, val in result_dict.items():
            # index_val = dummy_list[val]
            # index_val.append(key)
            # dummy_list[val] = index_val
            dummy_list[val].append(key)

        # print(dummy_list)

        final_list = []
        for x in range(len(dummy_list)-1, -1, -1):
            if len(final_list) < k:
                delta = k-len(final_list)
                final_list = final_list + dummy_list[x][:delta]
            else:
                break

        return final_list[:k]
