



import csv
import matplotlib.pyplot as plt


CEREAL_FILE = "cereal.csv"

def read_file(filename):
    ''' Function: read_file
        Parameters: filename (string) for a CSV file
        Returns: 2d list of what the file contains
        Does: Reads every line of the file, except the header,
              and stored in a 2d list which is returned at the end
    '''
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        next(reader)
        for row in reader:
            data.append(row)
    return data

def subset_data(data, col1, col2, col3):
        lst = []
        for row in data:
            lst2 = []
            lst2.append(row[col1])
            lst2.append(row[col2])
            lst2.append(row[col3])
            lst.append(lst2)
        return lst

def similarity(x1,y1,x2,y2):
    euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    return euclidean_distance


def find_closest(abs_fav, dataset):
    # closest_distance = 1000
    # current_cereal = []
    # cereal_names = []
    # closest_pos = 0
    # pos = 0
    # for cereal in :
    #     cereal_names.append(cereal[0])
    #     current_cereal.append(cereal[1])
    #     current_cereal.append(cereal[2])
    #     print(current_cereal)
    #     current_cereal = [int(value) for value in current_cereal]
    #     similarity(cereal[0], current_cereal[0], cereal[1], current_cereal[1])
    #     if similarity < closest_distance:
    #         closest_distance = similarity
    #         closest_pos = pos
    #     pos += 1
    
    euclidean_distance1 = 100
    shortest_dist_pos = 0
    for row in dataset:
        distances = []
        dist = similarity(float(row[1]), float(row[2]), abs_fav[0][1], abs_fav[0][2])
        distances.append(dist)
    for distance in distances:
        if distance <   euclidean_distance1:
            euclidean_distance1 = distance
            shortest_dist_pos = distance
    
    
       
    
    

def main():
    cereal_data = read_file(CEREAL_FILE)
    #print(cereal_data)
    abs_fave = [["Cracklin Oat Bran", 3, 3]] 
    subset_cereal = subset_data(cereal_data, 0, 4, 5)
    print(find_closest(abs_fave, subset_cereal))
    

    
    
    
main()