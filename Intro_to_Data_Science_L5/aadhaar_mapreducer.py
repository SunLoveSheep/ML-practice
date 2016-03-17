import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.

    for line in sys.stdin:
        #tokenize the line of data
        data = line.strip().split(",")
        
        #ignore incorrect data and skip the header line:
        if (len(data) != 12) or (data[0]=='Registrar'):
            continue
        
        print "{0}\t{1}".format(data[3],data[8])
        
mapper()

def reducer():
    
    aadhaar_generated = 0
    old_key = None
    
    for line in sys.stdin:
        #read in line by line the sorted keys
        data = line.strip().split("\t")
        
        #if length not right, skip the data
        if len(data) != 2:
            continue
        
        #assign key value and count into "this_key" and "count" from the current line
        this_key, count = data
        
        #if we encounter a new key value, which means the previous key value is counted, output previous key value and counter value
        #as a new pair of key
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, aadhaar_generated)
            aadhaar_generated = 0
        
        #if no new key encountered, update previous key to current key and the counter
        old_key = this_key
        aadhaar_generated += float(count)
    
    #print final key:
    if old_key != None:
        print "{0}\t{1}".format(old_key, aadhaar_generated)


reducer()
