import Teacher as teach

def Searching():
    n = input("Ключевое слово: ")
    for i in range(len(teach.studentsArray)):
        if n in teach.studentsArray[i]:
            print(teach.studentsArray[i])
