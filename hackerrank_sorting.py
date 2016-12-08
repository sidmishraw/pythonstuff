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



def main():
  'main function to test out other functions'

  full_counting_sort()



# boilerplate code to execute only when this module is running
# as the main module
if __name__ == '__main__':
  main()





