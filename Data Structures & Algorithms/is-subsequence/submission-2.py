class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        string_list = []
        for i in t:
            string_list.append(i)

        counter=0
        pos=-1   
        for j in s:
            if j in string_list[pos+1:]:
                new_pos = string_list[pos+1:].index(j) + pos+1
                print(j, pos, new_pos)
                if pos >= new_pos:
                    return False
                else:
                    pos = new_pos
                    counter+=1
            else:
                return False
        
        return True

        
