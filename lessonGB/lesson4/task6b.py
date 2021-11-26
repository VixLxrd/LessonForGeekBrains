from itertools import cycle

rep = 0

for i in cycle(range(3)):
    if rep > 10:
        break
    print(i)
    rep += 1
