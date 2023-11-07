L = [1, -30, 0, -2, 500, 4, 2, 100]

M = []
positifItems = []


for el in L:
    if el < 0:
        M.append(el)
    else:
        positifItems.append(el)

M.extend(positifItems)

print(M)




