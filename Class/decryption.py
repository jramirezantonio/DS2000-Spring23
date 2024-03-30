'''
    DS 2000
    
        a a b c d
        b b c d a
        c c d a b
        d d a b c
    
    Given:
        key - bdad
        word - babd
        
        we should get - abba
    
'''

HEADER = ["a", "b", "c", "d"]
LOOKUP = {"a" : ["a", "b", "c", "d"],
          "b" : ["b", "c", "d", "a"],
          "c" : ["c", "d", "a", "b"],
          "d" : ["d", "a", "b", "c"]}

def decrypt(key, word, header, lookup):
    ''' Fn: decrypt
        Param: key(string), word to decrypt (string), header (list of strings),
        lookup up table (dictionary of string : list)
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


def main():
    key = "bdad"
    word = "babd"
    expected = "abba"
    actual = decrypt(key, word, HEADER, LOOKUP)
    print(actual, expected)


main()