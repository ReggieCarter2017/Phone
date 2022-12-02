studentsArray = []
items = {}
res = {}


def showStudents():
    count = 0
    for i in studentsArray:
        count+=1
        print(f"{count}. {i}")
    print("\n")


def addItem():
    items[input("Введите новый предмет: ")] = ""


def usingItems():
    res = dict(zip(range(1, len(items)+1), items))
    return res

def addGrade():
    for i in range(len(studentsArray)):
        print(i+1, ". " + str(studentsArray[i]))
    userInput = int(input("Выберите ученика: "))

    for key, value in usingItems().items():
        print(str(key) + ". ", value)
    key = int(input("Выберите предмет: "))
    grade = input("Введите оценку: ")
    studentsArray[userInput - 1] = str(studentsArray[userInput - 1]) + ", " + usingItems()[key] + ": " + grade


def addStudent():
    global studentsArray
    last_name = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    studentClass = input("Введите класс ученика: ")
    string = last_name + " " + name + ", " + studentClass
    studentsArray.append(string)
    return studentsArray

