

#Veera want lose 19 pounds in one month.
#there are multiple condition to lose 10 pounds in a month
#veera needs to walk 10000 steps daily or need to run at least 4 miles a day .
#and addition to those ,veera needs eat less than 1500 calories daily.
#we should creat a program to calculate if veera can losse weight or not

walking_steps = 5000
running_distance = 3.9
daily_calory = 1499

can_loose_weight = (walking_steps>= 10000 or running_distance >=4) and daily_calory <1500

print("veera can lose weight",can_loose_weight)