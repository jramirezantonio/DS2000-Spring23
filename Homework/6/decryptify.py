'''
    Josue Antonio
    DS 2000
    Homework 6 Problem 2/3
    3/19 - Spring 2023
    decryptify.py
'''

import csv

VIGINERE_FILE = "vigenere.csv"
KEYS_FILE = "keys.txt"

def make_decryption(lst):
    ''' Fn: make_decryption
        Param: 2d list
        Returns: dictionary
        Does: isolates column 0 of list and turns them into keys of the dict 
              with the rest of each row being the value for each key
    '''
    dct = {}
    for elt in lst:
        dct[elt[0]] = elt[1:]
    return dct

def decrypt_word(header, lookup, word, key):
    ''' Fn: decrypt_word
        Param: header (list of strings), lookup up table
        (dictionary of string : list), word to decrypt (string), key(string)
        Returns: string
        Does: apply the vigenere cipher, given the key/word we look up each 
              letter of the key in the dict, find the corresponding letter of 
              the word and get its value from the header
    '''
    decrypted = ""
    for i in range(len(key)):
        curr_letter = key[i]
        lst = lookup[curr_letter]
        curr_encrypted = word[i]
        pos = lst.index(curr_encrypted)
        decrypt_letter = header[pos]
        decrypted += decrypt_letter
    return decrypted

def read_csv(filename):
    ''' Fn: read_csv
        Param: filename string
        Returns: (list, list) tuple
        Does: reads every line of csv file storing the first line in a 
              "header" list, and the rest of the lines in a separate 2d list
    '''
    data, header = [], []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        header = next(reader)
        for row in reader:
            data.append(row)
    return data, header

def read_txt(filename):
    ''' Fn: read_txt
        Param: filename string
        Returns: 1d list
        Does: reads every line and adds it to 1d data list that gets returned
    '''
    data = []
    with open(filename, "r") as infile:
        for line in infile:
            keys = line.strip().split()
            data += keys
    return data
    
def main():
    # Gather data - prompt user for encrypted message
    enc_message = input("Enter encrypted message:\n")
    # Read text with keys and store them
    keys = read_txt(KEYS_FILE)
    # Read csv file, store header list, and rest of data separately
    data, header = read_csv(VIGINERE_FILE)
    # Remove empty string from header
    header = header[1:]
    
    # Computation - create lookup dictionary
    lookup = make_decryption(data)
    # Decrypt enc_message using each key in keys list
    for key in keys:
        decrypted = decrypt_word(header, lookup, enc_message, key)
        
        # Communication - check if current decrypted word is a link and if so,
        # print it to the user - you have found your right encrypted link :)
        if decrypted.startswith("https://bit.ly"): 
            print("\nThe mysterious link is:", decrypted)
    
    
    
    
    
    
   				 
    
main()