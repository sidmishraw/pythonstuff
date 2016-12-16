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
  the queries. v1.0'
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



def main():
  #draw_staircase()
  circular_array_rotation()

if __name__ == '__main__':
  main()