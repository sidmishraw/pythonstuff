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


# climbing the leaderboard Codesprint challenge
def ranking_calc2(cache, x, ranking):
  if ranking == 0:
    return 1
  if ranking not in cache:
    return ranking
  if cache[ranking] > x:
    return ranking + 1
  elif cache[ranking] == x:
    return ranking
  else:
    return ranking_calc(cache, x, ranking - 1)

# climbing the leaderboard Codesprint challenge
def ranking_calc(cache, x, srank, lrank):
  if srank >= lrank:
    if cache[srank] <= x:
      return srank
    elif cache[srank] > x:
      return srank + 1
  mid = (srank + lrank) // 2
  print('srank = %s, lrank = %s and mid = %s' % (srank, lrank, mid))
  if cache[mid] == x:
    return mid
  elif cache[mid] < x:
    return ranking_calc(cache, x, srank, mid - 1)
  elif cache[mid] > x:
    return ranking_calc(cache, x, mid + 1, lrank)


# not optimal solution
def climbing_leaderboard():
  'for solving the climbing leaderboard challenge of codesprint'
  n = int(input())
  scores = list(map(int, input().split(" ")))
  m = int(input())
  alices = list(map(int, input().split(" ")))
  score_cache = {}
  ranking = 1
  for score in scores:
    if ranking in score_cache:
      if score_cache[ranking] > score:
        ranking += 1
        score_cache[ranking] = score
    else:
      score_cache[ranking] = score
  for alice in alices:
    ranking_calced = ranking_calc(score_cache, alice, 1, ranking)
    print(ranking_calced)

# not optimal solution
def climbing_leaderboard2():
  'for solving the climbing leaderboard challenge of codesprint'
  n = int(input())
  scores = list(map(int, input().split(" ")))
  m = int(input())
  alices = list(map(int, input().split(" ")))
  ranking = 0
  prev = float('inf')
  for score in scores:
    if score < prev:
      prev = score
      ranking += 1
  for alice in alices:
    rank_index = len(scores) - 1
    rank = ranking
    while rank_index > -1:
      if rank_index == 0:
        print('1')
        break
      elif alice < scores[rank_index]:
        print(rank + 1)
        break
      elif alice == scores[rank_index]:
        print(rank)
        break
      else:
        rank_index -= 1
        if scores[rank_index] > scores[rank_index + 1]:
          rank -= 1


# computes the prime numbers
def is_prime(number):
  'checks if number is prime'
  import math
  if number % 2 == 0 and number > 2: 
    return False
  for i in range(3, int(math.sqrt(number)) + 1, 2):
    if number % i == 0:
      return False
  return True



def find_prime_count(number, digits):
  'computes the number of primes'
  s = str(number)
  wi_index = 0
  wf_index = digits - 1
  while wf_index < len(s):
    dsum = sum(list(map(int, s[wi_index:wf_index])))
    if is_prime(dsum):
      continue
    else:
      return 0



# prime digits sum
def prime_digits_sum():
  'prime digits sum problem from hackerrank'
  q = int(input().strip())
  for _ in range(0, q, 1):
    n = int(input().strip())
    count = 0
    for number in range(10 ** (n - 1), 10 ** n, 1):
      count3 = find_prime_count(number, 3)
      if count3 == 0:
        count = 0
        break
      else:
        count += count3
      count4 = find_prime_count(number, 4)
      if count4 == 0:
        count = 0
        break
      else:
        count += count4
      count5 = find_prime_count(number, 5)
      if count5 == 0:
        count = 0
        break
      else:
        count += count5
    print(count)


# adding a __init__.py inside a package makes it a python package, python doesn't treat
# the folder as a module, instead it behaves like a package.
def main():
  # draw_staircase()
  # circular_array_rotation()
  # gridland_metro()
  # lonely_integer()
  # missing_numbers()
  # pairs()
  # climbing_leaderboard()
  prime_digits_sum()

if __name__ == '__main__':
  main()

