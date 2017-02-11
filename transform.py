# transform.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-02-07 19:07:30
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-02-11 14:20:34




'''
Transforms the given table into a hyper-graph. Trying to mine new patterns.
The reason I'm using a WeakSet instead of set is to hold weakrefs for the CharNode objs 
with the only strong reference held by the ITEM_CACHE.
'''

from os import getcwd
from pprint import pprint
from weakref import proxy
from weakref import WeakSet


TID_SEPARATOR = '   '
SEPARATOR = ','
NEW_LINE = '\n'
INPUT_FILE_PATH = r'{}/{}'.format(getcwd(), 'input.txt')
MIN_THRESHOLD = 3
ITEM_CACHE = {}

class Row(object):
  '''
  Row of the table
  '''

  def __init__(self, tid, list_of_items):
    self.tid = tid
    self.list_of_items = list_of_items

  def __repr__(self):
    return 'tid = {}, items = {{{items}}}'.format(self.tid, items = ','.join(self.list_of_items))


class CharNode(object):
  '''
  The CharNode is an encapsulation for the DataNode for the Hypergraph.
  '''

  def __init__(self, value):
    self.value = value
    self.neighbors = WeakSet()
    self.parents = WeakSet()
    self.out_degree = 0

  def __repr__(self):
    return 'value = {}, neighbors={{{}}}, parents={{{}}}, out_degree={}'.format(self.value, \
      ','.join(set(map(lambda x: x.value, self.neighbors))), \
      ','.join(set(map(lambda x: x.value, self.parents))), self.out_degree)




def parse_block(string_block):
  '''
  Parse block of something like
  100   {f, a, c, d, g, i, m, p}
  200   {a, b, c, f, l, m, o}
  300   {b, f, h, j, o}
  400   {b, c, k, s, p}
  500   {a, f, c, e, l, p, m, n}
  into Row objects
  '''

  strings = string_block.split(NEW_LINE)
  rows = []
  for string in strings:
    tid, list_of_items = string.split(TID_SEPARATOR)
    rows.append(Row(tid, list(list_of_items.strip('{').strip('}').split(', '))))
  return rows


def process_block(rows):
  '''
  Take in the rows, a list of Row objects and build up the ITEM_CACHE
  :input-param: rows : list of Row objects
  '''
  global ITEM_CACHE

  for row in rows:
    prev = None
    traversal_set = WeakSet()
    parents_cache_row = {}
    for e in row.list_of_items:
      if e not in ITEM_CACHE:
        ITEM_CACHE[e] = CharNode(e)
      if prev:
        prev.neighbors.add(ITEM_CACHE[e])
        prev.out_degree += 1
        traversal_set.add(prev)
      ITEM_CACHE[e].parents = ITEM_CACHE[e].parents.union(WeakSet(traversal_set))
      prev = ITEM_CACHE[e]
  return


def process_item_cache():
  '''
  Process the item cache, dropping the elements that have an outdegree lower than the
  required MIN_THRESHOLD.
  Since the parents and neighbors of each CharNode are WeakSets maintaining weakrefs,
  there is not additional need for removing them once removed from the ITEM_CACHE.
  '''

  global ITEM_CACHE, MIN_THRESHOLD

  dupl = dict(ITEM_CACHE)
  for k in dupl:
    if dupl[k].out_degree < MIN_THRESHOLD:
      del ITEM_CACHE[k]
  del dupl
  pprint(ITEM_CACHE)
  return



if __name__ == '__main__':
  input_string_block = None
  with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as f:
    input_string_block = f.read().strip('\n').strip('   ')
    print(input_string_block)
  parsed_block = parse_block(input_string_block)
  process_block(parsed_block)



