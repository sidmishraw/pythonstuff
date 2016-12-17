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


def main():
  #draw_staircase()
  #circular_array_rotation()
  gridland_metro()

if __name__ == '__main__':
  main()

