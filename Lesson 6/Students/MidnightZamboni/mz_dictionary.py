file = open("en-es.xml", "r", encoding="utf-8")

enWords = {}
esWords = {}
currentWord = ""

for i in range(100):#while True:
    dictLine = file.readline()
    # if "<w>" in dictline:
        #currentWord = ""
    # if </w> in dictline:
        #wordNo += 1
    if "<c>" in dictline:
        #add word to dictionary
        #set a variable indicating the current word
    if "<d>" in dictline:
        #assign definition in dictionary using current word



    if "<c>" in dictLine:
        engWord = dictLine.strip("\t", "<c>", "<c>", "\n")
        enWords[engWord] = "def"

    if not dictLine:
        break

print(enWords)
