def occurences(it, lst):
    i = 0
    for el in lst:
        if el == it:
            yield i
        i += 1
    

lst = [1,2,5,8,6,2,5,9,1,8,8]

number = int(input("Entrer un entirer : "))

occrs = []
for i in occurences(number, lst):
    occrs.append(i)
            
print("Le nombre d'occurences de ", number, " dans la liste est : ", len(occrs))
print("Les indices des occurences sont : ", occrs)