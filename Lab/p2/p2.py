'''
    Bam and Josue
    DS 2001
    Practicum #2 Coding Assignment
    26th Jan
    
'''

import matplotlib.pyplot as plt
DATA = "punxsutawney.txt"

def main():
    with open(DATA, "r") as infile:
        
        # Gather Data - read in year, shadow, and avg temp from
        # punxsutawney.txt file
        year1 = int(infile.readline())
        shadow1 = infile.readline().strip()
        temp1 = float(infile.readline())
        
        
        year2 = int(infile.readline())
        shadow2 = infile.readline().strip()
        temp2= float(infile.readline())
        
        year3 = int(infile.readline())
        shadow3 = infile.readline().strip()
        temp3 = float(infile.readline())
        
        year4 = int(infile.readline())
        shadow4 = infile.readline().strip()
        temp4 = float(infile.readline())
        
        year5 = int(infile.readline())
        shadow5 = infile.readline().strip()
        temp5 = float(infile.readline())
        
       
        # Computation - determine if the avg. temp is greater than equal to
        # 52 deg. F, and check if the prediction is accurate
        if temp1 >= 52:
            measured_temp1 = True
        else:
            measured_temp1 = False
        
        if measured_temp1 == True and shadow1 == "No Shadow":
            accurate1 = True
            color1 = "green"
            label1 = "accurate"
        elif measured_temp1 == False and shadow1 == "Full Shadow":
            accurate1 = True
            color1 = "green"
            label1 = "accurate"
        else:
            accurate1 = False
            color1 = "red"
            label1 = "not accurate"
        
        if temp2 >= 52:
            measured_temp2 = True
        else:
            measured_temp2 = False
        
        if measured_temp2 == True and shadow2 == "No Shadow":
            accurate2 = True
            color2 = "green"
            label2 = "accurate"
        elif measured_temp2 == False and shadow2 == "Full Shadow":
            accurate2 = True
            color2 = "green"
            label2 = "accurate"
        else:
            accurate2 = False
            color2 = "red"  
            label2 = "not accurate"
            
        if temp3 >= 52:
            measured_temp3 = True
        else:
            measured_temp3 = False
        
        if measured_temp3 == True and shadow3 == "No Shadow":
            accurate3 = True
            color3 = "green"
            label3 = "accurate"
        elif measured_temp3 == False and shadow3 == "Full Shadow":
            accurate3 = True
            color3 = "green"
            label3 = "accurate"
        else:
            accurate3 = False
            color3 = "red"
            label3 = "not accurate"
            
        if temp1 >= 52:
            measured_temp4 = True
        else:
            measured_temp4 = False
        
        if measured_temp4 == True and shadow4 == "No Shadow":
            accurate4 = True
            color4 = "green"
            label4 = "accurate"
        elif measured_temp4 == False and shadow4 == "Full Shadow":
            accurate4 = True
            color4 = "green"
            label4 = "accurate"
        else:
            accurate4 = False
            color4 = "red"
            label4 = "not accurate"
            
        if temp1 >= 52:
            measured_temp5 = True
        else:
            measured_temp5 = False
        
        if measured_temp5 == True and shadow5 == "No Shadow":
            accurate5 = True
            color5 = "green"
            label5 = "accurate"
        elif measured_temp5 == False and shadow5 == "Full Shadow":
            accurate5 = True
            color5 = "green"
            label5 = "accurate"
        else:
            accurate5 = False
            color5 = "red"
            label5 = "not accurate"
        
        
        # Report - illustrate accuracy with visualization 
        plt.plot(year1, temp1, "o", markersize = 12, color = color1, label = label1)
        plt.plot(year2, temp2, "o", markersize = 12, color = color2, label = label2)
        plt.plot(year3, temp3, "o", markersize = 12, color = color3)
        plt.plot(year4, temp4, "o", markersize = 12, color = color4)
        plt.plot(year5, temp5, "o", markersize = 12, color = color5)
        
        plt.title("Punxutawney Phil's accuracy")
        plt.xlabel("Year")
        plt.ylabel("Avg. US temp. in February (F)")
        
        plt.xlim(2011, 2017)
        plt.ylim(31, 40)
        plt.legend()
        
        
        
        
        
        
        
            
    
        
    
main()