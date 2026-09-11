file = open("en-es.xml", "r", encoding="utf-8")

enWords = {}
esWords = {}

for i in range(100):#while True:
    dictLine = file.readline()
    if "<c>" in dictLine:
        engWord = dictLine.strip("\t", "<c>", "<c>", "\n")
        enWords[engWord] = "def"

    if not dictLine:
        break

print(enWords)