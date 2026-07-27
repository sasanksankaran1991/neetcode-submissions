class Solution:

    def encode(self, strs: List[str]) -> str:

        # decoded_strs = ''
        # for x in strs:
        if len(strs) == 0:
            decoded_strs = 'empty'
        else:
            decoded_strs = "||".join(strs)

        return decoded_strs

    def decode(self, s: str) -> List[str]:
        
        if s == 'empty':
            return []
        else: 
            s = s.split('||')
            return s
