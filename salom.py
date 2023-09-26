def amallar():
    menu()

    tanlov = int(input("amalni tanlang = "))
    while tanlov != 6:
        if tanlov == 1:
            qoshish()

            menu()
            tanlov = int(input("amalni tanlang = "))
        elif tanlov == 2:
            print("Eslatma 6ta harfdan kam qatorlar ochirildi")
            ochirish()
            menu()
            tanlov = int(input("amalni tanlang = "))
        elif tanlov == 3:
            contactlarni_korish()
            menu()
            tanlov = int(input("amalni tanlang = "))
        elif tanlov == 4:
            qidirish()
            menu()
            tanlov = int(input("amalni tanlang = "))
        else:
            tanlov = int(input("Bunday amal turi yoq"))


def menu():
    print(
        """__MENU__
    qoshish = 1
    ochirish = 2
    qidirish=4
    contactlarni_korish = 3
"""
    )


def qoshish():
    fayl = open("C:/Users/user/Desktop/rrr.txt", "r")
    a = fayl.readlines()

    royhat = []
    for soz in a:
        royhat.append(soz.rstrip())
    royhat.insert(1, input("Ism kiriting = "))
    print(royhat)

    yozish = open("C:/Users/user/Desktop/rrr.txt", "w")

    for soz in royhat:
        yozish.write(soz + "\n")
    yozish.close()

    fayl = open("C:/Users/user/Desktop/rrr.txt", "r")
    a = fayl.readlines()

    royhat = []
    for soz in a:
        royhat.append(soz.rstrip())
    royhat.insert(3, input("Familiya kiriting = "))
    print(royhat)

    yozish = open("C:/Users/user/Desktop/rrr.txt", "w")

    for soz in royhat:
        yozish.write(soz + "\n")
    yozish.close()

    fayl = open("C:/Users/user/Desktop/rrr.txt", "r")
    a = fayl.readlines()

    royhat = []
    for soz in a:
        royhat.append(soz.rstrip())
    royhat.insert(5, input("Tel_raqam = "))
    print(royhat)

    yozish = open("C:/Users/user/Desktop/rrr.txt", "w")

    for soz in royhat:
        yozish.write(soz + "\n")
    yozish.close()

    fayl.close()


def ochirish():
    file = open("C:/Users/user/Desktop/rrr.txt", "r")
    content = ""
    while True:
        line = file.readline()
        if len(line.strip()) >= 6:
            content += line
        if not line:
            break
    file.close()
    file = open("C:/Users/user/Desktop/rrr.txt", "w")
    file.write(content)

    file.close()


def contactlarni_korish():
    fayl = open("C:/Users/user/Desktop/rrr.txt", "r")
    d = fayl.readlines()

    royhat = []
    for soz in d:
        royhat.append(soz.rstrip("\n"))
    royhat.insert(7, "contactlar korildi")
    print(royhat)
    fayl.close()


def qidirish():
    import io

    word = input("Qidiring = ")
    with io.open("C:/Users/user/Desktop/rrr.txt", encoding="utf-8") as file:
        for line in file:
            if word in line:
                print(line, end="")


amallar()
