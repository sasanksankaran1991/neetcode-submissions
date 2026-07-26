class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_dict = {}
        for x in strs:
            val_dict = {}
            for i in range(len(x)):
                if x[i] in val_dict:
                    val_dict[x[i]] += 1
                else:
                    val_dict[x[i]] = 1

            val_key = tuple(sorted(val_dict.items()))
            if val_key in strs_dict:
                val = strs_dict[val_key]
                val.append(x)
                strs_dict[val_key] = val
            else:
                strs_dict[val_key] = [x]

        print(strs_dict)
        keys_list = strs_dict.values()
        return list(keys_list)
        # for x in range(len())
            
