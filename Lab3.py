# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
# def functie(a, b):
#     c = []
#     a = set(a)
#     b = set(b)
#     c.append(a.intersection(b))
#     c.append(a.union(b))
#     c.append(a.difference(b))
#     c.append(b.difference(a))
#     return c

# def fct(a, b):
#     a = set(a)
#     b = set(b)
#     dictionar = dict(Intersectie = a.intersection(b), Reuniune = a.union(b), Diferenta_ab = a.difference(b), Diferenta_ba = b.difference(a))    
#     return dictionar

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [6, 7, 8, 9, 10]
# print(functie(a, b))
# print(fct(a, b))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
# def functie(a):
#     dictionar = dict()   
#     for j in range(0, len(a)):
#         k = 0
#         for i in range(0, len(a)):
#             if a[j] == a[i]:
#                 k += 1
#         print(k)
#         dictionar[a[j]] = k  
#     print(dictionar)    
       

# a = "ana are mere"  
# functie(a)       


# 3.
# def functie(dictionar):
#     max = 0
#     for i in dictionar.items():
#         if i[1] > max:
#             max = i[1]
#             c = i[0]  
#     return max, c     

# max = 0    
# x  = {
#     "Dacia" : 120,
#     "BMW" : 170,
#     "Audi": 160
# }     
# for i in x.keys():
#     if x[i] > max:
#         max = x[i]
#         c = i 
# print((max, c))

# print(functie(x))

















