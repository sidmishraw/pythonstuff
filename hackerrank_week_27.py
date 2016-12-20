# hackerrank week of 27 code challenge solutions

__author__ = 'sidmishraw'



# drawing book problem
def drawing_book():
  'solution for the drawingbook problem'
  n = int(input().strip())
  p = int(input().strip())
  mid = n // 2
  if p <= mid:
    print(p // 2)
  elif p > mid:
    print((n - p) // 2)




def main():
  'main function to execute all the solutions'
  drawing_book()


if __name__ == '__main__':
  main()