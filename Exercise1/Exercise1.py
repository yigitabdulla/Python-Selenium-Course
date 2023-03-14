list = []

def add():
    student = input("Aralarinda boşluk olacak şekilde ad-soyad giriniz:")
    list.append(student)
    print(list)

def multipleAdd():
    a = int(input("Kac ogrenci eklemek istiyorsunuz:"))
    for i in range(a):
        b = input("Ad-Soyad arasinda boşluk olacak şekilde öğrenci adini giriniz:")
        list.append(b)
    print(list)

def delete():
    student = input("Silmek istediginiz ogrencinin ad-soyadini aralarinda boşluk olacak sekilde giriniz:")
    for i in range(len(list)):
        if(list[i] == student):
            list.pop(i)
    print(list)

def multipleDelete():
    a = int(input("Kaç öğrenci silmek istiyorsunuz:"))
    j = 1
    while j <= a:
        student = input("Ad-Soyad arasinda boşluk olacak şekilde öğrenci adini giriniz:")
        list.remove(student)
        j += 1
    print(list)

def printList():
    for i in range(len(list)):
        print(list[i])

def searchNumber():
    student = input("Aralarinda boşluk olacak şekilde ad-soyad giriniz:")
    for i in range(len(list)):
        if(list[i] == student):
            print("Student number of " +student+" "+ str(i))




