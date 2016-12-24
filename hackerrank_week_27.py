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

  size, cost = tuple(map(int, input().strip().split(" ")))
  min_cost_array = list(map(int, input().strip().split(' ')))
  min_count_array = list(map(lambda x: math.ceil(x / cost), min_cost_array))

  print(min_count_array)

  history = set()

  for x in min_count_array:

    history_size = len(history)

    for _ in range(0, history_size + 1, 1):

      if x not in history:
        history.add(x)
        break
      else:
        x += 1

  print(sum(history))


def main():
  'main function to execute all the solutions'
  # drawing_book()
  tailor_shop()


if __name__ == '__main__':
  main()