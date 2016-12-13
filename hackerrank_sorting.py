# sorting algorithms found on hackerrank challenges
# for quicksort and other algos, look at hackerrank.py or hackerrankv2.py

'Collection of sorting algorithm challenge solutions in Python'

__author__='sidmishraw'


def full_counting_sort():
  'method for the full counting sort challenge question from \
  hackerrank'

  n = int(input())

  input_int_str_array = []

  for j in range(0,n,1):

    string = input().split(" ")

    if j <= (n/2 - 1 if n % 2 == 0 else ((n+1) / 2) - 1):
      string[1] = "-"

    input_int_str_array.append(string)

  # this approach of creating list is wrong since
  # this will copy the inner list 100 times
  # so if change is made to 1 list, it will be seen in all the lists
  # array_array = [[]] * 100
  # where as array_array = [[] for i in range(0,100,1)]
  # will give new list objects for each index of the outer list
  # using list comprehension to reduce code, here it is a better
  # solution since the for loop would just have 1 line of code anyways
  array_array = [[] for _ in range(0,100,1)]

  _ = list(map(lambda element: array_array[int(element[0])].append(element[1]) \
    , input_int_str_array))

  print(" ".join(list(map(lambda element: " ".join(element), array_array))))


# Sample Input #3
# 4
# 5 4 3 2
# Sample Output #3
# 2 3 3 4 4 5
def closest_numbers():
  import math
  'function for solving the closest numbers problem on hackerrank'
  n = int(input())
  with open('abcinput.txt','rt') as f:
    content = f.read()
    array = list(map(int, content.split(" ")))
    array = sorted(array)
    smallest_diff = math.inf
    indices = {}
    i = 0
    while i < (n - 1):
      diff = abs(array[i] - array[i + 1])
      if diff <= smallest_diff:
        smallest_diff = diff
        if diff in indices.keys():
          if array[i] - array[i + 1] <= 0:
            indices[diff].add((array[i],array[i + 1]))
          else:
            indices[diff].add((array[i + 1],array[i]))
        else:
          if array[i] - array[i + 1] <= 0:
            indices[diff] = {(array[i],array[i + 1])}
          else:
            indices[diff] = {(array[i + 1],array[i])}
      i += 1
    final_indices = sorted(indices[smallest_diff])
    print(" ".join(list(map \
      (lambda x:" ".join(list(map(str,x))), \
        final_indices))))




# Sample Input
# 7
# 0 1 2 4 6 5 3
# Sample Output
# 3
def quick_partitioner(array, start_index, pivot_index):
  i = start_index
  for j in range(start_index, pivot_index, 1):
    if array[j] <= array[pivot_index]:
      array[i], array[j] = array[j], array[i]
      i += 1
  array[pivot_index], array[i] = array[i], array[pivot_index]
  print(array, i)
  return (array, i)

def find_the_median():
  'hackerrank find the median challenge problem using quicksort partitioner'
  n = int(input())
  array = list(map(int, input().split(" ")))
  pivot_index = len(array) - 1
  median_index = int(pivot_index / 2)
  index = pivot_index
  start_index = 0
  while index != median_index:
    array, index = quick_partitioner(array, start_index, pivot_index)
    if index > median_index:
      pivot_index = index - 1
    elif index < median_index:
      start_index = index + 1
  print(array[median_index])



# Insertion sort advanced analysis
# Sample Input
# 2  
# 5  
# 1 1 1 2 2  
# 5  
# 2 1 3 1 2
# Sample Output
# 0  
# 4
# Problem with this approach was that it computed the sorted array before
# generating the result
def advanced_insertion_sort_analysisv1():
  'advanced insertion sort analysis problem from hackerrank v1.0'
  from functools import reduce
  t = int(input())
  for _ in range(0, t, 1):
    n = int(input())
    array = list(map(int, input().split(" ")))
    # need to track the number of shifts per element being inserted
    shift_tracker = []
    # do the insertion sort and count the number of shifts
    # assuming 0th element is already sorted
    for i in range(1, n, 1):
      key_element = array[i]
      shifts = 0
      j = i
      while j > 0 and key_element < array[j - 1]:
        array[j] = array[j - 1]
        shifts += 1
        j -= 1
      array[j] = key_element
      shift_tracker.append(shifts)
      print(array)
    total_shifts = reduce(lambda accumulator, element: accumulator + element, \
      shift_tracker)
    print(total_shifts)

# modifying the computation
# modifications include, introduction of variables to hold the sorted maximum
# and sorted_elements_count. These variables enable me to count the elements
# without actually sorting the array
# Assumption: The number of shifts is going to be len(sorted_array) - 1, if the
# incoming element is less than the sorted_max element. Since to make room, we need
# to shift the array by len(sorted_array) - 1 spaces.
# Using this logic in the below function
# fails, since it only defines the upper bound, atmax there are going to be
# len(sorted_array) - 1 number of shifts
# switching over to inversion counting and merge sort approach(advanced topic)
def advanced_insertion_sort_analysisv2():
  'advanced insertion sort analysis problem from hackerrank v2.0'
  t = int(input())
  for _ in range(0, t, 1):
    n = int(input())
    array = list(map(int, input().split(" ")))
    shifts = 0
    # assuming sorted array of size 1, array[0]
    # array[0] is the sorted maximum
    sorted_max = array[0]
    len_sorted_array = 1
    for i in range(1, n, 1):
      incoming_element = array[i]
      j = i
      len_sorted_array += 1
      if incoming_element < sorted_max:
        shifts += (len_sorted_array - 1)
      else:
        if incoming_element > sorted_max:
          sorted_max = incoming_element
      print('incoming_element = %s and len_sorted_array = %s and sorted_max = %s' \
        % (incoming_element, len_sorted_array, sorted_max))
      print("shifts = %s" % (shifts))

# Inversion counting and merge sort approach for counting the number of
# shifts possible in case of insertion sort, without actually sorting the array
def advanced_insertion_sort_analysis():
  'advanced insertion sort analysis v3.0'
  t = int(input())
  for _ in range(0, t, 1):
    n = int(input())
    array = list(map(int, input().split(" ")))
    # I have a global shifts variable since I'm using Merge sort to
    # compute the number of shifts for insertion sort
    merge_sort_partitioner(array, 0, len(array) - 1)
    global shifts
    print(shifts)
    shifts = 0

# Merge sort logic
# recursive approach
def merge_sort_partitioner(array, start_index, end_index):
  'partitoner used by merge sort to partition the array \
  till it is just 1 length arrays'
  # break case of recursion
  if start_index >= end_index:
    return shifts
  # The // operator will give the floor value, an int instead of float
  mid = (start_index + end_index) // 2
  # left partition
  merge_sort_partitioner(array, start_index, mid)
  # right partition
  merge_sort_partitioner(array, mid + 1, end_index)
  # merge the partitions
  merge_sort(array, start_index, mid, end_index)


shifts = 0

# ideally one would pad the smaller half with a larger number in order
# to sort properly, but I'm not going to do any padding
# but not doing the adding leads to too much of boundary condition handling
# hence proceeding with padding with math.inf

# initially the number of inversions or shifts = 0
# when we add the element from the left array to the merged array,
# we increment the inversions with the number of elements from the right array
# already added to the merged array. i.e shifts += j when left[i] <= right[j]
# An "inversion" is nothing but a situation where we need 
# to invert (swap) the elements to make the array sorted.
# For each element in left array, we would like to know 
# how many elements in right are smaller and this will give us 
# the required inversions. To this, we need to look into the 
# two cases where this can happen in merge routine.
# Whenever we put an element from left array, we need to 
# increment the inversions with the count of elements [j] 
# which are already added to result/merged array
# Once one of the array is completely merged/exhausted(after merge loop), 
# if there are any elements left in left array, then we need to increment the 
# count of inversions with (number of elements already merged 
#   from right array * elements left out in left array)
def merge_sort(array, start_index, mid, end_index):
  import math
  global shifts
  left = array[start_index:mid + 1]
  right = array[mid + 1:end_index + 1]
  i = j = 0
  left.append(math.inf)
  right.append(math.inf)
  for index in range(start_index, end_index + 1, 1):
    if left[i] <= right[j]:
      array[index] = left[i]
      i += 1
      shifts += j
    else:
      array[index] = right[j]
      j += 1


def main():
  'main function to test out other functions'

  # full_counting_sort()
  # closest_numbers()
  # find_the_median()
  advanced_insertion_sort_analysis()


# trying out class decorators without arguments
# The class decorators without arguments behave differently than
# their counterparts
# In this case, the class decorators without arguments,
# when we add the decorator, the function is passed as an arguments to
# the __init__() of decorating class and the __call__() is called when the
# function is invoked.
# class decorating_class(object):
#   def __init__(self, func):
#     self.func = func
#     print("assigedn func to class and ", func.__qualname__)

#   def __call__(self, *args, **kwargs):
#     print(*args, **kwargs)
#     print('calling the wrapper function')
#     called_func_value = self.func(*args, **kwargs)
#     return called_func_value

# @decorating_class
# def trying_decorated_func(name, age):
#   return "name is %s and age is %s" % (name, age)


# But in case of decorating classes taking arguments,
# the arguments are passed to the __init__() and the function is passed
# to the __call__() and the __call__() is called at the time of adding the
# decorator to the function
# This form of the decorator will allow the calls of the form
# funct, funct is already evaluated for the values passed as arguments to the
# decorator class. Use this with caution
# Places I can use this are:
# when I need to define some sort of getter functions, this will make a great
# case for getter and setter functions(methods)
# class DecoratingClassWithArguments(object):
#   'This is a decorating class that takes some arguments'
#   def __init__(self, *args, **kwargs):
#     self.args = args
#     self.kwargs = kwargs
#     print('arguments are %s %s' % (args, kwargs))

#   def __call__(self, original_function):
#     print('__call__() or the wrapper function is called', self.args, self.kwargs)
#     value = original_function(*self.args, **self.kwargs)
#     print('value is %s' % value)
#     return value


# @DecoratingClassWithArguments('Sid1', 24)
# def funct(name, age):
#   return "name is %s and age is %s" % (name, age)

# didn't have the problem when using decorators that were defined using
# functions having wrapper functions.




# boilerplate code to execute only when this module is running
# as the main module
if __name__ == '__main__':
  main()






