#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1

n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
        
    num = 1
    for k in range(i + 1):
        print(num, end=" ")
        num = num * (i - k) // (k + 1)
        
    print()
