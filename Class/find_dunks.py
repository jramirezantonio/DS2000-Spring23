'''
    DS2000
    Spring 2023
    Sample code from class - nearest neighbor algo. 
    
    Tweaking code from Friday...
    - use the csv library to read a csv file (so we can search "Boston,MA")
    - use a function to turn a column into a list
    
    Tweaking code from Tuesday...
    - add a euclidean distance function
    - add a minimum distance function
    - find 
'''

import csv
import matplotlib.pyplot as plt

DUNKS_FILE = "DD_US.csv"
CITY_COL = 2
LONG_COL = 0
LAT_COL = 1
ADDRESS_COL = 3
LANEY_LAT = 42.30537
LANEY_LONG = -71.061

def read_csv(filename):
    ''' Function: read_csv
        Parameters: filename
        Returns: 2d list of strings
        Does: reads each line of the file to create a 2d list.
    '''
    lst = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for line in csvfile:
            lst.append(line)
    return lst
    
def col_to_lst(lst, col, data_type = str):
    ''' Function: col_to_lst
        Parameters: 2d list, int
        Returns: 1d list
        Does: Create a list made up of every row at the given column
    '''
    new_lst = []
    for row in lst:
        new_lst.append(data_type(row[col]))
    return new_lst

def get_local(lst, city, col):
    ''' Function: get_local
        Parameters: 2d list of strings, string for city, int
        Returns: 2d list of strings
        Does: Look for given city at the position given by int
              in every row, returns a filtered 2d list
    '''
    smaller = []
    for row in lst:
        if city in row[col]:
            smaller.append(row)
    return smaller

def similarity(x1, y1, x2, y2):
     euclidean_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
     return euclidean_dist

def euclidean(lats, longs, goal_lat, goal_long):
    ''' Function: euclidean
        Parameters: 1d list of lats, 1d list of longs, single floats for goal 
                    lat / goal long
        Return: 1d list of floats, all the distances
        Does: compute euclidean distance between goal and each given point
    '''
    distances = []
    for i in range(len(lats)):
        lat = lats[i]
        long = longs[i]
        distance = (lat - goal_lat) ** 2 + (long - goal_long) ** 2
        distance = distance ** (1 / 2)
        distances.append(distance)
    return distances

def find_min(distances):
    ''' Function: find_min
        Parameters: list of floats
        Return: smallest distance, and its position
        Does: finds smallest distance in the list, returns its value and pos
    '''
    min_val = float("inf")
    min_pos = -1
    for i in range(len(distances)):
        if distances[i] < min_val:
            min_val = distances[i]
            min_pos = i
    return min_val, min_pos

def main():
    # Gather data - read from the file
    data = read_csv(DUNKS_FILE)
    
    # # Computation - isolate lat/long into separate lists
    lats = col_to_lst(data, LAT_COL, data_type = float)
    longs = col_to_lst(data, LONG_COL, data_type = float)
        
    # Get  a list of all distances
    distances = euclidean(lats, longs, LANEY_LAT, LANEY_LONG)
    
    # Find the closest location
    min_val, min_pos = find_min(distances)
    
    # Communication - report the closest one!
    print("The closest dunks is", min_val, "away and is here:", 
          data[min_pos][ADDRESS_COL])
    
    # # communicate - plot all the DD loatoins
    # plt.scatter(longs, lats, color = "orange")
    # plt.plot(LANEY_LONG, LANEY_LAT, "*", color = "fuchsia", markersize = 13)
    
    # # Gather data - what city to look at?
    # city = input("What city?\n")
    
    # # Computations - find all the DD in that city
    # city_results = get_local(data, city, CITY_COL)
    
    # # Communication - print out all the locations
    # print(city_results)
    # print("How many Dunks in that city?", len(city_results))
    # print("How many Dunks in US?", len(data))
    
main()