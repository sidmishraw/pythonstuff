# hackerrank_python_exercises.py
# Python_DS_Suite
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-11 03:29:38
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-11 14:45:09


__author__ = 'sidmishraw'


def find_the_percentage():
  'finding the percentage problem from hackerrank'
  N = int(input())
  student_dict = {}
  for _ in range(0, N, 1):
    input_str = input().strip().split(' ')
    student_name, math, phy, chem = input_str[0], *list(map(int, input_str[1:]))
    student_dict[student_name] = (math + phy + chem) / 3
  name = input()
  print('%.2f' % student_dict[name])


def main():
  'the main function duh!'
  find_the_percentage()



if __name__ == '__main__':
  main()