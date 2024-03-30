'''
    Josue Antonio
    DS 2000
    Homework 1 Problem 2
    1/17 - Spring 2023
    roadtrip.py 
    
    Test case #1: 
        Distance = 320
        Speed = 40
        Sleep time = 10 hours
        Expected: 0 days and 8 hours
        
    Test case #2:   
        Distance = 21000
        Speed = 90
        Sleep time = 7 hours
        Expected = 12 days and 8 hours
'''

def main():
    # Gather data - prompt the user for total number of trip miles, avg speed,
    # and daily total resting time
    
    total_miles = int(input("How far are Kermit  and Fozzie going, in miles? \
                                                                    \n"))
    avg_speed = int(input("What will be their average speed, in MPH?\n"))
    resting_hours = int(input("How long will they sleep each day, in hours?\n"
                                                                      ))
    
    # Computation - total hours, including sleep adjustment, and conversion of
    # total hours to days and hours
    
    travel_hours = total_miles / avg_speed
    travel_days = travel_hours // 24
    remaining_hours = ((travel_hours / 24) % 1) * 24
    total_hours = (resting_hours * travel_days) + remaining_hours
    total_days = travel_days + (total_hours // 24)
    final_hours = total_hours % 24

    # Communication - report the total roadtrip duration in days and hours
        
    print("The Muppet Road Trip will take", round(total_days), "days", "and", 
                                              round(final_hours), "hours.\n")
    
main()