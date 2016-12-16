# basic problems from hackerrank algorithms section
__author__ = 'sidmishraw'




def draw_staircase():
  'draws a staitcase using # and spaces for the given n, n = width and height'
  n = int(input())
  for i in range(1, n + 1, 1):
    drawing = '%s%s' % (' '* (n - i), '#' * i)
    print(drawing)

def main():
  draw_staircase()

if __name__ == '__main__':
  main()