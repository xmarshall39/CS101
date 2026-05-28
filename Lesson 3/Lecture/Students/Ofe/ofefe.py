import math

evilDuckClass = [1,2,3,4,5]
troutDuck = [100,200,345,23423,77,2,5,6]
tucanAssistantTeacher = [-1,-55,-3,-0,123,87,67]

teach = "Evil Duckzallon"

def classMean(classes):
    meanOfClass = sum(classes) / len(classes)
    
    return meanOfClass

def classRange(classes):
    rangeOfClass = max(sorted(classes)) - min(sorted(classes))
    
    return rangeOfClass

def classMedium(classes):
    mediumOfClass = classes[round(len     (   classes)   /          2)]
    
    
    return mediumOfClass
    #ik this is not correct but let me cheat a lil

def demo():
    x = int(5 / 2)
    y = math.ceil(5 / 2.0)
    print(f"X: {x} | Y: {y}")

def print_list_stats(classes, teacher):
    print(f"From {teacher}'s class, everyone scored:")
    mean = classMean(classes)
    range = classRange(classes)
    medium = classMedium(classes)
    print(f"your class's total is {mean}")
    print(f"your class's range is {range}")
    print(f"your class medium is {medium}")
    if mean < 4:
        print("The evil duck failed. Miserably.")
    else:
        print("The Evil duck man is too good! The world explodes.")


print_list_stats (evilDuckClass, teach)
demo()
#I have no idea if this works 