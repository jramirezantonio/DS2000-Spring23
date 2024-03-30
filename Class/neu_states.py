'''
    DS2000
    Spring 2023
    Sample code from class - March 3rd
    Questions: Given a state, how many students from there?
               Which state has the most students?
'''

import csv

FILENAME = "neu_geography.csv"
def read_csv(filename):
    ''' Fn: read_csv
        Param.: filename, a string
        Returns: a dictionary of string, int pairs
        Does: reads each line of CSV file, first item is key, second is value
    '''
    data = {}
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for row in csvfile:
            data[row[0]] = int(row[1]) 
    return data

def find_max(dct):
    ''' FN: find_max
        Param.: dictionary where key is anything, but value must be a number
        Return: key, value pair where value is highest
        Does: iterate over given dct., find highest value and return both the 
                the value and its key
    '''
    max_val = -1
    max_key = ""
    for key, value in dct.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key, max_val

def main():
    # Gather data - turn CSV file into dictionary
    dct = read_csv(FILENAME)
    
    # 1. Given a state how many students from there?
    state = input("Enter a state\n")
    if state in dct:
        num_students = dct[state]
    else:
        num_students = 0
    
    # 2. Which state has the most students?
    max_state, max_num = find_max(dct)
    
    # Communication - report results
    print("There are", num_students, "students from", state)
    print(max_state, "has the most students, with...", max_num)


main()