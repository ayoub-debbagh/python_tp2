
print("1 : euro en mad", "2 : mad en euro", sep="\n")
conversion = int(input("Quel operation voullez vous effectuer?"))
value = float(input("Entrer le montant : "))

match conversion:
    case 1:
        print(f"{value} euro <=> {value * 10.87}  Dh")
    case 2:
        print(f"{value} Dh <=> {value * 10.87}  Euro")
    case -1:
        index = False
    case _:
        print("Choisir l'un des deux options")


