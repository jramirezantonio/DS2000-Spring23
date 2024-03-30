'''
    DS2000
    Spring 2023
    Sample code from class - Jan 10th
    
    Grizz and Carol's average score
'''

def main():
    # Gather Data - get get grizz and carol's friendliness (0-10)
    grizz = int(input("What is Grizz's friendliness level?\n"))
    carol = int(input("What is Carol's friendliness level?\n"))
    
    # Computation - compute the average score
    avg = (grizz + carol) / 2
    
    
    # Communication - report out the answer
    print("Their average friendliness is:", avg)
    
main()

