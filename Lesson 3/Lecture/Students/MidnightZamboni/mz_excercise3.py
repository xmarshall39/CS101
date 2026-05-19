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
def classMode (gradesList):
    repeatedGrade = []
    singleGrades = []

    for i in range(len(gradesList)):
        if gradesList[i] not in singleGrades:
            singleGrades.append(gradesList[i])
        if gradesList[i] in singleGrades:
            repeatedGrade.append(gradesList[i])
    
    return repeatedGrade
'''

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


    if listMean < 64:
        performance = "underwhelmingly"

    elif listMean > 65 and listMean < 84:
        performance = "as expected"

    else:
        performance = "well"

    print(f"The class scores entered have an average grade of {listMean}, a median grade of {listMedian}, and a range of {listRange}. \n {teacherName} has performed {performance}.")


def all_class_stats (classA, classB, classC, classD, schoolName):
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
class_b_grades = [34,85,53,67,23]
class_c_grades = [87,56,56,97,43]
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


all_class_stats(class_a_grades, class_b_grades, class_c_grades, schoolName)
'''
gradeslist =rand_select_grades(class_a_grades, class_b_grades, class_c_grades, 5)

print(gradeslist)
