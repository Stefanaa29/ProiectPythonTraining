
# 1.def cmmdc(a,b):
#     while b!=0:
#         r = a%b
#         a = b
#         b = r
#     return a
# n = int(input("dati numarul de numere: "))
# x = []
# for i in range(0, n):
#     x.append(int(input("dati un nr:")))

# a = x[0]
# i = 1
# while i<n:
#     b = x[i]
#     a = cmmdc(a, b)
#     i += 1

# print(a)

# a= x[0]
# for i in range(1,n):
#      b = x[i]
#      a = cmmdc(a, b)

# print(a)

# 2.x = 0
# s = "Ana are mere"
# for i in range(0, len(s)):
#     if s[i] in "aeiouAEIOU":
#         x = x + 1
# print(x)

# 3.x= 0
# s = "si"
# v = "Va merge si Mihai la mare daca si Andrei va merge"
# for i in range(0, len(v)):
#     if v[i:i+len(s)] == s:
#         x= x + 1

# print(v.count(s))
# print(v.startswith("Va"))
# print(x)

# def change_case(s):
#     r = [s[0].lower()]
#     for c in s[1:]:
#         if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#             r.append('_')
#             r.append(c.lower())
#         else:
#             r.append(c)

#     return ''.join(r)

# s = "AnaAreMereRosii"
# print(change_case(s))


# s = "AnaAreMereRosii"
# rez = "ana_are_mere_rosii"
# i = 0
# rez = ""
# for j in range(0, len(s)):
#     if s[j].isupper() and j == 0:
#         rez = s[j].lower()
#     elif s[j].isupper():
#         rez = rez + "_" + s[j].lower()
#     else:
#         rez = rez + s[j]

# print(rez)

# def CreateDivizibleCheckFunction(n):

#     return lambda x: x%n==0

# fnDiv2 = CreateDivizibleCheckFunction (2)
# fnDiv7 = CreateDivizibleCheckFunction (7)
# x = 14
# print ( x, fnDiv2(x), fnDiv7(x) )

# l = [2, 3, 5, 9, 6]
# s = 0
# p = 1
# for i in range(0,5):
#     s = s + l[i]
#     p = p * l[i]
# print(s, p)


# print(list(enumerate(["Dragos","Mihai","Nicu","Vlad"])))

# x = []
# for i in range(1,100):
#     if i % 23 == 0:
#         x.append(i)
# print(x)

# x = [i for i in range(1,10)]
# print(x)

# x = [1,2,3,4,5]
# y = list(map(lambda e: e + 1, filter(lambda element: element%2==1,x)))
# print(y)

# ///////////////////////////////////////////////
# def fct(note,indici,start):
#     i = 0
#     new_list=[]
#     l = 2
#     while i < len(indici):
#         if len(note) <= l:
#             l =  l - len(note)
#         new_list.append(note[l])
#         l = l + indici[i]
#         print(l)
#         i=i+1
#     if len(note) <= l:
#         l =  l - len(note)
#     new_list.append(note[l])
#     return new_list

# print(fct(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# ////////////////////////////////////////////////////
# Se da o lista de numere. Sa se afiseze o lista noua cu patratele numerelor din prima lista.

# lista = [1, 2, 3, 4, 5]
# i = 0
# new_list = []
# for i in lista:
#     new_list.append(i * i)
# print(new_list)

# Se da o lista de nr. Sa se afis o lista noua cu patratele nr plus nr.
# lista = [1, 2, 3, 4, 5]
# i = 0
# new_list = []
# add = 1
# for i in range(0, 5):
#     new_list.append(lista[i] * lista[i]+lista[i])
#     add = add+1
# print(new_list)

# /////////////////////////////////////////////////////////////////////
# Se da un dictonar si o lista cu key din dictionar. Stergeti lista din dictionar.


# dict={
#     "name":"Adi",
#     "age":16,
#     "salary":21000,
#     "city":"Mumbai"
# }

# keys=["name","salary"]

# for i in keys:
#     del dict[i]
# print(dict)

# /////////////////////////////////////////////
# Se da o lista de cuvinte. Afiseaza cuvantul cel mai lung si lungimea lui.


# list = ["magazin", "casa", "masa", "ceas"]
# lungime = 0
# cuvant = 0
# for i in list:
#     if (len(i) > lungime):
#         lungime = len(i)
#         cuvant = i
# print("Cuvantul cel mai lung este: ", cuvant)
# print("Lungimea lui este: ", lungime)


# Numarati cate litere mici si cate litere mari sunt in sir si cate cuvinte sunt.

# sir = "AnA Are MeRe"
# literemici = 0
# literemari = 0
# cuv = 1
# for i in sir:
#     if i.isupper():
#         literemari += 1
#     elif i.islower():
#         literemici += 1
#     elif i == " ":
#         cuv += 1
# print(literemici, literemari, cuv)        



num1 = 38
if(num1>12):
    print("Num1 is good")
elif(num1>35):
    print("Num2 is not gooooo....")
else:
    print("Num2 is great")