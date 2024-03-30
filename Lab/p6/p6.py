'''
    Josue Antonio
    p6.py
'''

BEYONCE_FILE = "beyonce.txt"
TAYLOR_FILE = "taylor.txt"

def read_txt(file):
    with open(file, "r") as infile:
        data = []
        for line in infile:
            data.append(line.strip().split(" "))
    new_list = []
    for elt in data:
        new_list.extend(elt)  
    
    return new_list
            
def flat_2d(list):
    new_list = []
    for elt in list:
        new_list.extend(elt)
    return(new_list)

def word_counter(list):
    counter_dict = {}
    for word in list:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1
    return counter_dict
        
def predictor(artist1, dict1, artist2, dict2, lyric):
    split_lyric = lyric.split(" ")
    d = word_counter(split_lyric)
    counter1 = 0
    counter2 = 0
    for word, count in d.items():
        if word in dict1:
            counter1 += 1
        elif word in dict2:
            counter2 += 1
    if counter1 > counter2:
        return artist1
    elif counter2 > counter1:
        return artist2
    else:
        print("Unknown prediction")
        return artist1 + " or " + artist2
def main():
    beyonce = read_txt(BEYONCE_FILE)
    taylor = read_txt(TAYLOR_FILE)
    b_dict = word_counter(beyonce)
    t_dict = word_counter(taylor)
    
    lyric = input("Enter a lyric!\n")
    print("That lyric was probably written by:",predictor("Beyonce", b_dict, 
                                                    "Taylor", t_dict, lyric))
    
    
main()