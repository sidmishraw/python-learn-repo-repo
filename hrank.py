# hrank.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-26 22:58:35
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-03 12:30:49


# # The inbetween or Between 2 sets problem

# def gcd(larger_nbr, smaller_nbr):
#   '''
#   Computes the GCD of the 2 input nbrs
#   '''
#   if larger_nbr % smaller_nbr == 0:
#     return smaller_nbr
#   else:
#     return gcd(smaller_nbr, larger_nbr % smaller_nbr)

# def lcm(nbr1, nbr2):
#   '''
#   Computes the LCM of the 2 input nbrs
#   '''
#   larger_nbr = nbr1 if nbr1 > nbr2 else nbr2
#   smaller_nbr = nbr2 if nbr2 < nbr1 else nbr1
#   lcm = (larger_nbr * smaller_nbr) // gcd(larger_nbr, smaller_nbr)
#   return lcm

# def lcm_list(lst_nbrs):
#   '''
#   Computes the LCM of the list of nbrs
#   '''
#   lcm_seeder = lcm(lst_nbrs[0], lst_nbrs[1])
#   index = 2
#   while index < len(lst_nbrs):
#     lcm_seeder = lcm(lcm_seeder, lst_nbrs[index])
#     index += 1
#   return lcm_seeder
  
# def gcd_list(lst_nbrs):
#   '''
#   Computes the GCD of the list of nbrs, given that
#   lst_nbrs is sorted in ascending order
#   '''
#   gcd_seeder = gcd(lst_nbrs[1], lst_nbrs[0])
#   index = 2
#   while index < len(lst_nbrs):
#     gcd_seeder = gcd(lst_nbrs[index], gcd_seeder)
#     index += 1
#   return gcd_seeder


# # if __name__ == '__main__':
# #   '''
# #   The in-between
# #   '''
# #   n, m = list(map(int, input().strip().split(' ')))
# #   # sorted in ascending order
# #   a = sorted(list(map(int, input().strip().split(' '))))
# #   # sorted in ascending order
# #   b = sorted(list(map(int, input().strip().split(' '))))
# #   lcm_a = lcm_list(a)
# #   gcd_b = gcd_list(b)
# #   print(counter)



# # matrix layer rotation
# def rotate_layer(layer_nbr, matrix, m, n):
#   '''
#   Rotates the layer denoted by the layer nbr of the given
#   matrix and m,n where m is nbr of rows and n is nbr of cols of the 
#   matrix
#   '''
#   tmp = matrix[layer_nbr][layer_nbr]
#   # rotate top surface
#   i = layer_nbr
#   j = layer_nbr
#   while j < n - 1 - layer_nbr:
#     matrix[i][j] = matrix[i][j + 1]
#     j += 1
#   # rotate right surface
#   while i < m - 1 - layer_nbr:
#     matrix[i][j] = matrix[i + 1][j]
#     i += 1
#   # rotate bottom surface
#   while layer_nbr < j:
#     matrix[i][j] = matrix[i][j - 1]
#     j -= 1
#   # rotate left surface
#   while layer_nbr < i:
#     matrix[i][j] = matrix[i - 1][j]
#     i -= 1
#   matrix[layer_nbr + 1][layer_nbr] = tmp


# def count_nbr_layers(m, n):
#   count = 0
#   while m > 0 and n > 0:
#     count += 1
#     m -= 2
#     n -= 2
#   return count


# def print_matrix(matrix):
#   return '\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), matrix)))
    
# # The inbetween or Between 2 sets problem

# def gcd(larger_nbr, smaller_nbr):
#   '''
#   Computes the GCD of the 2 input nbrs
#   '''
#   if larger_nbr % smaller_nbr == 0:
#     return smaller_nbr
#   else:
#     return gcd(smaller_nbr, larger_nbr % smaller_nbr)

# def lcm(nbr1, nbr2):
#   '''
#   Computes the LCM of the 2 input nbrs
#   '''
#   larger_nbr = nbr1 if nbr1 > nbr2 else nbr2
#   smaller_nbr = nbr2 if nbr2 < nbr1 else nbr1
#   lcm = (larger_nbr * smaller_nbr) // gcd(larger_nbr, smaller_nbr)
#   return lcm

# def lcm_list(lst_nbrs):
#   '''
#   Computes the LCM of the list of nbrs
#   '''
#   if len(lst_nbrs) < 2:
#     return lst_nbrs[-1]

#   lcm_seeder = lcm(lst_nbrs[0], lst_nbrs[1])
#   index = 2
#   while index < len(lst_nbrs):
#     lcm_seeder = lcm(lcm_seeder, lst_nbrs[index])
#     index += 1
#   return lcm_seeder
  
# def gcd_list(lst_nbrs):
#   '''
#   Computes the GCD of the list of nbrs, given that
#   lst_nbrs is sorted in ascending order
#   '''
#   if len(lst_nbrs) < 2:
#     return lst_nbrs[-1]

#   gcd_seeder = gcd(lst_nbrs[1], lst_nbrs[0])
#   index = 2
#   while index < len(lst_nbrs):
#     gcd_seeder = gcd(lst_nbrs[index], gcd_seeder)
#     index += 1
#   return gcd_seeder

# if __name__ == '__main__':
#   m, n, r = list(map(int, input().strip().split(' ')))
#   matrix = []
#   for _ in range(0, m, 1):
#     matrix.append(list(map(int, input().strip().split(' '))))
    
#   nbr_layers = count_nbr_layers(m, n)

#   effective_rotations_lyr_0 = 2 * m + 2 * n - 4
  
#   effective_rotations_list = [ effective_rotations_lyr_0 - i * 8 for i in range(0, nbr_layers, 1) ]
  
#   complete_rotation_nbr = lcm_list(effective_rotations_list)
  
#   effective_r = r % complete_rotation_nbr

#   print('effective_rotations_lyr_0 = {}, effective_rotations_list= {}, complete_rotation_nbr = {},\
#   effective_r = {} '.format(effective_rotations_lyr_0, \
#     effective_rotations_list, complete_rotation_nbr, effective_r))
  
#   for _ in range(0, effective_r, 1):
#     # run the rotation on all layers r nbr of times
#     for layer_nbr in range(0, nbr_layers, 1):
#       rotate_layer(layer_nbr, matrix, m, n)
#   print(print_matrix(matrix))
      


# # check parentheses is balanced.
# def check_paren_balance(string):
#   '''
#   Checks if the parenthesis are balanced.
#   '''
#   stack_paren = []
#   for c in string:
#     if len(stack_paren) == 0:
#       stack_paren.append(c)
#     else:
#       if c == ']' and stack_paren[-1] == '[' \
#       or c == ')' and stack_paren[-1] == '(' \
#       or c == '}' and stack_paren[-1] == '{': 
#         stack_paren.pop()
#       else:
#         stack_paren.append(c)
#   if len(stack_paren) != 0:
#     return 'NO'
#   else:
#     return 'YES'



# if __name__ == '__main__':
#   string = '[][][][][{{{{{{{{{))))))}}}}'


# # queue using 2 stacks
# class MyQueue(object):
#   '''
#   Queue implemented using 2 stacks.
#   '''

#   def __init__(self):
#     self.stack1 = []
#     self.stack2 = []

#   def peek(self):
#     pass

#   def pop(self):
#     pass

#   def put(self, value):
#     pass


# if __name__ == '__main__':
#   queue = MyQueue()
#   t = int(input().strip())
#   for line in range(t):
#       values = list(map(int, input().strip().split(' ')))
#       if values[0] == 1:
#           queue.put(values[1])        
#       elif values[0] == 2:
#           queue.pop()
#       else:
#           print(queue.peek())





# # Palindromic Permutations of a string
# def permute_fhalf(string, lindex, rindex, perms):
#   if lindex >= rindex:
#     perms.add(''.join(string))
#     return
#   i = 0
#   while i < rindex:
#     string[lindex], string[i] = string[i], string[lindex]
#     permute_fhalf(string, lindex + 1, rindex, perms)
#     string[lindex], string[i] = string[i], string[lindex]
#     i += 1


# def permute(first_half, odd_char):
#   '''
#   Permutes the first half of the string and attaches the odd char in the
#   middle and follows it up with the reversed permutation of the string.
#   '''
#   perms = set()
#   permute_fhalf(first_half, 0, len(first_half), perms)
#   permuted_strings = []
#   for s in perms:
#     permuted_strings.append(''.join([s, odd_char, ''.join(reversed(s))]))
#   return permuted_strings


# def gen_palindromic_permutations(string):
#   '''
#   Generates palindromic permutations of the given string.
#   '''
#   dict_cache = {}
#   palindromes = []

#   for c in string:
#     if c not in dict_cache:
#       dict_cache[c] = 1
#     else:
#       dict_cache[c] += 1

#   count_odd = None

#   if len(string) % 2 == 0:
#     count_odd = 0
#   else:
#     count_odd = 1

#   for item in dict_cache.items():
#     if item[1] % 2 != 0:
#       count_odd -= 1

#   if count_odd < 0:
#     return palindromes

#   # take half frequency of the string as the base string
#   # permute it and add the reverse of the first half with the
#   # odd numbered char at the middle
#   first_half = []
#   odd_char = ''
#   for item in dict_cache.items():
#     if item[1] % 2 != 0:
#       odd_char = item[0]
#     for _ in range(0, item[1] // 2, 1):
#       first_half.append(item[0])
#   palindromes = permute(list(first_half), odd_char)
#   return palindromes



# if __name__ == '__main__':
#   string = 'abba'



# # LinkedList - kth node
# class Node(object):

#   def __init__(self, data = None, next = None):
#     self.data = data
#     self.next = next

# class LinkedList(object):

#   def __init__(self):
#     self.start = None

#   def add(self, data):
#     self.start = Node(data, self.start)
#     return

#   def __str__(self):
#     current = self.start
#     s = ''
#     while current != None:
#       s += str(current.data) + ' '
#       current = current.next
#     return s

#   def kth_element(self, k):
#     current = self.start
#     fast_r = current
#     for _ in range(0, k, 1):
#       if fast_r != None:
#         fast_r = fast_r.next
#       else:
#         return None
#     if fast_r == None:
#       return None
#     while fast_r.next != None:
#       current = current.next
#       fast_r = fast_r.next
#     return current.data

# if __name__ == '__main__':
#   l = LinkedList()
#   l.add(1)
#   l.add(2)
#   l.add(3)
#   l.add(4)
#   l.add(5)


class Node(object):

  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def create_min_bst(self, arr, lindex, rindex):
    if rindex < lindex:
      return
    mid = (lindex + rindex) // 2
    self.data = arr[mid]
    self.left = Node()
    self.left.create_min_bst(arr, lindex, mid - 1)
    self.right = Node()
    self.right.create_min_bst(arr, mid + 1, rindex)

  def traverse(self, arr):
    if self.left != None:
      self.left.traverse(arr)
    arr.append(str(self.data) if self.data != None else '')
    if self.right != None:
      self.right.traverse(arr)

class Tree(object):
  def __init__(self):
    self.root = None

  def create_min_bst(self, arr):
    if self.root == None:
      self.root = Node()
    self.root.create_min_bst(arr, 0, len(arr) - 1)

  def __repr__(self):
    nodes = []
    if self.root != None:
      self.root.traverse(nodes)
    return ' '.join(nodes)



