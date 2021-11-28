from random import randrange

with open("folder_test/text5.txt", "w") as f:
    for i in range(1, 100):
        num = randrange(1, 1000)
        f.write(str(num) + " ")
with open("folder_test/text5.txt", "r") as f:
    data = [int(i) for i in f.read().split()]
    print(sum(data))
