class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s_list = []
        for x in s:
            if ((ord(x) >= 97) and (ord(x)<=122)) or  ((ord(x) >= 48) and (ord(x)<=57)):
                s_list.append(ord(x))

        l = 0
        r = len(s_list)-1
        m = (l+r)//2

        while (l <= r):
            if s_list[l] == s_list[r]:
                l+=1
                r-=1
            else:
                return False

        return True