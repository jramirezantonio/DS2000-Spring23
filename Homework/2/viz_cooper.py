'''
    Josue Antonio
    DS 2000
    Homework 2 - Problem 3
    1/23 - Spring 2023
    viz_cooper.py
    
    Test Case: Distance = 2.21 units
                Feet = 2.21(800) = 1768
                Miles = 1768/5280 = 0.33
                I want to cover 0.33 miles in 10 minutes
                = 1.98 miles per hour
    
'''

import matplotlib.pyplot as plt
DISTANCES = "distances_to_cooper.txt"
DISTANCE_UNIT = 800
FT_IN_MILE = 5280

def main():
    # Gather data - read in the distances between the 3 people to Cooper
    # from the text file
    with open (DISTANCES, "r") as infile:
        distance1 = float(infile.readline())
        distance2 = float(infile.readline())
        distance3 = float(infile.readline())
    
    # Computation - convert distances in units to feet, and compute the paces
    # (in MPH) each person should have to reach Cooper in 10 minutes
    distance1 = distance1 * DISTANCE_UNIT
    distance2 = distance2 * DISTANCE_UNIT
    distance3 = distance3 * DISTANCE_UNIT
    
    pace1 = (distance1 / FT_IN_MILE) / (1 / 6)
    pace2 = (distance2 / FT_IN_MILE) / (1 / 6)
    pace3 = (distance3 / FT_IN_MILE) / (1 / 6)
    
    # Communication - plot distance (ft) vs. MPH
    plt.plot(distance1, pace1, "o", color = "red", markersize = 12)
    plt.plot(distance2, pace2, "o", color = "blue", markersize = 12)
    plt.plot(distance3, pace3, "o", color = "green" , markersize = 12)

    # Change the x limit and y limit
    plt.xlim(1000, 2500)
    plt.ylim(1, 3)
 
    # Label the x and y axes and add a title
    plt.xlabel("Distance (ft)")
    plt.ylabel("Pace (MPH)")
    plt.title("Distances vs. Paces")
    
    
    
main()


