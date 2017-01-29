# hashing.py

__author__ = 'sidmishraw'
__email__ = 'sidharth.mishra@sjsu.edu'
__python_version__ = '3.5.2'



'''
Introduction to building your own hashtable using Python3.
and questions for Uber.. internship challenges
'''

def login_problem():
  '''
  Given input which is vector of log entries of some online system each entry is
  something like (user_name, login_time, logout_time), come up with an algorithm with outputs number of
  users logged in the system at each time slot in the input, output should contain only the time slot which
  are in the input.
  For the example given below output should contain timeslots
  [(1.2, 1), (3.1, 2), (4.5, 1), (6.7, 0), (8.9, 1), (10.3,0)]

  /*
  [
  ("Jane", 1.2, 4.5),
  ("Jin", 3.1, 6.7),
  ("June", 8.9, 10.3)
  ]

  =>

  [(1.2, 1), (3.1, 2), (4.5, 1), (6.7, 0), (8.9, 1), (10.3, 0)]

  */
  '''
  vectors = [("Jane", 1.2, 4.5), ("Jin", 3.1, 6.7), ("June", 8.9, 10.3)]
  time_dict = {}
  checkpoint_time = 0
  for vector in vectors:
    if vector[1] in time_dict:
      time_dict[vector[1]] += 1
    elif vector[1] >= checkpoint_time:
      time_dict[vector[1]] = 1
    elif vector[1] < checkpoint_time:
      time_dict[vector[1]] = 2
      time_dict[checkpoint_time] += 1
    checkpoint_time = vector[2]
    if checkpoint_time in time_dict:
      time_dict[checkpoint_time] += 1
    else:
      time_dict[checkpoint_time] = 0

  print(time_dict)



def main():
  # login_problem()
  pass


if __name__ == '__main__':
  # in python strings are immutable, so no character mdifications
  # use the string replace methods etc

  image = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'] ]
  for i in range(0, 3, 1):
    for j in range(0, 3, 1):
      image[i][j]
  # for i in range(0, len(image), 1):
  #   for j in range(len(image) - 1, -1, -1):
  #     image[j][i], image[i][len(image) - 1 - j] = image[i][len(image) - 1 - j], image[j][i]




