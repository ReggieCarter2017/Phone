import Import as imp
import Logger as log

def UserInterface():
        choice = 0
        while choice != 3:
            print("1. Показать список контактов.\n2. Добавить контакт в телефонный справочник.\n3. Поиск по ключевому слову.\n4. Выйти из приложения.")
            choice = int(input())
            if choice == 4:
                data = imp.ImportUser()
                log.UserInputLogger(data)
                log.UserInputLogger2(data)
            elif choice == 1:
                log.printLog()
            elif choice == 3:
                print(', '.join(log.SearchingInLog()))






