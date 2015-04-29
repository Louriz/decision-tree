from __future__ import division
import math
import operator
import time
import random
import copy
from collections import Counter


##################################################
# data class to import and hold csv data
##################################################
class data:
    def __init__(self, datafile, test=False):
        self.datafile = datafile
        self.read_data()

    def read_data(self):
        f = open('tennis.csv') #make general later
        original_file = f.read()
        rowsplit_data = original_file.split("\r")
        self.examples = [rows.split(',') for rows in rowsplit_data]

        #list attributes
        self.attributes = self.examples.pop(0)
        
        #create array that indicates whether each attribute is a numerical value or not
        attr_type = open('tennistypes.csv') #make general later
        orig_file = attr_type.read()
        self.attr_types = orig_file.split(',')

        #convert attributes that are numeric to floats
        for example in self.examples:
            for x in range(len(self.examples[0])):
                if self.attributes[x] == 'True':
                    example[x] = float(example[x])
                               

        

        print str(self.examples)
        #print str(orig_file)
        #print str(self.attr_types)

##################################################
# count number of examples with classification "1"
##################################################
def one_count(instances, attributes, classifier):
    count = 0

    #find index of classifier
    print attributes
    for a in range(len(attributes)):
        if attributes[a] == classifier:
            class_index = a
    
    for i in instances:
        if i[class_index] == "1":
            count += 1

    return count

#####################################################
# Calculate entropy relative to c-wise classification
#####################################################
def entropy_S(instances, attributes, classifier):
    count = one_count(instances, attributes, classifier)
    total = len(instances)
    count0 = total - count
    s = (-(count/total) * math.log2(count/total)) + (-(count0/total) * math.log2(count0/total))
    return s

#####################################################
# Calculate iformation gain of each attribute
#####################################################
def gain(instances, attributes, classifier):
    gain_vals = []
    for a in attributes ##not finished, split recursively over



##################################################
# main function, organize data and execute functions based on input
# need to account for missing data
##################################################
def main():
    train_file = "tennis.csv"
    train_data = data(train_file)

    classifier = "Play"

    print one_count(train_data.examples, train_data.attributes, classifier)
    

if __name__ == "__main__":
	main()