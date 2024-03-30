'''
    Josue Antonio
    DS 2000
    Homework 1 Problem 3
    1/18 - Spring 2023
    sailing.py 
    
    Test case #1:
        traffic = 8
        wind = 7
        swells = 1
        Expected: (0.2*2) + (0.5*8) + (0.3*0) = 4.4
        
    Test case #1:
        traffic = 1
        wind = 5
        swells = 0
        Expected: (0.2*9) + (0.5*10) + (0.3*10) = 9.8
    
'''

TRAFFIC = 0.2
WIND_SPEED = 0.5
HIGH_SWELL = 0.3

def main():
    # Gather Data - prompt the user for traffic level, wind speed, and 
    # swell level
    
    traffic = int(input("How much traffic was there, on a scale of 0-10?\n"))
    wind_speed = int(input("What was the wind speed, in knots 5-15?\n"))
    swell_level = int(input("Were the swells high (0 = no, 1 = yes)?\n"))
    
    
    # Computation - convert sailing quality parameters to the range 0-10, and
    # compute weighted average to quantify how good of a sailing day it's
    
    converted_traffic = 10 - traffic
    converted_wind_speed = 15 - wind_speed
    converted_swell_level = (swell_level + 10) % 11
    
    weighted_average = (TRAFFIC * converted_traffic) + \
        (WIND_SPEED * converted_wind_speed) + \
            (HIGH_SWELL * converted_swell_level)
                        

    # Communication - report the weighted average quantifying the quality of 
    # the sailing day
    
    print("On a scale out of 10, we computed your day of sailing to have a " \
    "weighted average of", round(weighted_average,1), "\n")
      
main()
