listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input ('Digite um valor para a posição:')))
    if c == 0: mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(listanum)
print(f'o maior valor foi o {mai} nas posições ', end='')

for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i} ... ', end='')
print()
