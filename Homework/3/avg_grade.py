'''
    Josue Antonio
    DS 2000
    Homework 3 - Problem 1
    1/30/2023 
    avg_grade.py
    
    Test case:
        HW: 95, 94, 97. Avg. = 95.33
        Quiz: 99, 100. Avg. = 99.5
        Viz: 90
        Overall avg. = (0.75)*95.33 + (0.2)*99.5 + (0.05)*90 = 95.9
    
'''

GRADES = "ds2000_grades.txt"
HW = 0.75
QUIZ = 0.20
MINI_VIZ = 0.05

def main(): 
    # Gather Data - initialize hw total, quiz total, viz total, and hw/quiz 
    # counters; read from file
    hw_total = 0
    quiz_total = 0
    hw_counter = 0
    quiz_counter = 0
    viz_total = 0
    
    with open (GRADES, "r") as infile:
        while(True):
            assignment_type = infile.readline().strip()
            assignment_score = infile.readline().strip()
            
            # If we're at end of file, stop
            if assignment_type == "":
                break
            
            assignment_score = float(assignment_score)
            
            # Update totals and counters
            if assignment_type == "HW":
                hw_total += assignment_score
                hw_counter += 1
            elif assignment_type == "Quiz":
                quiz_total += assignment_score
                quiz_counter += 1
            elif assignment_type == "Viz":
                viz_total += assignment_score
        
    # Computation - calculate avg. HW score, avg. quiz score, and 
    # avg. overall score
    if hw_counter == 0:
        avg_hw = 0
    else:
        avg_hw = hw_total / hw_counter
    
    if quiz_counter == 0:
        avg_quiz = 0
    else:
        avg_quiz = quiz_total / quiz_counter
    overall_avg = HW * avg_hw + QUIZ * avg_quiz + MINI_VIZ * viz_total
    
    # Communication - report the avg. HW score, avg. quiz score, and overall 
    # average.
    print("The average HW score is:", round(avg_hw, 2))
    print("The average quiz score is:", round(avg_quiz, 2))
    print("The Viz score is:", round(viz_total,2))
    print("The average overall score is:", round(overall_avg, 2))
                
                
            
    
    
    
main()