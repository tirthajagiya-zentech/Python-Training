#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    temp = i
    for k in range(1,2*i):
        # print(f"{temp} ",end="")
        print(temp,end="")
        if k<i:
            temp = temp + 1
        else:
            temp = temp - 1
    print()
