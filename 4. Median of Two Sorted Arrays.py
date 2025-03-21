import math


# class Solution:
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#     pass
# both are sorted array so when merge check the last and first of the array

def binarySearch(arr, num, last_index, first_index):
    median_index = math.ceil((last_index + first_index) / 2)  # 2.5 -> 3
    median = arr[median_index]
    if median == num:
        return median_index
    if first_index >= last_index - 1:
        if num > arr[first_index]:
            return first_index + 1
        else:
            return first_index
    if num > median:
        return binarySearch(arr, num, last_index, median_index)
    else:
        return binarySearch(arr, num, median_index, first_index)


def insertNumber(arr, num):
    index = binarySearch(arr, num, 0, len(arr) - 1)
    return arr.insert(index, num)

def checkCase(first_array, second_array):
    if first_array[-1] > second_array[-1]:
        return second_array, first_array  # a_array, b_array
    else:
        return first_array, second_array

def mergeArr(first_array,second_array):
    a_array, b_array = checkCase(first_array, second_array)

    if b_array[len(b_array)-1] > a_array[len(a_array)-1]:
        if b_array[0] < a_array[0]:#TH nam trong
            return 'nam trong'
        elif a_array[0] <= b_array[0] <= a_array[len(a_array)-1]:
            if a_array[0] == b_array[0]:
                pass
            elif  b_array[0] <= a_array[-1]:
                pass
            else:
                pass
        else:
            return 'ngoai khoang'



test_array  = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
best_array = [ 13, 14, 15, 16]
print(mergeArr(test_array,best_array))
# input_num = 8
# index = binarySearch(test_array, input_num, len(test_array) - 1, 0)
# test_array.insert(index, input_num)
# print(test_array)
