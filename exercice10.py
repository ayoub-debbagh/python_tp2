
L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]
L1 = list(dict.fromkeys(L1))
L2 = list(dict.fromkeys(L2))
L3 = []

for el1 in L1:
    for el2 in L2:
        if el1 == el2 and el1 not in L3:
            L3.append(el1)

print(L3)