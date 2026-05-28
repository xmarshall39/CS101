# Guided Lesson 4: Strings are kinda just lists
"hello"
['h' , 'e', 'l']
# Strings are just lists of *characters*
# Therefore, I can use the index operator [] and loops on strings
x = "hello"
x_list = ['h' , 'e', 'l', 'l', 'o']
print(x[0]) # 'h'
print(len(x))
sorted_x = sorted(x)
print(sorted_x)

for letter in x:
    print(letter)

i = 0
while i < len(x):
    print(x[i])
    i += 1


# len(), sorted(), and more work on strings too!
# However, strings are IMMUTABLE (in python) and FIXED SIZE (in all languages)
x_list[0] = 'b'
x_list.append('y')
print(x_list)
#x[0] = 'b'
#print(x)
# What else can we do...
# String concatenation (the + operator)
concat_x = "hello" + " world" + "dfkljads" + 'dasfad' + "sdfkjasdlkfjas;lfkj" + str(48937020)

print(concat_x)
# upper(), lower(), isdigit(), isalpha(), 
upper_x = x.upper()
lower_x = upper_x.lower()
another_lower = "Uppercase Sometimes But Not all the times".lower()

print(upper_x)
print(lower_x)
print(another_lower)

digit_ex1 = "hello123".isdigit()
digit_ex2 = "123456".isdigit()
digit_ex3 = "why why why".isdigit()

print(digit_ex1)
print(digit_ex2)
print(digit_ex3)

# *in* keyword for strings and lists, split(), join()

if 'h' in x:
    print('h in hello string')

if 'b' in x_list:
    print('b in hello list')

split_hello = list("hello"); #"hello".split()
print(split_hello)

split_func_hello = "hello".split("|")

joined_hello = "|".join(split_hello)
print(joined_hello)

# Pt.2 Nesting:
# This refers to using some coding feature within itself
nested_list = [["hello", "goodbeye", "salutations"], [1, 2, 3, 4, 5, 6], [9.7, 1.4, 3.4]]
for inner_list in nested_list:
    print(inner_list)
    for element in inner_list:
        print(element)
# if statemenets can be nested

# Example: Complex branching

# We may use this term when lists are contained in another list

# Example: 2D Array for map (9-5 degrees)

#for/while loops can be nested

# Example Use Case: Iterating over 2D Arrays

# there are no restrictions to how we do that

# An Aside: Importing local files and relative directories
#import example_module
#from .. import example_module_2
#from ....CS101 import example_module_3
# Next time: files
