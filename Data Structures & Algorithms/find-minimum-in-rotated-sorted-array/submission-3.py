class Solution:

    def sort(self, arr1, arr2):
        # print('****', arr1, arr2)
        i = 0
        j = 0
        new_arr = []
        while i <= len(arr1) or j <= len(arr2):
            if (i == len(arr1)) & (j == len(arr2)):
                # print(new_arr, 'stop')
                return new_arr
            elif i == len(arr1):
                new_arr+=arr2[j:]
                j = len(arr2)
            elif j == len(arr2):
                new_arr+=arr1[i:]
                i = len(arr1)
            elif arr1[i] < arr2[j]:
                new_arr.append(arr1[i])
                i+=1
            else:
                new_arr.append(arr2[j])
                j+=1
            # print(new_arr, i, j, len(arr1), len(arr2))
     


    def split(self, arr):
        # print(arr)
        if len(arr) == 1:
            return arr

        min_v = 1
        max_v = len(arr)
        mid = (min_v+max_v)//2

        arr1 = self.split(arr[:mid])
        arr2 = self.split(arr[mid:])

        new_arr = self.sort(arr1, arr2)
        # print("---", new_arr, arr1, arr2)

        return new_arr



    def findMin(self, nums: List[int]) -> int:

        # new_arr = self.split(nums)

        return min(nums)
        
        
        

