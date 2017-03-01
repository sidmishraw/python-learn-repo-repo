# read_bacteria.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-13 00:48:54
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-26 20:36:13


# from json import loads
# from pprint import pprint


# if __name__ == '__main__':

#   with open('bacteria.json', 'r', encoding='utf-8') as json_file:
#     string = json_file.read()
#     json_string = loads(string)
#     pprint(json_string)
#     reqd_data = json_string['ubiome_bacteriacounts']
#     dict_bac = { bac['taxon']:bac for bac in reqd_data }
#     print(len(reqd_data))
#     print(len(dict_bac))






# working on the hackerrank exercises

# 2D Array - DS
from pprint import pprint

# 6 x 6 2 - D array 
array = []
max_sum = -float('infinity')

if __name__ == '__main__':
  '''
  2D - Array
  '''

  for i in range(0, 6, 1):
    array.append(list(map(int, input().strip().split(' '))))

  i = 0

  while i < 4:

    j = 0
    while j < 4:
      
      a = array[i][j]
      b = array[i][j + 1]
      c = array[i][j + 2]
      d = array[i + 1][j + 1]
      e = array[i + 2][j]
      f = array[i + 2][j + 1]
      g = array[i + 2][j + 2]
      sum_symbol = a + b + c + d + e + f + g
      # print('nbrs = %s, %s, %s, %s, %s, %s, %s' % (a, b, c, d, e, f, g))
      # print('sum = %s' % sum_symbol)
      if sum_symbol >= max_sum:
        max_sum = sum_symbol
      j += 1
    # print('new i')
    i += 1

  print(max_sum)

  

