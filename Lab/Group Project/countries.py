#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:25:22 2023

@author: davidku
"""
from pycountry_convert import country_alpha2_to_continent_code, \
    country_name_to_country_alpha2

continents = {
    'NA': 'North America',
    'SA': 'South America', 
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
    'EU': 'Europe'
}


def continent_converter(countries):
    ' parameters: countries, a list of countries'
    continent_name = [continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(country))] for country in countries]
    
    return(continent_name)


# if the above code doesn't work, try this:
''' 
    import pycountry_convert as pc

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Example
country_name = 'Germany'
print(country_to_continent(country_name))

Out[1]: Europe 
'''