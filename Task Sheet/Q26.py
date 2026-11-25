# 1
# 2 3
# 4 5 6
# 7 8 9 10

n=5
num = 1
for i in range(n+1):
    for j in range(i):
        print(num," ",end="")
        num = num + 1
    print()
