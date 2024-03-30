'''
    Josue Antonio
    DS2000
    Spring 2023
    Homework 5
    02/21
    Starter code for HW5 - a main and a couple of baisc functions.
    
    Your job is to write the rest of the functions main relies on! 
    mbta.py
'''

import csv
import matplotlib.pyplot as plt

MBTA_FILE = "mbta_data.csv"
LINE_COL = 3
TOTAL_ON = 12
TOTAL_OFF = 13
TIME_OF_DAY = 8

def read_file(filename):
    ''' Function: read_file
        Parameters: filename (string) for a CSV file
        Returns: 2d list of what the file contains
        Does: Reads every line of the file, except the header,
              and stored in a 2d list which is returned at the end
    '''
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        next(reader)
        for row in reader:
            data.append(row)
    return data

def get_col(data, col):
    ''' Function: get_col
        Parameters 2d list of anything, a column number (int)
        Returns: one column of the 2d list, turned into a list of its own
        Does: Loops over the 2d list, and for each sublist, appends
              a value at the given location onto a new list
    '''
    lst = []
    for row in data:
        lst.append(row[col])
    return lst

def riders_per_line(lst, line, color_col, riders_col):
    ''' Function: riders_per_line
        Parameters: 2d list of strings (matches structure of CSV file),
                    string for MBTA line we care about, col int where line
                    color lives, col int where number of riders lives
        Returns: average number (float) of riders in given line
        Does: looks for the given MBTA line in the 2D list. If found, increase
              the total number of riders. Computes the average number of 
              riders and returns it.
    '''
    number_riders = 0
    riders_counter = 0
    for row in lst:
        if line in row[color_col]:
            number_riders += int(row[riders_col])
            riders_counter += 1
            
    avg_riders = number_riders / riders_counter
    return avg_riders

def split_by_time(lst, time_period, time_col):
    ''' Function: split_by_time 
        Parameters: 2d list of strings (matches the structure of CSV file),
	                a string for the time period we care about, and an int for 
                    the column number where the time_period column lives
        Returns: a 2d list of strings
        Does: filters the original 2d list based on the given time period, 
              returning a smaller 2d list with just the items that match the 
              given time period
    '''
    filtered_lst = []
    for row in lst:
        if  time_period in row[time_col]:
            filtered_lst.append(row)
    return filtered_lst

def plot_ridership(lst_riders, lst_lines):
    ''' Function: plot_ridership
        Parameters: a list of ints (# of riders per line), and a list of 
                    strings (labels for the MBTA line names
        Returns: nothing
        Does: generates a bar plot, with both colors and labels taken from the 
              list of strings, and heights taken from the list of ints
    '''
    for i in range(len(lst_riders)):
        plt.bar(lst_lines[i], lst_riders[i], color = lst_lines[i] )
    plt.title("MBTA Average Ridership")
    plt.ylabel("Average Riders per Line")
    plt.xlabel("Lines")

def plot_time_ridership(lst, line_names):
    ''' Function: plot_time_ridership
        Parameters: 2d list of floats, and a 1d list of strings (line names)
        Returns: nothing
        Does: generates a line chart, calling the get_col function to retrieve 
              the data from each of the 4 lines. Labels and colors in the plot  
              are taken from the list of strings. 
    '''
    for i in range(len(line_names)):
        plt.plot(get_col(lst, i), color = line_names[i], 
                 label = line_names[i])
    plt.title("Ridership on all lines over the day")    
    plt.xlabel("Time Period")
    plt.ylabel("Riders per Line")
    plt.legend()
        
def main(): 
    # Step One: Gathering data
    # Get the data as a 2d list of ints
    data = read_file(MBTA_FILE)

    # Step Two: Computations 
    # Compute the average number of riders getting on each line
    lines = ["Green", "Blue", "Red", "Orange"]
    ridership = []
    for i in range(len(lines)):
        on_riders = riders_per_line(data, lines[i], LINE_COL, TOTAL_ON)
        ridership.append(on_riders)
    
    # Step Two: Computations
    # Count the average number of total riders at each time of day
    # We can reuse the ridership functions above, but first we
    # split the data into each separate part of day
    ridership_time = []
    for i in range(1, 12):
        time_period = "time_period_{:02d}".format(i)
        time_data = split_by_time(data, time_period, TIME_OF_DAY)
        curr_riders = []
        for j in range(len(lines)):
            riders = riders_per_line(time_data, lines[j], LINE_COL, TOTAL_ON)
            curr_riders.append(riders)
        ridership_time.append(curr_riders)
              
    # Step Three: Communicate! 
    # Plot the average number of riders getting on each line
    plot_ridership(ridership, lines)
    plt.show()
    
    # Plot each line's ridership over the day as a line chart
    plot_time_ridership(ridership_time, lines)
    
    # Communicate part 2... print out average ridership per line
    print("Average ridership per line:")
    for i in range(len(lines)):
        print("\t", lines[i], ": ", round(ridership[i]), " avg riders.",
              sep = "")

    
main()  