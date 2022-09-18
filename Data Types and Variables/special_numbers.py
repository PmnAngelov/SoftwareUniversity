n = int(input())
sets = []
for a in range(1, n +1):
    a2 = a
    while a2 > 0:
        b = a2 % 10
        sets.append(b)
        a2 = a2 // 10

    if sum(sets) == 5 or sum(sets) == 7 or sum(sets) == 11:
        print(f"{a} -> True")
    else:
        print(f"{a} -> False")
    sets = []