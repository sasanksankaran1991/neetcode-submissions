class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            s_val = s[i]
            t_val = t[i]
            if s_val not in s_dict:
                s_dict[s_val] = 1
            else:
                s_dict[s_val] += 1

            if t_val not in t_dict:
                t_dict[t_val] = 1
            else:
                t_dict[t_val] += 1

        print(t_dict, s_dict)
    
        for key, values in s_dict.items():
            if s_dict[key] != t_dict.get(key, 0):
                return False
        return True

