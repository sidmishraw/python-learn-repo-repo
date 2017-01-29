# testing_cci.py
# # -*- coding: utf-8 -*-
# # @Author: Sidharth Mishra
# # @Date:   2017-01-20 14:42:42
# # @Last Modified by:   Sidharth Mishra
# # @Last Modified time: 2017-01-26 22:57:35

# import re

# def precedence(operator1, operator2):
#   'checks the precedence of the operators, returns true if operator1\
#    has higher precedence else false'
#   if operator1 == '+' and (operator2 == '*' or operator2 == '/'):
#     return False
#   elif operator1 == '-' and (operator2 == '*' or operator2 == '/'):
#     return False
#   elif operator1 == '*' and (operator2 == '*' or operator2 == '/'):
#     return False
#   elif operator1 == '/' and (operator2 == '*' or operator2 == '/'):
#     return False
#   elif operator1 == '-' and operator2 == '-':
#     return False
#   elif operator1 == '+' and operator2 == '+':
#     return False
#   else:
#     return True

# def evaluate(operand1, operand2, operator):
#   'evaluates the expression'
#   if operator == '+':
#     return operand1 + operand2
#   elif operator == '-':
#     return operand1 - operand2
#   elif operator == '*':
#     return operand1 * operand2
#   elif operator == '/':
#     return operand1 / operand2



# if __name__ == '__main__':
#   # expression evaluation   
#   operand_stack = []
#   operator_stack = []
#   expression = input().strip()
#   operands = list(map(int, list(filter((lambda x: x != ''), re.split(r'[\+\-\/\*]'\
#     , expression)))))
#   operators = list(filter((lambda x: x != ''), re.split(r'\d', expression)))
#   print(operands)
#   print(operators)
#   # initial phase
#   i = 0
#   while len(operands) != 0:
#     if (i - 1) % 2 == 0:
#       operator = operators.pop(0)
#       if len(operator_stack) == 0:
#         operator_stack.append(operator)
#       elif precedence(operator, operator_stack[-1]):
#         operator_stack.append(operator)
#       else:
#         popped_operator = operator_stack.pop()
#         operator_stack.append(operator)
#         operand2 = operand_stack.pop()
#         operand1 = operand_stack.pop()
#         operand_stack.append(evaluate(operand1, operand2, popped_operator))
#     else:
#       operand = operands.pop(0)
#       operand_stack.append(operand)
#     print(operator_stack)
#     print(operand_stack)
#     i += 1

#   # final unwinding the stack
#   while len(operator_stack) != 0:
#     operand2 = operand_stack.pop()
#     operand1 = operand_stack.pop()
#     operator = operator_stack.pop()
#     result = evaluate(operand1, operand2, operator)
#     operand_stack.append(result)
  
#   print(operand_stack.pop())




# if __name__ == '__main__':
#   # bubble sort
#   arr = [9, 2, 1, 3, 4, 5, 7, 16, 12, 15, 18, 6]
#   length = len(arr)
#   for i in range(0, length, 1):
#     for j in range(i + 1, length, 1):
#       if arr[i] > arr[j]:
#         arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
#   print('final {}'.format(arr))




# if  __name__ == '__main__':
#   # selection sort
#   arr = [9, 2, 1, 3, 4, 5, 7, 16, 12, 15, 18, 6]
#   length = len(arr)
#   min = float('infinity')
#   minindex = 0
#   for i in range(0, length, 1):
#     for j in range(i, length, 1):
#       if arr[j] < min:
#         min = arr[j]
#         minindex = j
#     arr[minindex], arr[i] = arr[i], arr[minindex]
#     min = float('infinity')
#     print(arr)
#   print('final %s ' % arr)




# def mergesort(arr, helper, lindex, rindex):
#   'partitions and merges the arrays'
#   if lindex >= rindex:
#     return [arr[lindex]]

#   mid = (lindex + rindex) // 2
#   larr = mergesort(arr, helper, lindex, mid)
#   rarr = mergesort(arr, helper, mid + 1, rindex)
#   return merge(larr, rarr)

# def merge(larr, rarr):
#   'merges the partitioned arrays'
#   merged = []
#   i,j = 0, 0
#   print('larr = {}'.format(larr),\
#   'rarr = {}'.format(rarr))

#   while i < len(larr) and j < len(rarr):
#     if larr[i] <= rarr[j]:
#       merged.append(larr[i])
#       i += 1
#     else:
#       merged.append(rarr[j])
#       j += 1

#   if i < len(larr):
#     while i < len(larr):
#       merged.append(larr[i])
#       i += 1
#   elif j < len(rarr):
#     while j < len(rarr):
#       merged.append(rarr[j])
#       j += 1

#   return merged

  


# if __name__ == '__main__':
#   # merge sort
#   arr = [9, 2, 1, 3, 4, 5, 7, 16, 12, 15, 18, 6]
#   print(mergesort(arr, helper, 0, len(arr) - 1))


# def quicksort(arr, lindex, rindex, pivotindex):
#   'quick sort'

#   if lindex >= rindex:
#     return

#   i = lindex
#   j = lindex

#   while j < rindex:
#     if arr[j] < arr[pivotindex]:
#       arr[i], arr[j] = arr[j], arr[i]
#       i += 1
#     j += 1

#   arr[i], arr[pivotindex] = arr[pivotindex], arr[i]

#   # since the element at index i is already at its
#   # desired place
#   quicksort(arr, lindex, i - 1, i - 1)
#   quicksort(arr, i + 1, rindex, rindex)

# if __name__ == '__main__':
#   # quick sort or pivot sort
#   arr = [9, 2, 1, 3, 4, 5, 7, 16, 12, 15, 18, 6]
#   quicksort(arr, 0, len(arr) - 1, len(arr) - 1)



# # cracking the code interview problems
# # merge sort - alternative
# def right_shift(A, j):
#   for i in range(len(A) - 1, j, -1):
#     A[i] = A[i - 1]


# if __name__ == '__main__':
#   A = [5, 6, 7, 8, -1, -1, -1, -1]
#   B = [1, 2, 3, 4]
#   i, j = 0, 0
#   while i < len(B) and j < len(A):
#     if B[i] <= A[j]:
#       right_shift(A, j)
#       A[j] = B[i]
#       i += 1
#       j += 1
#     else:
#       j += 1
#   if len(B) - i > 0:
#     while i < len(B):
#       A[i] = B[i]
#       i += 1

#   print(A, B)


# binary tree serialize deserialize

# class Node:

#   def __init__(self, data=None, left=None, right=None):
#     self.data = data
#     self.left = left
#     self.right = right

#   def build(self, strg):
#     'builds the node from the incoming string'
#     if strg[0] == '#':
#       return
#     self.data = strg[0]
#     del strg[0]
#     # build left subtree
#     if strg[0] == '#':
#       del strg[0]
#     else:
#       self.left = self.__class__()
#       self.left.build(strg)
#     # build right subtree
#     if strg[0] == '#':
#       del strg[0]
#     else:
#       self.right = self.__class__()
#       self.right.build(strg)

#   def serialize(self, strg):
#     'serializes the binary tree in preorder'
#     strg.append(str(self.data))
#     if self.left == None:
#       strg.append('#')
#     else:
#       self.left.serialize(strg)
#     if self.right == None:
#       strg.append('#')
#     else:
#       self.right.serialize(strg)



# class Tree:

#   def __init__(self):
#     self.root = None

#   def deserialize(self, string):
#     '''
#     Builds the binary tree from the given string of specific format
#     1,2,4,#,#,5,#,#,3,#,6,7,#,#,#
#     traversal is done preorder since root is needed
#     '''
#     self.root = Node()
#     strg = string.split(',')
#     self.root.build(strg)

#   def serialize(self):
#     if self.root == None:
#       return '#'
#     strg = []
#     self.root.serialize(strg)
#     return ','.join(strg)





# if __name__ == '__main__':
#   string = '1,2,4,#,#,5,#,#,3,#,6,7,#,#,#'
#   t = Tree()
#   t.deserialize(string)
#   print('input string = {}, serialized string = {}'.\
#     format(string, t.serialize()))


# HashMap implementation
# class Node:

#   def __init__(self, key, value):
#     self.key = key
#     self.value = value

#   def __eq__(self, other):
#     return type(self) == type(other) and self.key == other.key

#   def __str__(self):
#     return '({}-->{})'.format(self.key, self.value)

# class HashMap:

#   def __init__(self):
#     # the capacity
#     self.capacity = 10
#     # the hashtable, implements chaining
#     self.table = [ None for _ in range(self.capacity) ]
#     # load factor for resizing the hashmap
#     self.load_factor = 0.7
#     # the current size
#     self.size = 0 


#   def overwrite_node(self, hashvalue, node):
#     'if key is present, overwrite it else add it'
#     for e in self.table[hashvalue]:
#       if e.key == node.key:
#         e.value = node.value
#         return

#     self.table[hashvalue].append(node)


#   def put(self, key, value):
#     'puts the key,value in hashmap, overwrite old value'

#     self.check_size_resize_rehash()

#     hashvalue = self.compute_hash(key)

#     node = Node(key, value)

#     if self.table[hashvalue] == None:
#       # since duplicate values need 
#       self.table[hashvalue] = [node]
#     else:
#       self.overwrite_node(hashvalue, node)

#     self.size += 1


#   def check_size_resize_rehash(self):
#     'checks the size and resizes the hashmap according to thr\
#     load factor'

#     if self.size >= (self.load_factor * self.capacity):
#       # double the capacity
#       self.capacity *= 2
#       # copy the oldtable
#       oldtable = list(self.table)
#       self.table = [ None for _ in range(self.capacity) ]
#       self.size = 0
#       self.copy_contents(oldtable)

  

#   def compute_hash(self, key):
#     'computes the hash'
#     return abs(hash(key)) % self.capacity


#   def copy_contents(self, oldtable):
#     'rehashes and copies the old content from oldtable to new table'
#     for nodes in oldtable:
#       if nodes != None:
#         for node in nodes:
#           self.put(node.key, node.value)


#   def get(self, key):
#     'gets the value for the key from the hashmap'

#     hashvalue = self.compute_hash(key)

#     if self.table[hashvalue] == None or \
#     len(self.table[hashvalue]) == 0:
#       raise KeyError('Key not found')
#     else:
#       for node in self.table[hashvalue]:
#         if node.key == key:
#           return node.value


#   def remove(self, key):
#     'removes the key, value from hashmap'

#     hashvalue = self.compute_hash(key)

#     if self.table[hashvalue] == None:
#       raise KeyError('Key not found')
#     else:
#       for index in range(len(self.table[hashvalue])):
#         if self.table[hashvalue][index].key == key:
#           del self.table[hashvalue][index]
#           self.size -= 1
#           return


# if __name__ == '__main__':
#   h = HashMap()

#   for i in range(0, 10):
#     h.put(i, 1)


# string check dict, uber question

# def check_string(string, dictionary):
#   '''checks if the string can be broken down into
#   one or more space words from the dict.
#   "leetcode" = "leet code" for dict = {leet, code}
#   '''
#   if string == '' or len(dictionary) == 0:
#     return False
#   if string in dictionary:
#     return True
#   key = dictionary.pop()
#   string = ''.join(string.split(key))
#   return check_string(string, dictionary)


# if __name__ == '__main__':
#   string = 'leetcode'
#   dict1 = {'leet', 'code'}
#   print('YES' if check_string(string, dict1) else 'NO')
#   string = 'tobeornottobe'
#   print('YES' if check_string(string, dict1) else 'NO



# # without using hashing or any DS
# def bsearch(l, lindex, rindex, key):
#   if lindex >= rindex:
#     return False
#   mid = (lindex + rindex) // 2
#   if l[mid] == key:
#     return True
#   elif key < l[mid]:
#     return bsearch(l, lindex, mid - 1, key)
#   else:
#     return bsearch(l, mid + 1, rindex, key)


# # without using hashing or any DS
# def check_distinct(string_list, lindex):
#   if len(string_list[lindex:]) < 2:
#     return True
#   if bsearch(string_list, lindex + 1, \
#     len(string_list) - 1, string_list[lindex]):
#     return False
#   return check_distinct(string_list, lindex + 1)


# # using hashing, the lindex is never going to be used anyways
# def check_distinct(string_list, lindex):
#   dictionary = {}
#   for c in string_list:
#     if c not in dictionary:
#       dictionary[c] = 1
#     else:
#       return False
#   return True


# if __name__ == '__main__':
#   string = 'kangaroo'
#   print(check_distinct(list(string), 0))
#   string = 'bad'
#   print(check_distinct(list(string), 0))
#   string = 'a'
#   print(check_distinct(list(string), 0))



# URLify
# easy
# if __name__ == '__main__':
#   s = 'Mr John Smith'
#   s = '%20'.join(s.split(' '))
#   print(s)

# # harder approach
# def right_shift_2sp(string_list, lindex):
#   for _ in range(0,2):
#     for i in range(len(string_list) - 1, lindex, -1):
#       string_list[i] = string_list[i - 1]

# def replace_space(string):
#   string_list = list(string)
#   for c in enumerate(string_list):
#     if c[1] == ' ':
#       right_shift_2sp(string_list, c[0])
#       string_list[c[0]] = '%'
#       string_list[c[0] + 1] = '2'
#       string_list[c[0] + 2] = '0'
#   return ''.join(string_list)

# if __name__ == '__main__':
#   s = 'Mr John Smith    '
#   print(replace_space(s))



# if __name__ == '__main__':
#   string = input().strip().lower()
#   a_dict = {}
#   actual_len = 0
#   for c in string:
#     if c == ' ':
#       continue
#     actual_len += 1
#     if c not in a_dict:
#       a_dict[c] = 1
#     else:
#       a_dict[c] += 1
#   count_odd = 1 if (actual_len % 2) != 0 else 0
#   print(count_odd)
#   print(a_dict)
#   for item in a_dict.items():
#     print(item)
#     if item[1] % 2 != 0:
#       count_odd -= 1
#     if count_odd < 0:
#       break
#   print(count_odd)
#   print('NO' if count_odd < 0 else 'YES')



# # one away

# def check_edits(s1, s2):
#   if abs(len(s1) - len(s2)) > 1:
#     return False
#   a_dict, b_dict = {}, {}
#   for c in s1:
#     if c not in a_dict:
#       a_dict[c] = 1
#     else:
#       a_dict[c] += 1
#   for c in s2:
#     if c not in b_dict:
#       b_dict[c] = 1
#     else:
#       b_dict[c] += 1
#   count_edit = 1
#   if len(s1) - len(s2) < 0:
#     for item in b_dict.items():
#       if item[0] not in a_dict:
#         count_edit -= item[1]
#       else:
#         if item[1] != a_dict[item[0]]:
#           count_edit -= abs(item[1] - a_dict[item[0]])
#   else:
#     for item in a_dict.items():
#       if item[0] not in b_dict:
#         count_edit -= item[1]
#       else:
#         if item[1] != b_dict[item[0]]:
#           count_edit -= abs(item[1] - b_dict[item[0]])

#   return count_edit == 0


# if __name__ == '__main__':
#   s1 = 'pale'
#   s2 = 'ple'
#   print(check_edits(s1, s2))



# # string compression
# O(Nc) ~ O(N) - space - O(N)
# def compress_string(string):
#   strg = ''
#   counter = 0
#   compression_stack = []
#   for c in string:
#     if len(compression_stack) != 0 and \
#     compression_stack[-1] != c:
#         element = compression_stack[-1]
#         while len(compression_stack) != 0:
#           compression_stack.pop()
#           counter += 1
#         strg += element + str(counter)
#         counter = 0
#     compression_stack.append(c)

#   element = compression_stack[-1]
#   while len(compression_stack) != 0:
#     compression_stack.pop()
#     counter += 1
#   strg += element + str(counter)

#   print('string = {} and compressed string = {}'.format(string, strg))
#   return string if len(string) <= len(strg) else strg


# if __name__ == '__main__':
#   string = 'aabcccccaaa'
#   print(compress_string(string))
#   string = 'aaaaa'
#   print(compress_string(string))
#   string = 'a'
#   print(compress_string(string))

# # Sid's way of doing the rotation -- I prefer this method
# # only problem is that, it's a bit of a time to get the
# # final indices right
# # rotate matrix - 90 deg
# # for more rotations, just use this on the generated matrix
# # O(N**2) for inplace solution, matrix size = N x N
# def rotate_matrix_90deg(matrix, N):
#   'rotates the given N x N matrix by 90 degrees'
#   # step 1 - swap the cols 0 with n-1th and so on
#   for r in range(0, N, 1):
#     i = 0
#     j = N - 1
#     while i < j:
#       matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
#       i += 1
#       j -= 1
#   # step 2 - diagonal swaps
#   # starting from N - 1, 0 upto 0, N-1
#   for r in range(N - 1, -1, -1):
#     for c in range(0, N - 1 - r, 1):
#       matrix[r][c], matrix[N - 1 - c][N - 1 - r] = \
#       matrix[N - 1 - c][N - 1 - r], matrix[r][c]



# if __name__ == '__main__':
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   rotate_matrix_90deg(matrix, 3)
#   matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#   rotate_matrix_90deg(matrix, 4)

 
# # this is elegant since it protects against
# # the formation of an all 0 matrix due to the operations
# # zero matrix
# def zero_matrix(matrix):
#   zero_list = []
#   # phase 1 - scanning for zero
#   for r in range(0, len(matrix), 1):
#     for c in range(0, len(matrix), 1):
#       if matrix[r][c] == 0:
#         zero_list.append((r, c))
#   # phase 2 - making the rows and cols reqd to 0s
#   for coordinate in zero_list:
#     # makes the col to 0 for all rows
#     for r in range(0, len(matrix), 1):
#       matrix[r][coordinate[1]] = 0
#     for c in range(0, len(matrix), 1):
#       matrix[coordinate[0]][c] = 0


# if __name__ == '__main__':
#   matrix = [[1, 2, 3], [4, 5, 0], [6, 0, 1]]
#   zero_matrix(matrix)



# # checking for string rotation
# # assume that the issubstring() is given
# def issubstring(s1, s2):
#   return s2 in s1

# def check_rotation(s1, s2):
#   if len(s1) != len(s2):
#     return False
#   s1 += s1
#   return issubstring(s1, s2)

# if __name__ == '__main__':
#   s1 = 'waterbottle'
#   s2 = 'erbottlewat'
#   print(check_rotation(s1, s2))




# # print all permutations of a string (allowing duplicates)

# def generate_permutations(string, lindex, rindex, contents):
#   if lindex == rindex:
#     contents.append(''.join(string))
#     return
#   for index in range(lindex, rindex + 1, 1):
#     # swap lindex pos with index pos
#     string[lindex], string[index] = string[index], string[lindex]
#     # delegate the permutation generation to new string
#     generate_permutations(string, lindex + 1, rindex, contents)
#     # backtrack to original string
#     string[lindex], string[index] = string[index], string[lindex]


# if __name__ == '__main__':
#   s = list(input().strip())
#   contents = []
#   generate_permutations(s, 0, len(s) - 1, contents)
#   print(contents)



# # generating balancing parentheses


# def generate_paren(string, leftcount, rightcount, final, index):
#   if leftcount < 0 or leftcount > rightcount:
#     return # this is an illegal string, not balanced
#   if leftcount == 0 and rightcount == 0:
#     # balanced, exhausted all strings
#     final.append(''.join(string))
#   else:
#     string[index] = '('
#     generate_paren(string, leftcount - 1, rightcount, final, index + 1)
#     string[index] = ')'
#     generate_paren(string, leftcount, rightcount - 1, final, index + 1)




# if __name__ == '__main__':
#   count = int(input().strip())
#   string = [None] * 2 * count
#   final = []
#   generate_paren(string, count, count, final, 0)

# # generating powerset

# def find_ps(set_, ps):
#   if len(set_) == 0:
#     return
#   else:
#     new_ps = []
#     element = set_.pop()
#     for s in ps:
#       s_copy = list(s)
#       s_copy.append(element)
#       new_ps.append(s_copy)
#     print(new_ps, ps)
#     ps.extend(new_ps)
#     print(ps)
#     find_ps(set_, ps)



# if __name__ == '__main__':
#   set_ = [1, 2, 3]
#   ps = [list()]
#   find_ps(set_, ps)




# # super functional strings
# import sys

# def generate_substrings(string, window_size, set_):
#   '''
#   Generates the substrings
#   '''
#   while window_size <= len(string):
#     lindex = 0
#     while lindex < len(string):
#       s = string[lindex : lindex + window_size]
#       set_[s] = (len(s), find_distinct_count(s))
#       lindex += 1
#     window_size += 1
  

# def find_distinct_count(string):
#   a_dict = set()
#   for c in string:
#     a_dict.add(c)
#   return len(a_dict)

    
    
# def compute_function(p):
#   substrings = {}
#   generate_substrings(p, 1, substrings)
#   #print(substrings)
#   sum = 0
#   for v in substrings.values():
#     value = (v[0] ** v[1]) % ((10 ** 9) + 7)
#     sum += value
#   return sum

  
  
# if __name__ == '__main__':
#   t = int(input().strip())
#   sys.setrecursionlimit(80000)
#   for _ in range(0, t, 1):
#     p = input().strip()
#     print(compute_function(p))
  

# # hackerrank problem, antenna

# def set_all(array, lindex, rindex):
#   while lindex < rindex and lindex < len(array):
#     array[lindex] = True
#     lindex += 1



# def set_antenna(inarray, k):
#   len_array = max(inarray)
#   array = [ True for _ in range(len_array + 1) ]
#   for x in inarray:
#     array[x] = False
#   count = 0
#   index = 0
#   while index < len(array):
#     if not array[index]:
#       count += 1
#       set_all(array, index, index + 2 * k + 1)
#       print(index, index + 2 * k + 1)
#       index += 2 * k + 1
#     else:
#       index += 1
#   count_false = 0
#   for i in array:
#     if not i:
#       count_false += 1
#   print('count false = {}'.format(count_false))
#   return count





# if __name__ == '__main__':
#   n, k = list(map(int, input().strip(' ').split(' ')))
#   arr = list(map(int, input().strip(' ').split(' ')))
#   count = set_antenna(arr, k)
#   print(count)


