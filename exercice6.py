liste = [-1, 0, 2, 3, 3, 2, 0, -1]

# index = True
# while index:
#     x = input("Entrer un entier :  (entrer 'x' pour quiter) ")
#     if x == 'x':
#         index = False
#         continue

#     x = int(x)

#     liste.append(x)


numberToRemove = int(input("Entrer le nombre a eliminer : "))
index = True

while index:
    if numberToRemove in liste:
        liste.remove(numberToRemove)
    else:
        index = False


print(liste)
