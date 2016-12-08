# hackerrank v2.0
# code is indented using spaces (2)
__author__ = 'sidmishraw'

def in_place_quicksort(array, start_index, pivot_index):

  # break condition of my recursion
  # if the start_index == pivot_index: array with single element - already sorted
  # if the start_index > pivot_index: array is sorted, no elements ready to sort
  if start_index >= pivot_index:
    return

  # Not going to use this because it will form copies of the 
  # array instead I'm going to use the same array and
  # keep changing the indices
  # left will be the slice from beg:pivotindex and right will be
  # slice from pivotindex to lastindex
  # left_array = array[start_index:pivot_index]
  # right_array = array[pivot_index:len(array)]

  # taking the end-range as pivot_index since I'm assuming
  # the last element of the array is the pivot element

  # initial pointer - inplace pointer
  i = start_index

  # j is the iteration pointer
  for j in range(start_index,pivot_index, 1):

    # if pivot element is greater or equal, then
    # swap ith and jth elements of the array and increment i
    # print("Comparing array[pivot_index](%s) and array[j](%s)" %(array[pivot_index]
    #   ,array[j]))
    if array[pivot_index] >= array[j]:
      array[i], array[j] = array[j], array[i]
      i += 1

  # swap the ith element with the pivot element after parsing through
  # entire array
  array[i], array[pivot_index] = array[pivot_index], array[i]
  
  print(repr(array))

  # assign the indices for left subarray and right subarray
  # print("start_index = %s pivot_index = %s i = %s" % (start_index,pivot_index,i))
  in_place_quicksort(array, start_index, i - 1)
  in_place_quicksort(array, i + 1, pivot_index)



# boilerplate code just to execute when this module is run as main module
if __name__ == '__main__':
  input_array = [3,1,1,5,4,8,2,2,6]
  pivot_index = len(input_array) - 1 # last index = len(a) - 1, can be -1 as well
  start_index = 0 # first index = 0
  # print("%s %s %s" %(input_array, pivot_index, start_index))
  input_array = in_place_quicksort(input_array, start_index, pivot_index)
  