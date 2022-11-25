def ImportUser():
    print('Для того, чтобы добавить новый контакт в телефонный справочник введите фамилию, имя, телефон и описание через запятую: ')
    UserInput = input().split(", ")

    return UserInput
