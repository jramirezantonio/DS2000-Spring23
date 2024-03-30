'''
    Josue Antonio
    DS 2000
    Homework 4 Problem 3
    2/16 - Spring 2023
    nola_v2.py
    
    Test case:
        Ideal = 65, 55, 56
        Ideal list becomes: [65, 55, 60, 56]
        
        Distance from here to 1950 -
        72, 65, 68.5, 50
        (65 - 72) ** 2 + (55 - 65) ** 2 + (60 - 68.5) ** 2 + (56 - 50) ** 2 =
        49 + 100 + 72.3 + 36 
        And then sqrt(257.3) = 16.04
    
'''

NOLA_WEATHER_FEB = "nola_weather_feb.csv"
YEARS_COL_POSITION = 0
HIGHS_COL_POSITION = 1
LOWS_COL_POSITION = 2
MEANS_COL_POSITION = 3
HUMIDITY_COL_POSITION = 4

def main():
    # Gather data - read in input from user and populate ideals list
    ideals = []
    ideal_high_temp = int(input("What is your ideal high temperature?\n"))
    ideal_low_temp = int(input("What is your ideal low temperature?\n"))
    ideal_humidity = int(input("What is your ideal humidity?\n"))
    ideals.append(ideal_high_temp)
    ideals.append(ideal_low_temp)
    # compute mean of temps and append it to ideals list
    mean = (ideal_high_temp + ideal_low_temp) / 2
    ideals.append(mean)
    ideals.append(ideal_humidity)
    
    # Computation - read in csv weather data
    years = []
    closest_distance = 100000
    closest_year_pos = 0
    pos = 0
    with open(NOLA_WEATHER_FEB, "r") as infile:
        infile.readline().strip().split(",")
        for line in infile:
            current_weather = []
            line = line.strip().split(",")
            years.append(int(line[YEARS_COL_POSITION]))
            current_weather.append(int(line[HIGHS_COL_POSITION]))
            current_weather.append(int(line[LOWS_COL_POSITION]))
            current_weather.append(float(line[MEANS_COL_POSITION]))
            current_weather.append(int(line[HUMIDITY_COL_POSITION]))
            
            # compute euclidean distance between ideal and current weather
            euclidean_distance = ((ideals[0] - current_weather[0]) ** 2 +
                    (ideals[1] - current_weather[1]) ** 2 +
                    (ideals[2] - current_weather[2]) ** 2  +
                    (ideals[3] - current_weather[3]) ** 2) ** (1 / 2)
            
            # find minimum such distance and the corresponding year pos
            if euclidean_distance < closest_distance:
                closest_distance = euclidean_distance
                closest_year_pos = pos
            pos += 1
    # Round closest distance, find year corresponding to closest year
    closest_distance = round(closest_distance, 2)
    closest_year = years[closest_year_pos]
    
    # Communication - report closest year and closest distance to user
    print("The year closest to your ideal weather is", closest_year, 
          "with distance", closest_distance)
    
main()