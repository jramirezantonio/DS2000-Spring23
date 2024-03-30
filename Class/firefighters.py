'''
    DS 2000
    Josue Antonio
    1/20 - Spring 2023
    Sample code from class - firefighters, overtime, & plotting
    
    Relationship between overtime and total salary
'''
import matplotlib.pyplot as plt

SALARIES = "firefighter_salaries.txt"

def main():
    # Gather data - read in overtime, regular salary, and color
    # from the input file
    
    with open (SALARIES, "r") as infile:
        overtime1 = float(infile.readline())
        regular1 = float(infile.readline())
        color1 = infile.readline().strip()
        
        overtime2 = float(infile.readline())
        regular2 = float(infile.readline())
        color2 = infile.readline().strip()
        
        overtime3 = float(infile.readline())
        regular3 = float(infile.readline())
        color3 = infile.readline().strip()
        
        
    # Computation - tolal salries and the average
    
    total1 = overtime1 + regular1 # is there are to do these 2 lines
    total2 = overtime2 + regular2 # (or more) in 1 line?
    total3 = overtime3 + regular3
    avg_total = (total1 + total2 + total3) / 3
        
    # Communication - plot overtime vs. total salary
    # overtime on x-axis and total salary on y-axis because overtime is the 
    # independent variable (y depends on it
    
    plt.plot(overtime1, total1, "o", color = color1, markersize = 12)
    plt.plot(overtime2, total2, "s", color = color2, markersize = 12)
    plt.plot(overtime3, total3, "x", color = color3, markersize = 12)

    # Change the x limit and y limit
    
    plt.xlim(5000, 30000)
    plt.ylim(120000, 165000)
    
    # Label the x and y axes and add a title
    
    plt.xlabel("Overtime pay ($)")
    plt.ylabel("Total income ($)")
    plt.title("Boston Firefighters Overtime vs Total Income (2021)")
    
    # Plot the average as a horizontal line
    
    plt.axhline(avg_total, color = "peru", label = "average total")
    
    # Add a legend
    plt.legend()


main()