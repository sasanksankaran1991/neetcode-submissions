class Solution:
    def scoreOfString(self, s: str) -> int:
        l=1
        score = 0
        while l <=len(s)-1:
            # print(s[l], s[l-1])
            score = score +abs((ord(s[l-1])-ord(s[l])))
            l+=1

        return score
