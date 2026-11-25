# Find diterminent of 3x3 matrix

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a,b,c = mat[0]
d,e,f = mat[1]
g,h,i = mat[2]

det = a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)
print(det)
