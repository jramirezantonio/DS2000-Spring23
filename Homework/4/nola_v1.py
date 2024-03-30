'''
    Josue Antonio
    DS 2000
    Homework 4 Problem 2
    2/16 - Spring 2023
    nola_v1.py
'''

import matplotlib.pyplot as plt
NOLA_WEATHER_FEB = "nola_weather_feb.csv"
YEARS_COL_POSITION = 0
HIGHS_COL_POSITION = 1
LOWS_COL_POSITION = 2

def main():
    # Initialize data lists to be populated
    years, highs, lows = [], [], []
    
    # Gather data - read in csv data by first ignoring header line and
    # then populate lists data lists
    with open(NOLA_WEATHER_FEB, "r") as infile:
        infile.readline().strip().split(",")
        for line in infile:
            line = line.strip().split(",")
            years.append(int(line[YEARS_COL_POSITION]))
            highs.append(int(line[HIGHS_COL_POSITION]))
            lows.append(int(line[LOWS_COL_POSITION]))
            
    # Computation - compute highest high temp and its respective position
    max_high_temp_pos = 0
    max_high_temp = 0
    for i in range(len(highs)):
        if highs[i] > max_high_temp:
            max_high_temp = highs[i]
            max_high_temp_pos = i
    
    # Communication - plot years against temperature 
    plt.figure(figsize=(15, 6))
    plt.scatter(years, highs, color = "red", label = "High Temps")
    plt.scatter(years, lows, color = "blue", label = "Low Temps")
    # Plot highest high temp
    plt.scatter(years[max_high_temp_pos], max_high_temp, 
             s = 20, color = "green", label = "Highest High Temp")        
    plt.title("Years vs. Temperature (Mardi Gras Day)")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.legend()
    
    # Create list of every 5 years to create x-ticks
    years2 = []
    for i in range(0, 100, 5):
        years2.append(years[i])
    years2.append(years[99])
    plt.xticks(years2)
    
main()
