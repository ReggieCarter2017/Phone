import Teacher as teach
import Searching as srch

def UserInterFace():
    print("1. Войти как учитель.\n2. Войти как ученик.\n3. Выйти из приложения.")
    userInput = int(input())
    while userInput != 3:
        if userInput == 1:
            n = int(input("1. Добавить ученика.\n2. Добавить предмет.\n3. Просмотреть учеников.\n4. Добавить оценку.\n5. Назад.\n6. Найти ученика.\n7. Выйти из приложения."))
            if n == 1:
                teach.addStudent()
            elif n == 2:
                teach.addItem()
            elif n == 3:
                teach.showStudents()
            elif n == 4:
                teach.addGrade()
            elif n == 5:
                UserInterFace()
            elif n == 6:
                srch.Searching()
            elif n == 7:
                break

        elif userInput == 2:
            s = int(input("1. Просмотреть учеников.\n2. Найти ученика.\n3. Назад.\n4. Выйти из приложения."))
            if s == 1:
                teach.showStudents()
            elif s == 2:
                srch.Searching()
            elif s == 3:
                UserInterFace()
            elif s == 4:
                break




