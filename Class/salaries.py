'''
    DS2000
    Spring 2023
    Sample code from class - boston salaries - Jan 17th

    Test case: average of data from the file 
    avg of 131111.83, 63698.64, 111431.15, 39508.98, 27228.00
'''

SALARY_FILE = "boston_salaries.txt"

def main():
    # Gather data - read salaries from file
    with open(SALARY_FILE, "r") as infile:
        salary1 = float(infile.readline())
        salary2 = float(infile.readline())
        salary3 = float(infile.readline())
        salary4 = float(infile.readline())
        salary5 = float(infile.readline())
    
    # Computation - what's the average salary
    avg = (salary1 + salary2 + salary3 + salary4 + salary5) / 5
    max_salary = max(salary1, salary2, salary3, salary4, salary5)
    
    
    # Communication - report to the user!
    print("Average Boston salary (from 5 samples) is: $", avg, sep = "")
    print("Highest Boston salary (from 5 samples) is: $", max_salary, sep = "")
        
main()