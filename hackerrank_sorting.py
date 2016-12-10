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




def main():
  'main function to test out other functions'

  # full_counting_sort()
  # closest_numbers()
  find_the_median()



# boilerplate code to execute only when this module is running
# as the main module
if __name__ == '__main__':
  main()





