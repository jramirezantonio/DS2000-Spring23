'''
    Josue & Nick
'''
import matplotlib.pyplot as plt
BIKE_COUNTS = "bike_counts.txt"

def read_data(file):
    days = []
    dates = []
    times = []
    totals = []
    westbounds = []
    eastbounds = []
    
    with open(file, "r") as infile:
        while True:
            day = infile.readline().strip()
            days.append(day)
            date = infile.readline().strip()
            dates.append(date)
            time = infile.readline().strip()
            times.append(time)
            total = infile.readline().strip()
            totals.append(total)
            westbound = infile.readline().strip()
            westbounds.append(westbound)
            eastbound = infile.readline().strip()
            eastbounds.append(eastbound)
            
            
            if day == "":
                break
            
            totals = [int(nums) for nums in totals]
            westbounds = [int(nums) for nums in westbounds]
            eastbounds = [int(nums) for nums in eastbounds]

            
            
        big_list = [days, dates, times, totals, westbounds, eastbounds]
        return big_list
    
    
def total_bikes(lst):
    total = sum(lst)
    string = "The total number of bikes was", total
    return string

            
def west_vs_east(lst1, lst2):
    total1 = sum(lst1)
    total2 = sum(lst2)
    direction = ""
    if total1 > total2:
        direction = "Westbound"
    else:
        direction = "Eastbound"
    string = "More bikes traveled", direction
    return string
    

def max_15_mins(lst):
    maximum = max(lst)
    string = "The max number of bikes observed in one 15 minute segment was", maximum
    return string

def daily_totals(lst1, lst2):
    posItion = 0
    daily_bikes = []
    sun_bikes = 0
    mon_bikes = 0
    tue_bikes = 0
    wed_bikes = 0
    thur_bikes = 0  
    frid_bikes = 0
    sat_bikes = 0
    
    for i in range(len(lst1)):
        curr_day = lst1[i]
        if(curr_day == "Sunday"):
            sun_bikes = sun_bikes + lst2[i]
        elif(curr_day == "Monday"):
            mon_bikes = mon_bikes + lst2[i]
        elif(curr_day == "Tuesday"):
            tue_bikes == tue_bikes + lst2[i]
        elif(curr_day == "Wednesday"):
            wed_bikes = wed_bikes + lst2[i]
        elif(curr_day == "Thursday"):
            thur_bikes = thur_bikes + lst2[i]
        elif(curr_day == "Friday"):
            frid_bikes = frid_bikes + lst2[i]
        elif(curr_day == "Saturday"):
            sat_bikes = sat_bikes + lst2[i]
    
    daily_bikes.append(sun_bikes)
    daily_bikes.append(mon_bikes)
    daily_bikes.append(tue_bikes)
    daily_bikes.append(wed_bikes)
    daily_bikes.append(thur_bikes)
    daily_bikes.append(frid_bikes)
    daily_bikes.append(sat_bikes)
    return daily_bikes

    
    
def main():
    lst = read_data(BIKE_COUNTS)
    lst2 = lst[3].pop(672)
    total_list = lst[3]
    total = total_bikes(total_list)
    print(total)
    print(west_vs_east(lst[4].pop(672),lst[5].pop(672)))
    print(max_15_mins(total_list))
    #daily_totals(lst[0], lst[3])
    print(daily_totals(lst[0], lst[3]))
    
main()