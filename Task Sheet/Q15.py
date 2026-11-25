# Find LCM and GCM of a number
a=12
b=18

if a>b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a

for i in range(minimum, 0, -1):
    if a%i==0 and b%i==0:
        print(i)
        break

a=11
b=12

if a>b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a

while True:
    if(maximum%a==0 and maximum%b==0):
        lcm = maximum
        print(lcm)
        break
    maximum += 1
