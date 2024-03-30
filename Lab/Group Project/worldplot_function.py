#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:44:25 2023

@author: davidku
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:52:58 2023

@author: davidku
"""

import matplotlib.pyplot as plt
import geopandas

def worldplot(countries, scores):
    '''
    parameters: list of all countries - in strings. (the column) AND 
                list of all happiness scores in the same order - in floats
    returns: nothing, just plots the world map where countries are colored 
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

# Example usage
countries = ["United States", "Canada", "Mexico"]
scores = [7.2, 6.5, 5.8]
worldplot(countries, scores)
