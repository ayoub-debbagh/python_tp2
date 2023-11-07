import random

randInt = random.randint(1, 100)

nbrTries = 0

while nbrTries < 7 :
    userInput =  int(input("Entrer un entier : "))
    nbrTries += 1
    if userInput > randInt:
        print("Tres grand")
        continue
    elif userInput < randInt:
        print("Tres petit")
        continue
    else:
        print("Bravo ", userInput, " est le nombre que j'ai choisit")
        print("Vous l'avez devine en ", nbrTries, " essais")
        break

if nbrTries == 7:
    print("J'ai gagne, je suis le meilleur, Le nombre que j'ai devine est ", randInt)
    print("Au revoir!")



