'''
    Josue Antonio
    Spring 2023
    Sample code from class - find the Dunks in your city!
    
    Two addends from Friday
        - read in using CSV file so that we can have Boston, MA together
'''

import csv
FILENAME= "DD_US.csv"
CITY_COL = 2

def read_csv(filename):
    ''' Function: read_csv
        Param: string
        Returns: 2D list of strings
        Does: turn each row of csv file into element of 2D list
    '''
    lst = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for line in csvfile:
            lst.append(line)
    return lst
            
def get_local(lst, city, city_col):
    ''' Function: get_local
        Param: 2d list of strings, string, and int
        Returns: 2d list of strings
        Does: find all rows in the given list where the city_col contains the
              city, and retunrs a shorter version of original lst
    '''
    city_lst = []
    for row in lst:
        if city in row[city_col]:
            city_lst.append(row)
    return city_lst
    
def main():
    # Gather data - read from CSV file into a 2d list
    data = read_csv(FILENAME)
    
    # Computation - which DD are in boston?
    city = input("Which city?\n")
    city = get_local(data, city, CITY_COL)
    num_dunks = len(data)
    num_city = len(city)
    
    # Communication - orint results
    print("City locations...", city)
    print("How many locations in your city?", num_city)
    print("How many locations in US?", num_dunks)
main()
