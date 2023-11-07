

def placementIndex(sortedListe, item):
    for el in sortedListe:
        if el >= item:
            return sortedListe.index(el) 
        




liste = [1,2,3,6,7,6]


# index = True
# while index:
#     x = input("Entrer un entier :  (entrer 'x' pour quiter) ")
#     if x == 'x':
#         index = False
#         continue

#     x = int(x)

#     liste.append(x)



liste.sort()


numberToInsert = int(input("Entrer le nombre a inserer : "))
placeIndex = placementIndex(liste, numberToInsert)
liste.insert(placeIndex, numberToInsert)

print(liste)


