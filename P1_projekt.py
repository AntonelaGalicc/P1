import os
from random import randrange

# Varijable
ukupanBrojStudenata = randrange(100, 1000)
brojStudenataFPMOZ = int(ukupanBrojStudenata * 0.45)
brojStudenataFF = int(ukupanBrojStudenata * 0.25)
brojStudenataFSRE = int(ukupanBrojStudenata * 0.3) + 1
izbor = 100
# Datoteka za upisivanje studenata
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
studentDataFile = (str(desktop) + '\Studenti.txt', "w")


# Funkcije
def unos_studenta():
    studentDataFile = open(str(desktop) + '\Studenti.txt', "a")
    print('Ime studenta: ')
    ime = str(input())
    print('Prezime: ')
    prezime = str(input())
    print('Mjesto stanovanja: ')
    mjesto_stanovanja = str(input())
    print('Broj indeksa: ')
    broj_indeksa = int(input())
    print('Fakultet: ')
    fakultet = str(input())
    print('Studij: ')
    studij = str(input())
    print('Prosjek Ocjena: ')
    prosjek_ocjena = float(input())
    studentInfo = (str(ime) + ' ' + str(prezime) + ' ' + str(mjesto_stanovanja) + ' ' + str(broj_indeksa) + ' ' + str(
        fakultet) + ' ' + str(studij) + ' ' + str(prosjek_ocjena))
    studentDataFile.write(str(studentInfo) + '\n')
    print(studentInfo)
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def sort_po_prezimenu():
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    lines.sort(key=lambda line: str(line.split()[1]))
    for line in lines:
        print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


# Print izbornika
def sort_po_imenu():
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    lines.sort(key=lambda line: str(line.split()[0]))
    for line in lines:
        print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def trazenje_po_mjestu(mjesto):
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    for line in lines:
        if mjesto in line:
            print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def trazenje_po_fakultetu(fakultet):
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    for line in lines:
        if fakultet in line:
            print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def trazenje_po_studiju(studij):
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    for line in lines:
        if studij in line:
            print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def ispis_sa_vecom_ocjenom(ocjena):
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    for line in lines:
        if(float(ocjena) < float(line.split()[6])):
            print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def trazenje_studenta(argument):
    studentDataFile = open(str(desktop) + '\Studenti.txt', "r")
    lines = studentDataFile.read().splitlines()
    for line in lines:
        if is_number(argument):
            if float(argument) == float(line.split()[3]):
                print('\033[0m' + line + '\n')
        else:
            if str(argument) == str(line.split()[0] + ' ' + line.split()[1]):
                print('\033[0m' + line + '\n')
    studentDataFile.close()
    print('Enter za nastavljanje: ')
    print(input())


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


while int(izbor) != 0:
    print('\033[1m' + 'Ukupan broj studenata: ' + '\033[0m' + str(ukupanBrojStudenata) + '\n')
    print('FPMOZ: ' + str(brojStudenataFPMOZ) + '\n')
    print('FF: ' + str(brojStudenataFF) + '\n')
    print('FSRE: ' + str(brojStudenataFSRE) + '\n')
    print('\033[1m' + 'Izaberi jednu od opcija:' + '\n')
    print('\033[0m' + 'Unos Studenta: ' + '\033[1m' + '1' + '\n')
    print('\033[0m' + 'Ispis svih studenata sortirano abecedno po prezimenu: ' + '\033[1m' + '2' + '\n')
    print('\033[0m' + 'Ispis svih studenata sortirano abecedno po imenu: ' + '\033[1m' + '3' + '\n')
    print('\033[0m' + 'Ispis svih studenata po nekom mjestu stanovanja: ' + '\033[1m' + '4' + '\n')
    print('\033[0m' + 'Ispis svih studenata pojedinog fakulteta: ' + '\033[1m' + '5' + '\n')
    print('\033[0m' + 'Ispis svih studenata pojedinog studija: ' + '\033[1m' + '6' + '\n')
    print('\033[0m' + 'Ispis svih studenata sa prosjecnom ocjenom vecom od zadane vrijednosti: ' + '\033[1m' + '7' + '\n')
    print('\033[0m' + 'Pronadi studenta po indeksu ili imenu i prezimenu: ' + '\033[1m' + '8')
    print('\033[0m' + '(Provjera da li postoji konkretni student u datoteci)' + '\n')
    print('\033[0m' + 'Unos novog studenta: ' + '\033[1m' + '9' + '\n')
    print('\033[0m' + 'Izlaz: ' + '\033[1m' + '0' + '\n')
    print('Izbor: ')
    izbor = input()
    if int(izbor) == 1:
        unos_studenta()
    elif int(izbor) == 2:
        sort_po_prezimenu()
    elif int(izbor) == 3:
        sort_po_imenu()
    elif int(izbor) == 4:
        print('Unesi mjesto: ')
        trazenje_po_mjestu(input())
    elif int(izbor) == 5:
        print('Unesi fakultet: ')
        trazenje_po_fakultetu(input())
    elif int(izbor) == 6:
        print('Unesi studij: ')
        trazenje_po_studiju(input())
    elif int(izbor) == 7:
        print('Unesi ocjenu: ')
        ispis_sa_vecom_ocjenom(input())
    elif int(izbor) == 8:
        print('Unesi broj indeksa ili ime i prezime studenta: ')
        trazenje_studenta(input())
    elif int(izbor) == 9:
        unos_studenta()
