# ams = __import__('aAms-ams').amsbo will fail since ams-ams will just give
# a namepace that resolves upto ams-ams and doesn't include amsbo module
# using ams = __import__('ams-ams.amsbo') will import both amsbo module as wel# l but will not have ams hold the reference to the amsbo module
# instead it will be the name for ams-ams package/namespace
# using
# ams = __import__('ams-ams.amsbo').amsbo solves the problem of
# aliasing ams-ams.amsbo as ams
ams = __import__('ams-ams.amsbo').amsbo

def testingamsbo():
  print(dir(ams))
  amount = float(input())
  mo = ams.Money(amount=amount)
  print(mo)
  

# Running Time of Algorithms
# input format -
# first line = 1 <= N <= 1001
# second line = -10000 <= x <= 10000, x in a
def runningTimeInsertionSort():
  f = open('abcinput.txt')
  # N = int(input())
  istring = list(map(int, f.read().split()))
  N = istring[0]
  a = istring[1:]
  counter = 0
  for i in range(1,N):
    j = i
    while j > 0 and a[j-1] > a[j]:
      a[j-1],a[j] = a[j],a[j-1]
      counter += 1
      j -= 1
      f.close()
      print(counter)

# Quick sort
def quickieSort(array,pivotElement):
  if len(array) <= 1:
    return array
  leftarray = list(filter(lambda x: x < pivotElement, array))
  rightarray = list(filter(lambda x: x > pivotElement, array))
  sortedarray = list(filter(lambda x: x == pivotElement, array))
  leftarray = quickieSort(leftarray,leftarray[0]) if len(leftarray) != 0 else []
  rightarray = quickieSort(rightarray,rightarray[0]) if len(rightarray) != 0 else []
  return leftarray + sortedarray + rightarray

# Inplace quick sort  
def quicksort(array, beginindex, pivotindex):
  if not array[beginindex:pivotindex]:
    return
  i = beginindex
  for j in range(beginindex, pivotindex if pivotindex > 0 else len(array) + pivotindex):
    if array[j] < array[pivotindex]:
      array[i],array[j] = array[j],array[i]
      i += 1
      array[i], array[pivotindex] = array[pivotindex],array[i]
      print(" ".join(list(map(str,array))))
      f = open('abcinput.txt','a')
      f.write(" ".join(list(map(str,array))))
      f.write('\n')
      f.close()
      quicksort(array,beginindex = beginindex, pivotindex = i - 1) if array[beginindex:pivotindex] else []
      quicksort(array,beginindex = i+1, pivotindex = pivotindex) if array[beginindex:pivotindex] else []


# testing out decorators
# Below is the basic template for defining decorators using functions
# def decorator_function(original_function):
#   # do stuff here
#   def wrapper():
#     # do stuff here
#     pass
#   return wrapper

# # the original function
# def original_function():
#   # do stuff here
#   pass

"""
 @decorator_function
 def original_function():
   pass

Is the same as declaring 
original_function = decorator_function(original_function)

decorator class approach--
"""
# decorator class approach template
class decorator_class(object):

  def __init__(self,original_function):
    self.original_function = original_function

  def __call__(self,*vargs,**kwargs):
    # this is the wrapper function
    # do stuff here that you would do inside a wrapper function
    pass
"""
  @decorator_class
  def original_function():
    pass

  The above snippet is the same as --
  
  original_function = decorator_class(original_function)
"""
# The functional way of declaring a decorator is the most common way of doing it
# But some people prefer going with the decorator class approach since it seems well
# organized

"""
  Problems faced while using decorators
 
  Nesting decorators ::

  def decorating_function1():
    def wrapper():
      pass
    return wrapper

  def decorating_function2():
    def wrapper():
      pass
    return wrapper

  @decorating_function1
  @decorating_function2
  def original_function(*vargs,**kwargs):
    pass

  original_function = decorating_function1(decorating_function2(original_function))

  The argument for decorating_function2 is the wrapper function that is returned from
  decorating_function1(original_function)

  We can use the functools module for for @wraps() decoration on the wrapper function
  to retain the information of the original_functon
"""
def decorating_function1(original_function):
  print(original_function.__name__)
  def wrapper(*vargs,**kwargs):
    print('inside wrapper of df1')
    return original_function(*vargs,**kwargs)
  return wrapper

def decorating_function2(original_function):
  print(original_function.__name__)
  def wrapper(*vargs,**kwargs):
    print('inside wrapper of df2 and original_function name = %s' %original_function.__name__)
    return original_function(*vargs,**kwargs)
  return wrapper

#@decorating_function2
#@decorating_function1
def original_function(name,age):
  print("Name of the person is %s and his age is %d" % (name,age))



def main():
  # runningTimeInsertionSort()
  # print(quickieSort([1,3,2],1))
   array = list(map(int,"2 1 3 1 2".split()))
   quicksort(array, beginindex = 0, pivotindex = -1)
  # testingamsbo()
  

# boilerplate code to execute the main()
if __name__ == '__main__':
  main()

  # For testing decorators
  # When we use the function without using decorators
  # original_function('Joshua',21)

  # decorators without that syntactic sugar notation
  # original_function = decorating_function1(original_function)

  # now wrapper function is the function that was named original_function
  # so when I pass in "Sid",24 as the parameters, wrapper("Sid",24) is executed
  # which then executes the print() and original_function("Sid",24) inside it
  # original_function('Sid',24)

  # decorators with syntactic sugar notation
  # @decorating_function1 on original_function()
  # original_function('Wayne', 27)

  # Testing out nested decorators
  # @decorating_function2
  # @decorating_function1
  # over orignal_function
  # original_function = decorating_function2(decorating_function1(original_function))
  # original_function('Sid',24)
