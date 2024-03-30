'''
    Josue Antonio
    DS 2000
    Homework 3 - Problem 2
    1/30/2023
    loansv2.py
    
'''

import matplotlib.pyplot as plt
DEBT_VS_TUITION = "debt_vs_tuition2.txt"

def main():
    # Gather Data - initiliaze variables and read in values from file to
    # compute the average debt-to-tuition 
    fraction_total = 0
    schools_counter = 0
    
    with open(DEBT_VS_TUITION, "r") as infile:
        while(True):
            name = infile.readline()
            avg_debt = infile.readline()
            yearly_tuition = infile.readline()
            
            if name == "":
                break
            
            avg_debt = int(avg_debt)
            yearly_tuition = int(yearly_tuition)
            
            # Update debt-to-tuition fraction and schools counter
            fraction_total += avg_debt / (yearly_tuition * 4)
            schools_counter += 1
    
    # Computation - compute avg. debt-to-tuition fraction
    avg_fraction = fraction_total / schools_counter
    
    
    # Read in data from files again to plot tuition vs. debt-to-tuition
    with open(DEBT_VS_TUITION, "r") as infile:
        while(True):
            name = infile.readline()
            avg_debt = infile.readline()
            yearly_tuition = infile.readline()
            
            if name == "":
                break
            
            avg_debt = int(avg_debt)
            yearly_tuition = int(yearly_tuition)
            
            # Computation - compute total tuition, debt-to-tuition for each 
            # school
            total_tuition = yearly_tuition * 4
            debt_to_tuition = avg_debt / total_tuition
            
            if debt_to_tuition <= avg_fraction:
                ratio_color = "green"
            elif debt_to_tuition > avg_fraction:
                ratio_color = "red"
            
            # Communication - plot yearly tuition vs. debt-to-tuition 
            plt.plot(yearly_tuition, debt_to_tuition, "o", color = ratio_color
                     , markersize = 8)
            
    # Communication - change the x/y limits, add lables, add horizontal line
    # with avg. debt-to-tuition fraction across all schools, add title, and
    # add a legend
    plt.xlim(55000, 63500)
    plt.ylim(0.06, 0.12)
    plt.xlabel("Yearly Tuition")
    plt.ylabel("Debt to Tuition Ratio")
    plt.axhline(avg_fraction, color = "orange",
                label = "average debt-to-tuition ratio")      
    plt.title("Debt to Tuition vs. Tuition")
    plt.legend(loc=(1.04, 0))
            
main()          
    
  

