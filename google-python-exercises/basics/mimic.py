#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import re


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++

  mimic = {} # dict initialization -- empty dict mimic

  try:

    f = open(filename,"rU") # open file in universal mode -- so that all line endings are converted to \n

    text = f.read() # reads all the lines at once into a single large string

    f.close()  # closing since the file is no longer needed, all text in-memory

    words = [words.split(" ") for words in re.split(r"\n",text)]
    print(words)

    prevword = None
    nextword = None

    for word in words:

      for wordIndex in range(0,len(word)):

        currentWord = word[wordIndex]

        if wordIndex == 0:
          prevword = ""
          if prevword in mimic:
            if mimic[prevword] or mimic[prevword] == []:
              mimic[prevword].append(currentWord)
          else:
            mimic[prevword] = [currentWord]
        else:
          prevword = word[wordIndex-1]

        if not currentWord == word[-1:][0]:
          nextword = word[wordIndex+1]

        if currentWord in mimic:
          if mimic[currentWord] or mimic[currentWord] == []:
            mimic[currentWord].append(nextword)
        else:
          mimic[currentWord] = [nextword]
  except IOError:
    print("IO Error occurred while reading from file: %s" % filename)

  return mimic


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  for i in range(0,200):
    print( random.choice(mimic_dict[word]), end=" ")
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  dict = mimic_dict(r"/Users/sidmishraw/Downloads/google-python-exercises/basic/small.txt")
  print(dict)
  print(print_mimic(dict, ''))


if __name__ == '__main__':
  main()
