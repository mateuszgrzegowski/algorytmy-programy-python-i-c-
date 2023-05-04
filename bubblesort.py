tab = [8, 2, 1, 9, 5]
tab = [6, 5, 4, 3, 2, 1]
print(tab)

i = 0
zamieniono = True
while i < len(tab) - 1 and zamieniono:
    j = 0
    zamieniono = False
    while j < len(tab) - 1 - i:
        if tab[j] > tab[j + 1]:
            tab[j], tab[j + 1] = tab[j + 1], tab[j]
            zamieniono = True
        j += 1
    i += 1
    print(tab)
