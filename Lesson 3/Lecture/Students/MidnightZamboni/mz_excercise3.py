import math
import random

def classMean (gradesList):
    totalPoints = sum(gradesList)
    mean = totalPoints/len(gradesList)
    return mean

def classMedian (gradesList):
    sortedGrades = sorted(gradesList)
    middleInd = math.floor(len(sortedGrades)/2)
    median = sortedGrades[middleInd]
    return median

def classRange (gradesList):
    sortedGrades = sorted(gradesList)
    gradeRange = sortedGrades[-1] - sortedGrades[0]
    return gradeRange

'''
4 Components:
- Current Grade
- Current High Score
- High Score Grades List
- Current Grade's Score

[0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4]

(1)
Current Grade = 0
Current High Score = 1
High Score Grades List = [0]
Current Grade Score = 1

(3)
Current Grade = 0 (index = 2)
Current High Score = 3
High Score Grades List = [0]
Current Grade Score = 3
...

(4)
Current Grade = 1
Current High Score = 2
High Score Grades List = [0]
Current Grade Score = 1
...

(8)
Current Grade = 2
Current High Score = 3
Current Grade Score = 3
High Score Grades List = [0, 2]

(9)
Current Grade = 2
Current High Score = 4
Current Grade Score = 4
High Score Grades List = [2]

'''

'''
take in a list
sort the list (least to greatest)
we set an empty list to hold future values
integer starting at zero 

we take the first value from the sorted list and add it to the empty list

- Initialize variables
    - currentCount = 1
    - highestCount = 0
    - last_grade = -1
- For grade in grades:
    - if grade == last_grade:
        - incriment currentCount
    - if currentCount > highestCount:
        - Clear ModeList
        - Add grade to ModList
        - highestCount = currentCount
    - else if currentCount == highestCount:
        - Add grade to ModeList
    - Set last_grade to grade

- Return ModeList


'''
def classMode(gradesList):
    repeatedGrades = []
    gradesList.sort()
    currentCount = 1
    highestCount = 0
    last_grade = -1

    for i in range(len(gradesList)):
        if gradesList[i] == last_grade:
            currentCount += 1
            if currentCount > highestCount:
                repeatedGrades.clear() 
                repeatedGrades.append(gradesList[i])
                highestCount = currentCount
            elif currentCount == highestCount:
                repeatedGrades.append(gradesList[i])

        last_grade = gradesList[i]
        
    return repeatedGrades
        


def randomClass (totalGrades):
    randoClass = []
    indGrades = 1
    while indGrades <= totalGrades:
        newGrade = random.randrange(10,100)
        randoClass.append(newGrade)
        indGrades+=1
    
    return randoClass


def print_list_stats (gradesList, teacherName):
    listMean = classMean(gradesList)
    listMedian = classMedian(gradesList)
    listRange = classRange(gradesList)
    listMode = classMode(gradesList)


    if listMean < 64:
        performance = "underwhelmingly"

    elif listMean > 65 and listMean < 84:
        performance = "as expected"

    else:
        performance = "well"

    print(f"The class scores entered have an average grade of {listMean}, a median grade of {listMedian}, and a range of {listRange}.")
    if len(listMode)>0:
        print(f"The mode of this class's grades is {listMode}.")
    
    
    print(f"\n {teacherName} has performed {performance}.")


def all_class_stats (classA, classB, classC, classD, schoolName):
    fullClass = []
    fullClass.extend(classA)
    for i in range(len(classA)):
        fullClass.append(classA[i])
        i += 1
    for i in range(len(classB)):
        fullClass.append(classB[i])
        i += 1
    for i in range(len(classC)):
        fullClass.append(classC[i])
        i += 1
    for i in range(len(classD)):
        fullClass.append(classD[i])
        i += 1
    print_list_stats(fullClass, schoolName)

def rand_select_grades (classA, classB, classC, gradeAmount):
    fullClass = []
    for i in range(len(classA)):
        fullClass.append(classA[i])
        i += 1
    for i in range(len(classB)):
        fullClass.append(classB[i])
        i += 1
    for i in range(len(classC)):
        fullClass.append(classC[i])
        i += 1
    sampleClass = fullClass.copy()
    random.shuffle(sampleClass)
    randomSelection = sampleClass[0:(gradeAmount)]
    
    return randomSelection






class_a_grades = [96,75,46,82,45]
class_b_grades = [34,85,82,67,23]
class_c_grades = [87,56,56,97,82]
class_d_grades = randomClass(5)

teacherAName = "Joe"
teacherBName = "Sherry"
teacherCName = "Becky"
teacherDName = "John"

schoolName = "Xavier's Coding School for Artists"


'''

print_list_stats(class_a_grades, teacherAName)
print_list_stats (class_b_grades, teacherBName)
print_list_stats(class_c_grades, teacherCName)
print_list_stats(class_d_grades, teacherDName)

print("\n")
'''

all_class_stats(class_a_grades, class_b_grades, class_c_grades, class_d_grades, schoolName)

