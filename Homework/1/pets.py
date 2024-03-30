'''
    Josue Antonio
    DS 2000
    Homework 1 Problem 1
    1/17 - Spring 2023
    pets.py 
    
    Test case #1
    Belita = 40 pounds, 6 years
    Nana = 60 pounds, 8 years
    Expected: Belita weighs 0.67x what Nana weighs.
              Belita's age is 0.75x Nana's age.
              
    Test case #2
    Josevito = 80 pounds, 0.67 years
    Titas = 20 pounds, 10 years
    Expected: Josevito weighs 4.0x what Titas weighs.
              Josevito's age is 0.07x Tita's age.
              
'''

def main():
    # Gather data - prompt the user for names of pets and their respective 
    # weights and ages
    
    pet_name1 = input("What is your first pet's name?\n")
    pet_weight1 = float(input("What is their weight in pounds?\n"))
    pet_age1 = float(input("What is their age in years?\n"))
    pet_name2 = input("What is your second pet's name?\n")
    pet_weight2 = float(input("What is their weight in pounds?\n"))
    pet_age2 = float(input("What is their age in years?\n"))
    
            
    # Computation - weight and age differentials
    
    weight_differential = pet_weight1 / pet_weight2
    age_differential = pet_age1 / pet_age2
    
    # Communication - report the differentials (rounded to 2 places)
    
    print(pet_name1, " weighs ", round(weight_differential,2), "x what ", 
          pet_name2, " weighs.", sep = "")
    print(pet_name1, "'s age is ", round(age_differential,2), "x ", 
          pet_name2, "'s age.", sep = "")

main()  