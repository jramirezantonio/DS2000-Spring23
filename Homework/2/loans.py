'''
    Josue Antonio
    DS 2000
    Homework 2 Problem 1
    1/23 - Spring 2023
    loans.py
    
'''

import matplotlib.pyplot as plt
DEBT_VS_TUITION = "debt_vs_tuition.txt"

def main():
    # Gather data - read in school names, avg debt per student, 
    # yearly tuition, and school colors  
    with open(DEBT_VS_TUITION, "r") as infile:
        school1 = infile.readline()
        debt1 = int(infile.readline())
        tuition1 = int(infile.readline())
        color1 = infile.readline().strip()
        school2 = infile.readline()
        debt2 = int(infile.readline())
        tuition2 = int(infile.readline())
        color2 = infile.readline().strip()
        school3 = infile.readline()
        debt3= int(infile.readline())
        tuition3 = int(infile.readline())
        color3 = infile.readline().strip()
    
        
    # Computation - average debt across 3 schools
    avg_debt = (debt1 + debt2 + debt3) / 3
    
    
    # Communication - plot tuition vs. debt where tuition values are on x-axis
    # and debt values are on y-axis
    plt.plot(tuition1, debt1, "o", color = color1, markersize = 12, 
             label = "Northeastern")
    plt.plot(tuition2, debt2, "o", color = color2, markersize = 12, 
             label = "Tufts")
    plt.plot(tuition3, debt3, "o", color = color3, markersize = 12, 
             label = "Brown")

    
    # Change the x limit and y limit  
    plt.xlim(56000, 65000)
    plt.ylim(18000, 25000)
 
    # Label the x and y axes and add a title
    plt.xlabel("Tuition ($)")
    plt.ylabel("Debt ($)")
    plt.title("Tuition Values vs. Debt Values")
    
    # Plot the average debt as a horizontal line
    plt.axhline(avg_debt, color = "peru", label = "average debt")
    
    # Add a legend
    plt.legend()
    
        
    
main()
