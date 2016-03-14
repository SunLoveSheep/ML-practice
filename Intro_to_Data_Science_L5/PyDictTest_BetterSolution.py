'''
In this .py, a better solution is given for PyDictTest
'''

import logging
import sys
import string

from util import logfile

logging.basicConfig(filename=logfile, format='%(message)s',
                   level=logging.INFO, filemode='w')


def word_count():
    word_counts = {}
    
    #iterate in terms of lines:
    for line in sys.stdin:
        data = line.strip().split(" ") #read one line of words in to a list, separated by " " (space)
        for i in data:
          key = i.translate(string.maketrans("",""),string.punctuation).lower() 
          #string.translate(s, table[, deletechars])
          #Delete all characters from s that are in deletechars (if present), and then translate the characters using table, 
          #which must be a 256-character string giving the translation for each character value, indexed by its ordinal. 
          #If table is None, then only the character deletion step is performed.
          if key in word_counts.key():
            word_counts[key] += 1
          else:
            word_counts[key] = 1

    print word_counts

word_count()
