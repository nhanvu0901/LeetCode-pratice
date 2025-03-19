import math


# class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     pass
    #both are sorted array so when merge check the last and first of the array

def binarySearch(arr,num,last_index,first_index):
    median_index = math.ceil((last_index + first_index) / 2)  # 2.5 -> 3
    median = arr[median_index]
    if median == num:
        return median_index
    if num > median:
        return binarySearch(arr,num,last_index,median_index)
    else:
        return binarySearch(arr,num,median_index,first_index)

if __name__ == "__main__":
    test = [5, 12, 23, 34, 45, 56, 67, 78, 89, 91, 93, 98, 105, 112, 119, 125, 130, 137, 142, 148, 153, 159, 164, 170, 175, 181, 186, 192, 197, 200]
    find = 78
    result = binarySearch(test,find,len(test)-1,0)
    print(result)
