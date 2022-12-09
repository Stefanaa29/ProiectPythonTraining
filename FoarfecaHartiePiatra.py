# ///////////////////////////////////////////////////////1

# -------------Piatra/Hartie/Foarfeca---------------------

import random
piatra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


hartie = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''


foarfeca='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Hai sa ne jucam!')
print('Alege: ')
print('1-Foarfeca')
print('2-Hartie')
print('3-Piatra')
alegere = int(input())
while alegere not in [1, 2, 3]:
    print("Alege dintre 1,2 sau 3!")
    alegere = int(input("Alege iar:"))
if alegere == 1:
    print(foarfeca)
elif alegere == 2:
    print(hartie)
elif alegere ==3:
    print(piatra) 

print("Este randul calculatorului!")
print("Calculatorul a ales:")
lista = [1, 2, 3]
alegere_calculator = random.choice(lista)
print(alegere_calculator)
if alegere_calculator == 1:
        print(foarfeca)
elif alegere_calculator == 2:
        print(hartie)
else:
    print(piatra)

if alegere == 1:
    if alegere_calculator == 1:
        print("Remiza!")
    elif alegere_calculator == 2:
        print("Ai casigat!")
    else:
        print("Ai pierdut!")  

if alegere == 2:
    if alegere_calculator == 1:
        print("Ai pierdut!")
    elif alegere_calculator == 2:
        print("Remiza")
    else:
        print("Ai castigat!")           

if alegere == 3:
    if alegere_calculator == 1:
        print("Ai casigat!")
    elif alegere_calculator == 2:
        print("Remiza")
    else:
        print("ai pierdut!")         
  