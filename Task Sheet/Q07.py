# Binary search
#
# Use a static list
# Use Binary search to find element asked by user
# Use one of the sorting algorithm that you have developed to sort list here

# li = [5,7,3,10,1,4]

element = 30

# for i in range(len(li)):
#     if li[i] == element:
#         print(i)
#         break
# else :
#     print("Not Found")

li2 = [1,2,3,4,5,6]

left = 0
right = len(li2) - 1

while left < right : 
    mid = (left + right) // 2
    print("Hello")
    if li2[mid] == element : 
        print(mid)
        break
    elif li2[mid] < element : 
        left = mid + 1
    else : 
        right = mid
else : 
    print("Not found")
