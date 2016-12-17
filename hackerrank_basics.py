# basic problems from hackerrank algorithms section
__author__ = 'sidmishraw'




def draw_staircase():
  'draws a staitcase using # and spaces for the given n, n = width and height'
  n = int(input())
  for i in range(1, n + 1, 1):
    drawing = '%s%s' % (' '* (n - i), '#' * i)
    print(drawing)


def circular_array_rotationv1():
  'does the circular array rotation as mentioned in hackerrank problem and solves\
  the queries. v1.0, this version is easy but slow. Optimized using a pointer'
  n, k, q = list(map(int, input().split(" ")))
  array = list(map(int, input().split(" ")))
  m_s = []
  for _ in range(0, q, 1):
    m_s.append(int(input()))
  for _ in range(0, k, 1):
    last = array.pop()
    array = [last] + array
  for m in m_s:
    print(array[m])

# uses an index pointer pointing to the start after rotation
def circular_array_rotation():
  'does the circular array rotation as mentioned in hackerrank problem and solves\
  the queries.'
  n, k, q = list(map(int, input().split(" ")))
  array = list(map(int, input().split(" ")))
  m_s = []
  for _ in range(0, q, 1):
    m_s.append(int(input()))
  start_index = 0
  for _ in range(0, k, 1):
    start_index -= 1
  for m in m_s:
    print(array[(m + start_index) % n])

# train track and lighting problem
# Gridland metro
# Note - it is better to go with dictionary when using
# count sort technique, since there looping is not heavy. Non 0 counts are lesser.
def gridland_metro():
  'solution for the gridland metro problem on hackerrank'
  n, m, k = tuple(map(int, input().split(" ")))
  # grid = [[ 0 for _ in range(0, m, 1)] for _ in range(0, n, 1)]
  grid = {}
  post_count = m * n
  for _ in range(0, k, 1):
    r, c1, c2 = tuple(map(int, input().split(" ")))
    if r in grid:
      c1_old, c2_old = grid[r]
      if c1 < c1_old and c2 > c2_old:
        grid[r] = (c1, c2)
        post_count = post_count - ((c2 - c2_old) + (c1_old - c1))
      elif c1 < c1_old and c2 <= c2_old:
        grid[r] = (c1, c2_old)
        if c1 == c2:
          post_count = post_count - 1
        else:
          post_count = post_count - (c1_old - c1)
      elif c1 >= c1_old and c2 > c2_old:
        grid[r] = (c1_old, c2)
        if c1 == c2:
          post_count = post_count - 1
        else:
          post_count = post_count - (c2 - c2_old)
    else:
      grid[r] = (c1, c2)
      post_count = post_count - (c2 - c1 + 1)
    print(grid)
    print(post_count)

# lonely integer problem from hackerrank
def lonely_integer():
  n = int(input())
  array = list(map(int, input().split(" ")))
  cache = {}
  for e in array:
    if e in cache:
      cache[e] += 1
    else:
      cache[e] = 1
  for key, value in cache.items():
    if value == 1:
      print(key)
      break

# missing numbers problem from hackerrank
def missing_numbers():
  n = int(input())
  A = list(map(int, input().split(' ')))
  m = int(input())
  B  = list(map(int, input().split(' ')))
  cacheA = {}
  cacheB = {}
  for e in A:
    if e not in cacheA:
      cacheA[e] = 1
    else:
      cacheA[e] += 1
  for e in B:
    if e not in cacheB:
      cacheB[e] = 1
    else:
      cacheB[e] += 1
  for key, freq in cacheB.items():
    if key not in cacheA or cacheA[key] < freq:
      print(key)

 
# pairs problem from hackerrank
def pairs():
  'counts the number of pairs with difference k'
  n, k = tuple(map(int, input().strip(" ").split(' ')))
  array = list(map(int, input().strip(" ").split(' ')))
  parsed_cache = set()
  count = 0
  for e in array:
    less = e - k
    if e not in parsed_cache:
      parsed_cache.add(e)
    else:
      count += 1
    if less in parsed_cache:
      count += 1
    else:
      parsed_cache.add(less)
  print(count)


# adding a __init__.py inside a package makes it a python package, python doesn't treat
# the folder as a module, instead it behaves like a package.
def main():
  # draw_staircase()
  # circular_array_rotation()
  # gridland_metro()
  # lonely_integer()
  # missing_numbers()
  pairs()

if __name__ == '__main__':
  main()

