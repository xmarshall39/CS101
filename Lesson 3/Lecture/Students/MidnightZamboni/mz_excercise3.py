
def classMean (gradesList):
    totalPoints = sum(gradesList)
    mean = totalPoints/len(gradesList)
    return mean

def classMedian (gradesList):
    sortedGrades = sorted(gradesList)
    middleInd = round(len(sortedGrades)/2)
    median = sortedGrades[middleInd]
    return median

def classRange (gradesList):
    sortedGrades = sorted(gradesList)
    gradeRange = sortedGrades[-1] - sortedGrades[0]
    return gradeRange

def print_list_stats (gradesList, teacherName):
    listMean = classMean(gradesList)
    listMedian = classMedian(gradesList)
    listRange = classRange(gradesList)

    if listMean < 64:
        performance = "subpar"

    elif listMean > 65 and listMean < 84:
        performance = "as expected"

    else:
        performance = "well"

    print(f"The class scores entered have an average grade of {listMean}, a median grade of {listMedian}, and a range of {listRange}. \n {teacherName} has performed {performance}.")




class_a_grades = [96,75,46,82,45]
class_b_grades = [34,85,53,67,23]
class_c_grades = [87,56,56,97,43]

teacherAName = "Joe"
teacherBName = "Sherry"
teacherCName = "Becky"

print_list_stats(class_a_grades, teacherAName)
print_list_stats (class_b_grades, teacherBName)
print_list_stats(class_c_grades, teacherCName)