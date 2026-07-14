class Solution:

    def searchVal(self, matrix, target):
        LM = 0
        RM = len(matrix)-1
        while LM<=RM:
            MM = (LM+RM)//2
            if target < matrix[MM][0]:
                RM = MM-1
            elif target >= matrix[MM][0] and target <= matrix[MM][-1]:
                return matrix[MM]
            elif target > matrix[MM][0]:
                LM = MM+1
            else:
                return matrix[MM]


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        val = self.searchVal(matrix, target)
        if val is None:
            return False
        L=0
        R=len(val)-1

        while L<=R:
            M=(L+R)//2
            print(L, M, R)
            if target < val[M]:
                print(1)
                R = M-1
            elif target > val[M]:
                print(2)
                L = M+1
            else:
                print(3)
                return True
        return False
