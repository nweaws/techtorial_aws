# Write the code to check the student pass the class or not.
# to be able to pass the class student needs to have at least 65 score from
# the exam and student needs to attend the at least 80 persent of all the classes.
# to calculate the average score we need to take 20 percent of first exam score
#and 30 percent of second exam score and 50 percent of the third exam score.
#we are given variable for three exam score and one variable
#for attendance to classes. if all condition are met,
#print True at thje end. If not print False.


exam1 = 60
exam2 = 40
exam3 = 90

attendancy = 80

avg_score = exam1 * 20/100 +exam2 * 30/100 + exam3*50/100

is_attendancy_enough = attendancy >= 80

is_avg_score_enough = avg_score >= 65

can_pass = is_attendancy_enough and is_avg_score_enough
print("Average score of the student is",avg_score)
print("Attendancy of student is ",attendancy)
print("Student can pass the class",can_pass)