# from random import randint
#
# def amallar():
#     menu()
#
#     tanlov = int(input('amalni tanlang = '))
#     while tanlov!= 6:
#         if tanlov == 1:
#             qoshish()
#
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 2:
#             ochirish()
#
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 3:
#             contactlarni_korish()
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         elif tanlov == 4:
#             tozalab_yozish()
#             menu()
#             tanlov = int(input('amalni tanlang = '))
#         else:
#             tanlov = int(input('Bunday amal turi yoq'))
#
#
# def menu():
#     print("""__MENU__
#     qoshish = 1
#     ochirish = 2
#     tozalab_yozish=4
#     contactlarni_korish = 3
# """)
# def qoshish():
#     fayl = open('C:/Users/user/Desktop/rrr.txt','a')
#     fayl.write(input('Ism kiriting = '+'\n'))
#     fayl.write(input('Fam kiriting = ' + '\n'))
#     fayl.write(input('Contact kiriting = ' + '\n'))
#
#     fayl.close()
# def ochirish():
#     fayl = open('C:/Users/user/Desktop/rrr.txt', 'r')
#     d = fayl.readlines()
#     print(d)
#     royhat = []
#
#     for soz in d:
#         royhat.append(soz.rstrip('\n'))
#     royhat.insert(111111, "salom")
#     print(royhat)
#     fayl.close()
# def contactlarni_korish():
#     fayl = open('C:/Users/user/Desktop/rrr.txt', 'r')
#     d = fayl.readlines()
#
#     royhat = []
#     for soz in d:
#         royhat.append(soz.rstrip('\n'))
#     royhat.insert(11111111, "salom")
#     print(royhat)
#     fayl.close()
# def tozalab_yozish():
#     fayl = open('C:/Users/user/Desktop/rrr.txt', 'w')
#     fayl.write(input('kiriting = '))
#     fayl.close()
#
#
# amallar()


# from __future__ import print_function
# import io
#
# word = input('Qidiring = ')
# with io.open('C:/Users/user/Desktop/rrr.txt', encoding='utf-8') as file:
#     for line in file:
#         if word in line:
#             print(line, end='')
#
# import codecs
#
# with codecs.open('rrr.txt','r',encoding='utf-8-sig') as f1:
#     for line in f1:
#         print(line.strip())
#         stringGET = line.strip()
#         if stringGET == '""':
#             continue
#
#     with codecs.open('FULL LIST.txt', 'a', encoding='utf-8-sig') as f2:
#         f2.write(stringGET)
#         f2.write('\n')
#         f2.close
# чтение и формирование нового содержимого файла
file = open("C:/Users/user/Desktop/rrr.txt", "r")
content = ""
while True:
    line = file.readline()
    if len(line.strip()) >= 6:
        content += line
    if not line:
        break
file.close()
# запись нового содержимого в файл
file = open("C:/Users/user/Desktop/rrr.txt", "w")
file.write(content)
file.close()





    #/////////////////////////////////oqish uchun
# fayl = open('C:/Users/user/Desktop/rrr.txt','r')
# d = fayl.readlines()
# print(d)
#
# fayl.close()
#//////////////////oqish2
# fayl = open('C:/Users/user/Desktop/rrr.txt','r')
# d = fayl.readlines()
# print(d)
# royhat = []
#
#
# for soz in d:
#     royhat.append(soz.rstrip('\n'))
# royhat.insert(2,"salom")
# print(royhat)
# fayl.close()


