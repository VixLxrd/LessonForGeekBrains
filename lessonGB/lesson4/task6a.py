from itertools import count, cycle

first, last = map(int, input().split())
for i in count(first):
    if i > last:
        break
    else:
        print(i)