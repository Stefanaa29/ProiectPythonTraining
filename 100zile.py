# 1 Zi 
# print("hello!")
# nume_oras = input("Care este numele orasului in care te-ai nascut?\n")
# nume_animal = input("Care este numele primului tau animal de companie?\n")
# nume = nume_oras + " " + nume_animal
# print(nume)

# 2 Ziua
# 1.a = int(input("Scrie numarul: \n"))
# b = a % 10 + a // 10
# print(str(a % 10) + "+" + str(a // 10) + "=" + str(b))

# 2.Greutate = float(input("Greutatea dumneavoastra este: "))
# Inaltimea = float(input("Inaltimea dumneavoastra este:"))
# IMC = int(Greutate / Inaltimea ** 2)
# print(IMC)


# 3.x = int(input("Varsta mea este: \n"))
# print(f"Am varsta de {x} ani")
# zile = x * 365
# saptamani = x * 52
# luni = x * 12
# zile1 = 90 * 365- zile
# saptamani1 = 90 * 52 - saptamani
# luni1= 90 * 12 - luni
# print(f"Mai aveti {zile1} zile, {saptamani1} saptamani si {luni1} luni.")

# 4.print("Bine ati venit la calculatorul de bacsisuri!")
# nota = float(input("Nota totala a fost de: "))
# bacsis = int(input("Cat bacsis ati vrea sa dati?10, 12 sau 15%\n"))
# cati_oameni = int(input("Cati oameni impart nota?\n"))
# fiecare_om = round(((nota + (bacsis / 100) * nota) / cati_oameni),2)
# print(f"Fiecare om ar trebui sa plateasca: {fiecare_om} lei")


# 5. inaltime = int(input("Inaltimea clientului este de: "))
# varsta = int(input("Varsta clientului este de: "))

# inaltimea_min = 120

# if inaltime >= inaltimea_min:
#     if varsta < 18:
#         print("Pretul biletului este 5 lei")
#     else:
#         print("Pretul biletului este 10 lei") 
# else:
#      print("Nu poti intra! Nu ai inaltimea minima!")


# 6.greutate = float(input("Greutatea dumneavoastra este:"))
# inaltime = float(input("Inaltimea dumneavoastra este:"))
# BMI = round(greutate / inaltime**2 * 10000)
# print(BMI)
# if BMI < 18.5:
#     print("Sunteti subponderal")
# elif BMI >= 18.5 and BMI < 25:
#     print("Aveti o greutate normala.")  
# elif BMI >= 25 and BMI < 30:
#     print("Sunteti supraponderal")
# elif BMI >= 30 and BMI < 35:
#     print("Sunteti obez")
# else:
#     print("Sunteti obez clinic")

# an = int(input("Tastati un an oarecare:"))
# if an % 4 == 0:
#     if an % 100 != 0:
#         print(f"Anul {an} este un an bisect")
#     elif an % 400 != 0:
#         print(f"Anul {an} este un an obisnuit")
#     else:
#         print(f"Anul {an} este an bisect") 
# else:
#     print(f"Anul {an} este un an obisnuit")

# ///////////////////////////////////////////////////////
# -------------Piatra/Hartie/Foarfeca---------------------

# import random
# piatra = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''


# hartie = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)

# '''


# foarfeca='''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# print('Hai sa ne jucam!')
# print('Alege: ')
# print('1-Foarfeca')
# print('2-Hartie')
# print('3-Piatra')
# alegere = int(input())
# while alegere not in [1, 2, 3]:
#     print("Alege dintre 1,2 sau 3!")
#     alegere = int(input("Alege iar:"))
# if alegere == 1:
#     print(foarfeca)
# elif alegere == 2:
#     print(hartie)
# elif alegere ==3:
#     print(piatra) 

# print("Este randul calculatorului!")
# print("Calculatorul a ales:")
# lista = [1, 2, 3]
# alegere_calculator = random.choice(lista)
# print(alegere_calculator)
# if alegere_calculator == 1:
#         print(foarfeca)
# elif alegere_calculator == 2:
#         print(hartie)
# else:
#     print(piatra)

# if alegere == 1:
#     if alegere_calculator == 1:
#         print("Remiza!")
#     elif alegere_calculator == 2:
#         print("Ai casigat!")
#     else:
#         print("Ai pierdut!")  

# if alegere == 2:
#     if alegere_calculator == 1:
#         print("Ai pierdut!")
#     elif alegere_calculator == 2:
#         print("Remiza")
#     else:
#         print("Ai castigat!")           

# if alegere == 3:
#     if alegere_calculator == 1:
#         print("Ai casigat!")
#     elif alegere_calculator == 2:
#         print("Remiza")
#     else:
#         print("ai pierdut!")         
  

#  Ziua 5
# inaltime_studenti = [180, 124, 165, 173, 189, 169, 146]
# suma = 0
# for i in inaltime_studenti:
#     suma += i
# media = suma / 7 
# print("Media este:" + str(round(media, 2)))   


# inaltime_studenti = []
# n = input().split()
# for i in n:
#     inaltime_studenti.append(int(i))
# while(len(inaltime_studenti) < n):
#     a = int(input())
#     inaltime_studenti.append(a)
    

# test development branch
# for i in range(0,n):
#     a = int(input())
#     inaltime_studenti.append(a)
    
# print(inaltime_studenti)


# Ex:
# scoruri = []
# min = 100
# n = int(input("Introduceti numarul de elemente din lista: "))
# for i in range(0, n):
#     a = int(input())
#     scoruri.append(a)
# print(scoruri)    
# for i in scoruri:
#     if i < min:
#         min = i   
# print(min)    

# suma = 0
# for i in range(2,100+1,2):
#     suma += i
# print(f"Suma numerelor pare este:{suma}")   


# FizzBuzz

# for numar in range(1,100+1):
#     if numar % 15 == 0:
#         print("FizzBuzz")
#     elif numar % 3 == 0:
#         print("Fizz")
#     elif numar % 5 == 0:
#         print("Buzz")
#     else:
#         print(numar)            

# import math
# def numar_cutii(height, width, cover):
#     numar = (inaltime * latimea) / c
#     print(math.ceil(numar))
  
# inaltime = int(input("Inaltimea peretelui: "))
# latimea = int(input("Latimea peretelui: "))
# c = 5
# numar_cutii(height=inaltime, width = latimea, cover= c)


# n = int(input("Verifica numarul:"))
# def functie(numar):
#     k = 0
#     for i in range(2, numar//2):
#         if numar % i == 0:
#             k += 1
#     if k > 0: 
#         print(f"{numar} nu este numar prim") 
#     else:
#         print(f"{numar} este numar prim")      

# functie(n)

