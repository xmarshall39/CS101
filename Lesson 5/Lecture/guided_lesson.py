# How to create/open a file - open() file handles
# "w" = write new file contents
# "a" = append new contents to end of file
# "r" = only read the file

file = open("newfile.txt", "w", encoding="utf-8")
#file = open("newfile.txt", "a", encoding="utf-8")
# How to write to a file
file.write("dl;kfjasl;kdjaso;ifjapsoeijaospfeidf;sj\n")

# Don'f forget to close file!
file.close()

# How to read a text file

file = open("dummy_file.txt", "r", encoding="utf-8")
all_text = file.readlines() # readlines() returns a list
for line in all_text:
    print(line.strip("\n"))
#print(all_text)
file.close()

# How to parse file content: readline()
file = open("dummy_file.txt", "r", encoding="utf-8")
while True:
    line = file.readline()
    if not line:
        break
    print(line.strip("\n"))

file.close()

# with/as keywords
with open("dummy_file.txt", "r", encoding="utf-8") as file:
    all_text = file.readlines()
    for line in all_text:
        print(line.strip("\n"))

print("hey everybody")
    

# what happens when opening a file open in another program???










































'''
# Warm Up Answer:
def anti_vowelify(word):
    new_letters = []
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_letters.append(letter)
    return "".join(new_letters)

print(anti_vowelify("Hello"))
print(anti_vowelify("Darkness"))
print(anti_vowelify("My"))
print(anti_vowelify("Old"))
print(anti_vowelify("Friend"))
'''