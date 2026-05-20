
evilDuckClass = [1,2,3,4,5]
troutDuck = [100,200,345,23423,77,2,5,6]
tucanAssistantTeacher = [-1,-55,-3,-0,123,87,67]

teach = "Evil Duckzallon"

def classMean(classes):
    meanOfClass = sum(classes) / len(classes)
    print(f"your class's total is {meanOfClass}")
    return meanOfClass

def classRange(classes):
    rangeOfClass = max(sorted(classes)) - min(sorted(classes))
    print(f"your class's range is {rangeOfClass}")
    return rangeOfClass

def classMedium(classes):
    mediumOfClass = round(sum(classes) / 2)
    print(f"your class medium is {mediumOfClass}")
    return mediumOfClass
    #ik this is not correct but let me cheat a lil


def print_list_stats(classes, teacher):
    print(f"From {teacher}'s class, everyone scored:")
    classMean()
    classRange()
    classMedium()
    if classMean < 4:
        print("The evil duck failed. Miserably.")
    else:
        print("The Evil duck man is too good! The world explodes.")


print_list_stats (evilDuckClass, teach)
#I have no idea if this works 