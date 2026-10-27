file = open("en-es.xml", "r", encoding="utf-8")
oxford = open("Oxford English Dictionary.txt", "r", encoding="utf-8")

enWords = {}
currentWord = ""
homms = []

while True:
    line = file.readline()

    if "<w>" in line:
        currentWord = ""
    if "<c>" in line:
        currentWord = line.strip()
        currentWord = currentWord.strip("<c>")
        currentWord = currentWord.strip("</c>").lower()
    if "<d>" in line:
        espWord = line.strip()
        #removeMGen = "\{m\}"
        #remobeFGen = "\{f\}"
        espWord = espWord.strip("<d>")
        espWord = espWord.strip("</d>")
        #espWord = espWord.replace(removeFGen,"")
        #espWord = espWord.replace(removeMGen,"")
    if "<t>" in line:
        defWord = line.strip()
        defWord = defWord.strip("<t>")
        defWord = defWord.strip("</t>")
    if "</w>" in line:
        if currentWord not in enWords:
            enWords[currentWord] = [espWord, [defWord]]
        elif currentWord in enWords:
            enWords[currentWord][1].append(defWord)

    if not line:
        break


while True:
    oxline = oxford.readline()
    oxSplit = oxline.split(" ") 
    oxDef = ""
    for i in range(len(oxSplit)):
        if i == 0:
            oxSplit[0] = oxSplit[0].lower().strip("-")
        else:
            oxDef += oxSplit[i] + " "
    if oxSplit[0] in enWords:
        enWords[oxSplit[0]].append(oxDef)
        
        

    if not oxline:
        break

dictkeys = list(enWords.keys())

for i in range(len(dictkeys)):
    if dictkeys[i] == enWords[dictkeys[i]][0]:
        homms.append(dictkeys[i])  
        

playerHistory=[]


playerSearch = input("Search a word (/q to quit): ").lower()

while playerSearch != "/q":
    
    if playerSearch in enWords:
        print(enWords[playerSearch][0])
        if len(enWords[playerSearch]) >= 3:
            print(enWords[playerSearch][2])
        else:
            print(enWords[playerSearch][1])
        playerHistory.append(playerSearch)
        playerSearch = input("Search a word (/q to quit): ").lower()
        
    elif "/ih" in playerSearch:
        if len(playerSearch) == 3:
            print("Here are all the homms:")
            for i in range(len(homms)):
                print (homms[i])
        elif "/ih-" in playerSearch:
            splitSearch = playerSearch.split("-")
            for h in range(len(splitSearch[1])):
                for i in range(len(homms)):
                    alphaMatch = homms[i]
                    if splitSearch[1][h] == alphaMatch[0]:
                        print(alphaMatch)
                    
        playerHistory.append(playerSearch)
        playerSearch = input("Search a word (/q to quit): ").lower()

    elif playerSearch == "/history":
        for i in range(len(playerHistory)):
            print(playerHistory[i])
        playerHistory.append(playerSearch)
        playerSearch = input("Search a word (/q to quit): ").lower()

    elif playerSearch not in enWords:
        print("Not in the dictionary provided. Try again (/q to quit).")
        playerHistory.append(playerSearch)
        playerSearch = input("Search a word (/q to quit): ").lower()

    
if playerSearch == "/q":

    #print(enWords["abbey"])
    print("Goodbye.")