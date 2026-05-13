'''
Lesson 3 Exercise - Mean, Median, Mode, Range
Objective: Learn how to use basic list operations using built-in and member functions to solve problems
Below, I'll demonstrate a few useful functions to manipulate lists. You must use the following functions to solve the problems below:
len(), min(), max(), sum(), sorted()
'''

class_a_grades = [90, 33, 56, 94, 34, 40, 75, 74, 77, 86, 90, 86, 55, 12, 43]
class_b_grades = [30, 66, 33, 44, 55, 66, 77, 55, 44, 22, 11, 33, 99, 99, 99, 99]
class_c_grades = [23, 65, 22, 77, 98, 58, 67, 89, 77, 88, 0, 92, 94, 74]

students_in_a = len(class_a_grades)
students_in_b = len(class_b_grades)
students_in_c = len(class_c_grades)

print(f"Class A Grades: {class_a_grades}")
print(f"Class B Grades: {class_b_grades}")
print(f"Class C Grades: {class_c_grades}")

print(f"Class A has {students_in_a} students | Class B has {students_in_b} students | Class C has {students_in_c} students")
print("") #Prints an empty line

# ==========================================================================================================================
# ==========================================================================================================================

class_a_lowest = min(class_a_grades)
print(f"The lowest score in class A is {class_a_lowest}")

#Note that we can use the function in our print like below instead of creating a variable. Same result.
print(f"The highest grade in class C is {max(class_c_grades)}")

print(f"The sum of class B scores is {sum(class_b_grades)}")
print("")

# ==========================================================================================================================
# ==========================================================================================================================

sorted_a_grades = sorted(class_a_grades)
print(f"Here are class A scores from lowest to highest: {sorted_a_grades}")

print(f"sorted() is a function that returns a *copy* and therefore doesn't change the original grades list. Watch:")
print(f"Class A Grades: {class_a_grades}")

'''
With all this in mind, your assignment is as follows:
1.) In a new .py file Create 3 grades lists just like the ones above, but provide your own numbers. 
    - Each class must have at least 5 students
    - The class lists must be global variables

2.) You will first create 3 functions for determining the mean, median, and range of a single list
    - Each function must take one parameter (a list)
    - Each function must return one number (a grade)
    - Median will be the hardest, try that last
3.) Create a 4th function called "print_list_stats"

    - This function must in 2 parameters: a list of grades, and string representing the teacher's name
    - This function must print the mean, median, and range for each class
    - Add an additional message evaluating the teacher based on the student scores
    
4.) Call print_list_stats() once for each class list

# ==========================================================================================================================

Bonus 1.) Making use the List member function append(), call print_list_stats() on the combo of all classes
            - Documentation on append() can be found here: https://www.w3schools.com/python/ref_list_append.asp
            - You only need to call print_list_stats() ONCE for this bonus
            - For class name, just use "All Classes"

Bonus 2.) Like the others, write a final function to calculate Mode
            - This function *could* return one value, but should it?
            - Add the output of this function to print_list_stats()
Bonus 2.5) How did you calculate Mode? If you used loops, try writing an alternative mode function that does not.
            If you didn't, try writing a version that uses loops :)
            If you can't think of an answer, just skip this

Bonus 3.) Create a 4th list using random student stats
            - The size of this list must match the smallest class among A, B, and C
            - No students in the random class will score lower than a 10
            - Run print_list_stats() on this random class

Bonus 4321.) Using the All Classes list, create a new 5th list featuring a random selection of existing student grades
            - First, make a copy of the All Classes list. Our solution will modify the list unlike sorted()
            - For this, use the member function copy()
            - This "sample class" must be the size of the largest class among A, B, and C
            - You cannot use random.randint() for this assignment
            - You instead must use random.shuffle() and list slicing
            - Documentation
                - https://www.geeksforgeeks.org/python/python-list-slicing/
                - https://www.w3schools.com/python/ref_random_shuffle.asp
'''