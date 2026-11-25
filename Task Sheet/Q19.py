# A
# B B
# C C C
# D D D D
# E E E E E

for i in range(5 + 1):
    ch = "A"
    for j in range(i):
        print(chr(64 + i),end=" ")
    print()
