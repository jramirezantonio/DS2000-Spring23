'''
    DS 2001 Final Project
    Josue Antonio
    Naveen Kodwani
    Luke Kreysar
    David Ku
    HappinessReport.py
'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import geopandas


REPORT_FILE = "World Happiness Report 2022.csv"

def plot_histograms(df, cont_cols):
    ''' Function: plot_histrograms
        Parameters: data frame from file, list of columns corresponding to
                all the continuous variables 
        Returns: nothing
        Does: plots histograms for all the continuous variables
    '''
    ranges = []
    for col in cont_cols:
        plt.hist(df[col], bins = 30)
        rng = [df[col].min(), df[col].max()]
        ranges.append(rng)
        plt.title(col)
        plt.ylabel("Frequency")
        plt.show()
    return ranges
         
def plot_scatters(df, factors):
    ''' Function: plot_scatters
        Paramenters: data frame from file, list of happiness factors
        Returns: nothing
        Does: create scatter plots for each factor vs. happiness score
    '''
    for factor in factors:
        plt.scatter(df[factor], df["Happiness score"])
        plt.title(factor + " v.s. " + "Happiness Score")    
        plt.ylabel("Happiness Score")
        plt.show()
        
def gen_heatmap(df):
    ''' Function: gen_heatmap   
        Paramater: data frame from file
        Returns: nothing
        Does: generates a heatmap of the correlation between all the factors
              of given data frame
    '''
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.heatmap(df.corr(), annot = True, fmt='0.1f')
    plt.title("Correlation Matrix")
    
def worldplot(countries, scores):
     '''
     Function: worldplot
     Parameters: list of all countries - in strings. (the column) AND 
                 list of all happiness scores in the same order - in floats
     Returns: nothing
     Does: plots the world map where countries are colored 
                 based on their happiness score
     '''
     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
     ax = world.plot()
     
     index_lst = range(len(countries))
     for i in index_lst:
         if scores[i] < 5:
             # The loop variable is "i", but the inner loop uses "country"
             world[world.name == countries[i]].plot(color='red', ax=ax)
                 
         elif scores[i] >= 5 and scores[i] < 6:
             # The loop variable is "i", but the inner loop uses "country"
             world[world.name == countries[i]].plot(color='yellow', ax=ax)
                 
         else:
             # The loop variable is "i", but the inner loop uses "country"
             world[world.name == countries[i]].plot(color='green', ax=ax)

     plt.show()    
 
def main():
    # Gather data - read csv file and store in data frame
    df = pd.read_csv(REPORT_FILE)
    
    # Explore data types of each column
    print(df.info())
    print(df.shape)
    
    # Which are the 10 happiest countries?
    print(df[["RANK", "Country", "Happiness score"]].head(10))
    
    # Univariate Analysis - histograms for each continuous variables
    # Create list of all headers' names, list of happiness score factors, and 
    # list of all continuous variables  
    columns = []
    factors = []
    for col in df:
        columns.append(col)
    cont_cols = [columns[i] for i in range(2, len(columns))]
    factors = [columns[i] for i in range(6, len(columns))]
    
    # Highest and lowest happiness scores
    print("\nLowest happiness score:", df["Happiness score"].min(), \
          "\nHighest happiness score:", df["Happiness score"].max())
    
    ranges = plot_histograms(df, cont_cols)
    # Happiness score with highest frequency is about 6.1
    #print(ranges)
    
    # Bivariate analysis - scatters of happiness factor vs. happiness score
    # for all happiness scores
    plot_scatters(df, factors)
    
    # Create correlation matrix to see correlation between all variables 
    hm_df = df[["RANK", "Happiness score", "GDP per capita", "Social support",
                "Healthy life expectancy", "Freedom to make life choices",
                "Generosity", "Perceptions of corruption"]]
    gen_heatmap(hm_df)

    # Example usage of worldplot
    #print(df["Countries"])
    # worldplot(countries, scores)
    
main()