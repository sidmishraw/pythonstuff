# hackerrank_graphs.py
'A collection of implementations for the problems \
about graphs on hackerrank website'

__author__ = 'sidmishraw'


# Journey to the Moon
# This method is not a follproof method. It required cleaning actions
# making it O(n**2) complexity. Not at all good.
# https://www.hackerrank.com/challenges/journey-to-the-moon
def journey_to_the_moon():
  'implementation of the solution to the problem Journey to the moon\
  on hackerrank website.'
  nbr_astronauts, nbr_edges = list(map(int, input().split(' ')))
  country = 0
  country_dict = {}
  country_edge_count = {}
  for _ in range(0, nbr_edges):
    ast1, ast2 = list(map(int, input().split(' ')))
    # check if the current country exists in our country dict
    if country in country_dict:
      # if yes, check if the astronaut exists in the country
      if ast1 in country_dict[country]:
        # if ast1 is of a particular country, add ast2 to the country set
        country_dict[country].add(ast2)
        country_edge_count[country] += 1
      elif ast2 in country_dict[country]:
        # if ast2 is of a particular country, add ast1 to the country set
        country_dict[country].add(ast1)
        country_edge_count[country] += 1
      else:
        # both the astronauts are not of this country it seems,
        # create a new country and add both of them into it
        country += 1
        country_dict[country] = set()
        country_edge_count[country] = 1
        country_dict[country].add(ast1)
        country_dict[country].add(ast2)
    else:
      # if no, create a new entry for the country in our dict
      # and add the astronauts to the country set.
      country_dict[country] = set()
      country_edge_count[country] = 1
      country_dict[country].add(ast1)
      country_dict[country].add(ast2)
  # The above approach causes problems when we get edges not in particular order
  # to take care of those scenarios, we can use the following approach
  for i in range(0, country + 1, 1):
    if len(country_dict[i]) == 0:
      continue
    for j in range(0, country + 1, 1):
      if i == j or len(country_dict[j]) == 0:
        continue
      # print(country_dict[i], country_dict[j])
      if len(country_dict[i].intersection(country_dict[j])) > 0:
        country_dict[i] = country_dict[i].union(country_dict[j])
        country_dict[j] = set()
  country_dict = dict(filter(lambda x: len(x[1]) > 0, country_dict.items()))
  for i in country_dict.keys():
    if len(country_dict[i]) == 0:
      continue
    for j in country_dict.keys():
      if i == j or len(country_dict[j]) == 0:
        continue
      # print(country_dict[i], country_dict[j])
      if len(country_dict[i].intersection(country_dict[j])) > 0:
        country_dict[i] = country_dict[i].union(country_dict[j])
        country_dict[j] = set()
  country_dict = dict(filter(lambda x: len(x[1]) > 0, country_dict.items()))
  # print(country_dict)
  # print(country_edge_count)
  # now to do the maths.
  # ideally, since we need to select 2 astronauts from 2 different
  # countries, we can compute the total number of possible edges in 
  # the complete graph and subtract the edges formed by the complete
  # graphs of the countries and hence giving us the edges that we want
  # that will be the number of astronaut pairs required.
  # NOTE - the country_edge_count dict is not really necessary now
  # but I've added this in for keeping track of the edges.

  def factorial(nbr):
    'factorial logic'
    fact = 1
    for i in range(1, nbr + 1, 1):
      fact *= i
    return fact

  def nCr(n, r):
    'combination logic'
    n_fact = factorial(n)
    n_minus_r_fact = factorial(n-r)
    r_fact = factorial(r)
    ncr = (n_fact) // (n_minus_r_fact * r_fact)
    return ncr

  same_country_edges = 0
  for astronauts in country_dict.values():
    same_country_edges += nCr(len(astronauts), 2)
  total_possible_edges = nCr(nbr_astronauts, 2)
  possible_pairs_count = total_possible_edges - same_country_edges
  # print('total_possible_edges = %s\nsame_country_edges = %s\n \
  #   possible_pairs_count = %s' % (total_possible_edges, same_country_edges, \
  #     possible_pairs_count))
  print(possible_pairs_count)



def main():
  'main point of entry into this program'
  journey_to_the_moon()

if __name__ == '__main__':
  main()