class Solution:
    def final_merge(self, arr1, arr2):
        print('final_merge', arr1, arr2)
        i=0
        j=0
        new_arr = []
        while (i <= len(arr1)) or (j <= len(arr2)):
            print(i, j, new_arr)
            if (i == len(arr1)) and (j == len(arr2)):
                return new_arr
            elif i == len(arr1):
                print(i, j)
                new_arr.append(arr2[j])
                j+=1
            elif j == len(arr2):
                new_arr.append(arr1[i])
                i+=1
            elif arr1[i] <= arr2[j]:
                new_arr.append(arr1[i])
                i+=1
            else:
                new_arr.append(arr2[j])
                j+=1
        print(new_arr, arr1, arr2)
        return new_arr

    def split(self, arr, s, e):
        if s+e <= 1:
            return arr

        m = int((s+e)/2)
        arr1 = arr[s:m]
        arr2 = arr[m:e]
        print('input to split', s, m, e, arr, arr1, arr2)
        arr11 = self.split(arr1, 0, m)
        arr21 = self.split(arr2, 0, e-m)

        arr = self.final_merge(arr11, arr21)
        print('result from merge', arr)

        return arr


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        arr1 = self.split(nums1[0:m], 0, m)
        arr2 = self.split(nums2, 0, n)

        print('final merge after all the calculation', arr1, arr2)

        res = self.final_merge(arr1, arr2)

        for i in range(len(res)):
            nums1[i] = res[i]

        