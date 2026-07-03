class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_val = 0
            for j in range(i+1, len(arr)):
                if arr[j]>max_val:
                    max_val = arr[j]
            arr[i] = max_val
        arr[-1] = -1
        return(arr)