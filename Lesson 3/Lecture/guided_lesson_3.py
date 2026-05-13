# GUIDED LESSON 3:

import random
# Review boolean statements
def doX():
    print("hi")

x = True
y = False

op = "or"

tt = not (True or True)
tf = not (True or False)
ft = not (False or True)
ff = not (False or False)

x = random.randint(0, 100)
#print(f"\nX is : {x}")
#if x >= 50 and x <= 75:
    #print("Between (and including) 50 and 75")

#if not x < 25 or not x > 75 and x % 2 == 0:
    #print("Number at the extreme limits and even")


print(f"True {op} True = {tt} | True {op} False = {tf} | False {op} True = {ft} | False {op} False = {ff}")

if "b" not in "manzana":
    print("it's not in there!")
elif "z" in "manzana":
    print("z is in there!!")
elif "a" in "manzana":
    print("it's definitely in there this time!")
elif "d" in 'manzana':
    print ("this is too much...")
else:
    print("it's not in there")




# Recap how lists and index-based selection works
string_list = ["up", "down", "left", "right", "Up", "Down", "Left", "Right"]
class_a_grades = [90, 33, 56, 94, 34, 40, 75, 74, 77, 86, 90, 86, 55, 12, 43]
first_student_grade = class_a_grades[0]
number_of_grades = len(class_a_grades) # 15
last_student_grade = class_a_grades[number_of_grades - 1]

print(f"\n\nfirst grade: {first_student_grade} | number of grades: {number_of_grades} | last grade: {last_student_grade}")

sum_of_all_grades = sum(class_a_grades)
highest_grade = max(class_a_grades)
lowest_grade = min(class_a_grades)

print(f"| highest: {highest_grade} | lowest: {lowest_grade}")

sorted_grades = sorted(class_a_grades)
sorted_grades.reverse()
print(f"Grades: {class_a_grades}")
print(f"Sorted Grades: {sorted_grades}")

print(f"Sorted Strings: {sorted(string_list)}")
print(f"Min: {min(string_list)} | max: {max(string_list)}")


# Teach for loop implementation and while loops

#for grade in class_a_grades:
    #print(grade)

num_grades = len(class_a_grades)
grade_range = list(range(num_grades))
print(grade_range)

#for i in range(len(class_a_grades)):
    #print(class_a_grades[i])


i = 0
while True:
    print(class_a_grades[i])
    break
    #i += 1


'''''''''
i = 0
print(class_a_grades[i])
i = 1
print(class_a_grades[i])
i = 2
print(class_a_grades[i])
'''

'''
grade = class_a_grades[0]
print(grade)
grade = class_a_grades[1]
print(grade)
grade = class_a_grades[2]
print(grade)
#...
'''