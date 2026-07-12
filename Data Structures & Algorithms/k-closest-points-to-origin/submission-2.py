import numpy as np
import math

class Solution:

    def sort(self, arr1, arr2, points1, points2):

        i=0
        j=0
        arr = []
        points = []

        while i < len(arr1) or j < len(arr2):
            if i < len(arr1) and (j == len(arr2) or arr1[i] <= arr2[j]):
                arr.append(arr1[i])
                points.append(points1[i])
                i+=1
            else:
                arr.append(arr2[j])
                points.append(points2[j])
                j+=1
        return arr, points




    def split(self, arr, points):
        if len(arr) <= 1:
            return arr, points

        m = len(arr) // 2
        arr1, points1 = self.split(arr[:m], points[:m])
        arr2, points2 = self.split(arr[m:], points[m:])

        arr, points = self.sort(arr1, arr2, points1, points2)

        return arr, points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_array = []

        for y in points:
            d = math.sqrt(pow(y[0], 2) + pow(y[1], 2))
            distance_array.append(d)


        arr, points = self.split(distance_array, points)



        return points[:k]