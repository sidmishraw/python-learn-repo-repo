# hrank.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-26 22:58:35
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-01 23:31:26


# The inbetween or Between 2 sets problem

def gcd(larger_nbr, smaller_nbr):
  '''
  Computes the GCD of the 2 input nbrs
  '''
  if larger_nbr % smaller_nbr == 0:
    return smaller_nbr
  else:
    return gcd(smaller_nbr, larger_nbr % smaller_nbr)

def lcm(nbr1, nbr2):
  '''
  Computes the LCM of the 2 input nbrs
  '''
  larger_nbr = nbr1 if nbr1 > nbr2 else nbr2
  smaller_nbr = nbr2 if nbr2 < nbr1 else nbr1
  lcm = (larger_nbr * smaller_nbr) // gcd(larger_nbr, smaller_nbr)
  return lcm

def lcm_list(lst_nbrs):
  '''
  Computes the LCM of the list of nbrs
  '''
  lcm_seeder = lcm(lst_nbrs[0], lst_nbrs[1])
  index = 2
  while index < len(lst_nbrs):
    lcm_seeder = lcm(lcm_seeder, lst_nbrs[index])
    index += 1
  return lcm_seeder
  
def gcd_list(lst_nbrs):
  '''
  Computes the GCD of the list of nbrs, given that
  lst_nbrs is sorted in ascending order
  '''
  gcd_seeder = gcd(lst_nbrs[1], lst_nbrs[0])
  index = 2
  while index < len(lst_nbrs):
    gcd_seeder = gcd(lst_nbrs[index], gcd_seeder)
    index += 1
  return gcd_seeder


# if __name__ == '__main__':
#   '''
#   The in-between
#   '''
#   n, m = list(map(int, input().strip().split(' ')))
#   # sorted in ascending order
#   a = sorted(list(map(int, input().strip().split(' '))))
#   # sorted in ascending order
#   b = sorted(list(map(int, input().strip().split(' '))))
#   lcm_a = lcm_list(a)
#   gcd_b = gcd_list(b)
#   print(counter)



# matrix layer rotation


def rotate_layer(layer_nbr, matrix, m, n):
  '''
  Rotates the layer denoted by the layer nbr of the given
  matrix and m,n where m is nbr of rows and n is nbr of cols of the 
  matrix
  '''
  tmp = matrix[layer_nbr][layer_nbr]
  # rotate top surface
  i = layer_nbr
  j = layer_nbr
  while j < n - 1 - layer_nbr:
    matrix[i][j] = matrix[i][j + 1]
    j += 1
  # rotate right surface
  while i < m - 1 - layer_nbr:
    matrix[i][j] = matrix[i + 1][j]
    i += 1
  # rotate bottom surface
  while layer_nbr < j:
    matrix[i][j] = matrix[i][j - 1]
    j -= 1
  # rotate left surface
  while layer_nbr < i:
    matrix[i][j] = matrix[i - 1][j]
    i -= 1
  matrix[layer_nbr + 1][layer_nbr] = tmp


def count_nbr_layers(m, n):
  count = 0
  while m > 0 and n > 0:
    count += 1
    m -= 2
    n -= 2
  return count


def print_matrix(matrix):
  return '\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), matrix)))
    
# The inbetween or Between 2 sets problem

def gcd(larger_nbr, smaller_nbr):
  '''
  Computes the GCD of the 2 input nbrs
  '''
  if larger_nbr % smaller_nbr == 0:
    return smaller_nbr
  else:
    return gcd(smaller_nbr, larger_nbr % smaller_nbr)

def lcm(nbr1, nbr2):
  '''
  Computes the LCM of the 2 input nbrs
  '''
  larger_nbr = nbr1 if nbr1 > nbr2 else nbr2
  smaller_nbr = nbr2 if nbr2 < nbr1 else nbr1
  lcm = (larger_nbr * smaller_nbr) // gcd(larger_nbr, smaller_nbr)
  return lcm

def lcm_list(lst_nbrs):
  '''
  Computes the LCM of the list of nbrs
  '''
  if len(lst_nbrs) < 2:
    return lst_nbrs[-1]

  lcm_seeder = lcm(lst_nbrs[0], lst_nbrs[1])
  index = 2
  while index < len(lst_nbrs):
    lcm_seeder = lcm(lcm_seeder, lst_nbrs[index])
    index += 1
  return lcm_seeder
  
def gcd_list(lst_nbrs):
  '''
  Computes the GCD of the list of nbrs, given that
  lst_nbrs is sorted in ascending order
  '''
  if len(lst_nbrs) < 2:
    return lst_nbrs[-1]

  gcd_seeder = gcd(lst_nbrs[1], lst_nbrs[0])
  index = 2
  while index < len(lst_nbrs):
    gcd_seeder = gcd(lst_nbrs[index], gcd_seeder)
    index += 1
  return gcd_seeder

if __name__ == '__main__':
  m, n, r = list(map(int, input().strip().split(' ')))
  matrix = []
  for _ in range(0, m, 1):
    matrix.append(list(map(int, input().strip().split(' '))))
    
  nbr_layers = count_nbr_layers(m, n)

  effective_rotations_lyr_0 = 2 * m + 2 * n - 4
  
  effective_rotations_list = [ effective_rotations_lyr_0 - i * 8 for i in range(0, nbr_layers, 1) ]
  
  complete_rotation_nbr = lcm_list(effective_rotations_list)
  
  effective_r = r % complete_rotation_nbr

  print('effective_rotations_lyr_0 = {}, effective_rotations_list= {}, complete_rotation_nbr = {},\
  effective_r = {} '.format(effective_rotations_lyr_0, \
    effective_rotations_list, complete_rotation_nbr, effective_r))
  
  for _ in range(0, effective_r, 1):
    # run the rotation on all layers r nbr of times
    for layer_nbr in range(0, nbr_layers, 1):
      rotate_layer(layer_nbr, matrix, m, n)
  print(print_matrix(matrix))
      



