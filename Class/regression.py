'''
    DS2000
    Spring 2023
    Sample code from class - linear regression
    
    Data set #1
    * Year, # movies Nicolas Cage  made, precipitation in Boston in March
    * First, check if they are well correlated (movies/rain)
    * If correlation is reaosnable, then we can ask: 
            How much rain will we get if Cage makes 20 moives?
            
    
    Data set #2:
    * Month/year, average home price
    * First, check if they are well correlated (order/price)
    * If correlation is reasonble, then we caks:
        How much will a house cost in JP in 2033?
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

CAGE = "cageweather.csv"
HOUSE = "jp_properties.csv"

def main():
    # Data set 1 --- relationship between Cage movies and rain
    df = pd.read_csv(CAGE, sep = "\t") # what does this delim do
    print(df)
    
    # print out a columm
    print(df["Nicolas Cage Movies"])
    
    # get the correlation of this dataset
    print("Correlation in the Cage dataset...")
    print(df.corr())
    
    # plot the line of best fit
    sns.regplot(x = df["Nicolas Cage Movies"],
                y = df["Boston Precipitation"])
    plt.title("Movies vs. Rain")
    print("These are not super well corrlated, so "
          " we won't try to predict anything.")
    
    # Data set 2 --- relationship between time
    # and the cost of a house in JP
    print("\n\n")
    df = pd.read_csv(HOUSE)
    
    # Print just the first 10 rows of the dataframe
    print(df.head(10))
    
    # Print the last 10 rows of the dataframe
    print(df.tail(10))
    
    # See how many rows there are
    print("Printing shape, which is rows, cols",
          df.shape)
    
    # Add a new columm with the order 
    # Dates don't work well in a line equation
    df["Order"] = df.index
    print(df.head(10))
    
    # How correlated are order and price?
    print("\n\nCorrelation...\n\n")
    print(df.corr())
    
    # Draw the line of best fit
    plt.show()
    sns.regplot(x = df["Order"], # what does this do?
                y = df["Median Sale Price"])
    
    # Get the slope and intercept so we can make
    # a prediction
    line = stats.linregress(x = df["Order"],
                            y = df["Median Sale Price"])
    print("Slope:", line.slope)
    print("Intercept:", line.intercept)
    
    # Make a preidction: given an x, what will y be?
    x = int(input("What x to try?\n"))
    y = x * line.slope + line.intercept
    print("At that time, houses in JP will cost...$",
          y, sep = "")
    
    
    
main()