# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
n=len(matrix)
m=len(matrix[0])
print(n,m)
left=0
right=n-1
top=0
bottom=m-1

li = []

while left<=right and top<=bottom:
    for i in range(left,right+1):
        li.append(matrix[top][i])
    top=top+1

    for i in range(top,bottom+1):
        li.append(matrix[i][right])
    right=right-1

    if top<=bottom:
        for i in range(right, left-1, -1):
            li.append(matrix[bottom][i])
        bottom=bottom-1

    if left<=right:
        for i in range(bottom,top-1,-1):
            li.append(matrix[i][left])
    left=left+1

print(li)
