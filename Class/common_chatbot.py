'''
    Sample code from class - March 3rd
    
    What were the unhinged words of the Bing chat bot?
    What was the word it used most frequently?
'''

FILENAME = "chatbot.txt"
def read_txt(filename):
    ''' Fn.: read_txt
        Param.: filename, a string
        Return: list of strings
        Does: iterate over each of the file, split on spaces, and append each
              word to a list
    '''
    words = []
    with open(filename, "r") as infile:
        for line in infile:
            words += line.split()
    return words

def wordcount(lst):
    ''' Fn: wordcount
        Param.: list of strings, including repeats
        Returns: a dct, where key = word and value = count
        Does: iterate over the list of words, updating the value in the dct
                as we go
    '''
    wc = {}
    for word in lst:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    return wc

def find_max(dct):
    ''' FN: find_max
        Param.: dictionary where key is anything, but value must be a number
        Return: key, value pair where value is highest
        Does: iterate over given dct., find highest value and return both the 
                the value and its key
    '''
    max_val = -1
    max_key = ""
    for key, value in dct.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key, max_val

def main():
    # Gather data - read in the text file to a 1d list
    words = read_txt(FILENAME)
    
    # Computation - turn the list of words into a dictionary
    dct = wordcount(words)
    
    most_common = []
    while len(most_common) < 10:
        max_word, max_count = find_max(dct)
        most_common.append(max_word)
        del(dct[max_word])
    print(most_common)
    
    # Computation - which word was said the most?
    max_word, max_count = find_max(dct)
    
    # Communication - report the most word
    print("Chatbot said this the most...", max_word)
    
    

main()