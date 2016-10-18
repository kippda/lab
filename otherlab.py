def createMenu(listOfChoices):
    tmpStr = ""
    ct = 1
    for choice in listOfChoices:
        tmpStr += str(ct) + ") " + choice + "\n"
        ct += 1
    return(tmpStr)

def validChoice(lst,str):
    """
    Returns a choice that is a digit between 1 and
    the length of the lst
    """
    ch = input("Please enter your choice: ")
    while ch.isdigit() is False or int(ch) < 1 or int(ch) > len(lst):
        print(str)
        ch = input("Please enter a valid choice: ")
    return(int(ch))

def mainMenu():
    print(mainStr)
    choice = validChoice(listOfChoices, mainStr)
    if choice == 1:
        print("Not implemented") #######
        print()
        mainMenu()
    elif choice == 2:
        printDict(studentDict)
        print()
        mainMenu()
    elif choice == 3:
        printNames(studentDict)
        print()
        mainMenu()
    elif choice == 4:
        print("Not implemented") #######
        print()
        mainMenu()
    elif choice == 5:
        printClasses(studentDict)
        print()
        mainMenu()
    elif choice == 6:
        print("Not implemented") #######
        print()
        mainMenu()   
    elif choice == 7:
        classesForStudent(studentDict)
        print()
        mainMenu()   

#def addStudent()

def printDict(tmpDict):
    for item in tmpDict:
        print(item, tmpDict[item])

def printNames(tmpDict):
    tmpList = []
    for item in tmpDict:
        tmpList.append(item)
    tmpList.sort()
    for name in tmpList:
        print(name)

#def delStudent()

def printClasses(tmpDict):
    tmpList = []
    for student in tmpDict:
        for elem in tmpDict[student]:
            if elem not in tmpList:
                tmpList.append(elem)
    tmpList.sort()
    print(tmpList)

#def studentsInClass()

def classesForStudent(tmpDict):
    tmpList = [student for student in tmpDict]
    print(tmpList)
    printNames(studentDict)
    name = input("Choose a student: ")
    while name not in tmpList:
        name = input("Choose a student: ")
    print(studentDict[name])

studentDict = {"Joe":["Bio","Music"], "Sally":["Chem","Bio"]}

listOfChoices = ["Add a student's info", "Print", "Print names",
                 "Delete a student's info", "Print list of classes",
                 "Names of all students in a particular class",
                 "Classes for a particular student", "Check for student",
                 "Quit"]

mainStr = createMenu(listOfChoices)

mainMenu()
