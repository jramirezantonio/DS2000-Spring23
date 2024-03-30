'''
    DS2000
    Spring 2023
    Sample code from class -- classifier to use in a nearest-neighbor
    prediction model
    
    Our goal -- determine whether a show will win an emmy
    
    Two categories only: emmy / no emmy
'''

from emmyshow import EmmyShow
import csv

K = 7
SHOW_FILE = "shows.csv"

def read_csv(filename):
    ''' Function: read_csv
        Parameters: filename, a string
        Returns: 2d list of strings
        Does: loops over each line in the file, which is saved as a 
              list of strings, skips the header
    '''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for row in csvfile:
            data.append(row)
    return data

def make_show_objs(lst):
    ''' Function: make_show_objs
        Parameters: 2d lst of strings
        Returns: lst of emmyShow objects
        Does: iterates over the list, turns each row into an object
    '''
    objs = []
    for row in lst[1:]:
        for i in range(len(row)):
            if row[i].isdigit():
                row[i] = float(row[i])
        tv = EmmyShow(row)
        objs.append(tv)
    return objs
    

def find_min(distances):
    ''' Function: find_min
        Parameters: list of floats
        Return: tuple of float, int
        Does: finds smallest distance in the list, returns
               its value and position
    '''
    min_val = float("inf")
    min_pos = -1
    for i in range(len(distances)):
        if distances[i] < min_val:
            min_val = distances[i]
            min_pos = i
    return min_val, min_pos

def classify(distances, train, k):
    ''' Function: classify
        Parameters: list of floats, list of TVShow objects, int k
        Returns: 2-element list of ints
        Does: find the min distance k times, then increase the count for
              the category that show is in
    '''
    counts = [0, 0]
    for i in range(K):
        min_dist, min_pos = find_min(distances)
        cat = train[min_pos].get_category()
        counts[cat] += 1
        distances.pop(min_pos)
        train.pop(min_pos)
    return counts
    
def main():
    # gather data - read in the tv show info from the file (training set)
    raw_shows = read_csv(SHOW_FILE)
    
    # gather data - hard-code a show to see if it'll win (testing set)
    test_show = EmmyShow(["The Last of Us", 0, 4, 5, 2])
    
    # computation - turn the 2d list of strings into show objects
    tv_objs = make_show_objs(raw_shows)
    
    # computtaion - make a list of distances between test and training
    distances = []
    for train in tv_objs:
        distance = train.euclidean(test_show)
        distances.append(distance)
        
    # computation - find the K nearest neighbors and see 
    # if the majority have an emmy, or not
    results = classify(distances, tv_objs, K)
    print("Is your show going to win an emmy?...\n\n")
    print("[no emmy, emmy]...", results)
    
main()