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


# tailor shop problem
def update_cache(cache, m, mincost):
  if m not in cache:
    cache.add(m)
    return
  else:
    return update_cache(cache, m + 1, mincost)

def tailor_shop():
  'solution for the tailor shop problem on code week 27'
  import math
  n, p = tuple(map(int, input().strip().split(" ")))
  a = list(map(int, input().strip().split(' ')))
  cache = set()
  for mincost in a:
    m = math.ceil(mincost / p)
    print('m = %s cache = %s' % (m, cache))
    update_cache(cache, m, mincost)
  min_nbr = sum(cache)
  print(min_nbr)


def main():
  'main function to execute all the solutions'
  # drawing_book()
  tailor_shop()


if __name__ == '__main__':
  main()