'''
  Algorithm:
      * create a bunch of TVShow objects
      * then, ask the user about a show they've recently watched
      * recommend from a list of TVShow objects, shows with similar length, 
        popoularity, and a good rating
'''

import csv
from tvshow import TVShow

SHOW_FILE = "sec1_recommendations.csv"

def read_file(filename):
    ''' Fn: read_file
        Param: filename, a string
        Returns: contents of the file as a 2d list
        Does: iterates over each row, generating a 2d list of strings
    '''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for row in csvfile:
            data.append(row)
    return data
    
def make_objects(lst):
    ''' Fn: make_objects
        Param: 2d list of stringss
        Returns: 1d list of TVShow objects
        Does: iterates over the given list, each row turns into an object
    '''
    show_objs = []
    for row in lst:
        title = row[0]
        rating = float(row[1])
        pop = int(row[2])
        length = int(row[3])
        show = TVShow(title, length = length, pop = pop,
                      rating = rating)
        show_objs.append(show)
    return show_objs
    

def main():
    # Gather data - read in from the file
    show_lst = read_file(SHOW_FILE)

    # Gather data - ask the user for info about a show they've watched
    title = input("What show?\n")
    length = int(input("Enter length of an episode\n"))
    pop = int(input("How popular is your show?\n"))
    rating = int(input("What is your rating?\n"))
    
    # Computation - generate a list of TVShow objects
    show_objs = make_objects(show_lst)
    
    # Computation - create TVShow obj from user input
    show = TVShow(title, length = length, pop = pop, rating = rating)
    
    # Computation - make a list of recommended shows
    recs = []
    for curr_show in show_objs:
        if curr_show.recommend(show):
            recs.append(curr_show)`
    
    # Print recommendations
    print("DS2000 thinks you should watch...")
    for rec in recs:
        print(rec)
        
    # To start with, recommend show witht the closest distance to
    # user's show
    
    min_show = None # obj that your don't have yet
    min_dist = float("inf")
    for rec in recs:
        distance = rec.euclidean(show)
        if distance < min_dist:
            min_dist = distance
            min_show = show
    
    # Finally, report the show to start with
    print("\n\n... But start with:", min_show)
main()