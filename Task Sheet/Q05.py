# Bubble sort
#
# Use a static list
# Use bubble sort to sort this list

#method1
li = [5,7,3,10,1,4]

def bubble_sort(li) :
    n = len(li) 
    for i in range(n - 1) : 
        for j in range(n - i - 1):
            if li[j] > li[j + 1] : 
                li[j] , li[j + 1] = li[j + 1], li[j]

bubble_sort(li)
print(li)

#method2
# li = [5,7,3,10,1,4]
li = [1,2,3,4,5]

def bubble_sort(li) :
    n = len(li) 
    for i in range(n - 1) :
        isSwap = False 
        for j in range(n - i - 1):
            if li[j] > li[j + 1] : 
                li[j] , li[j + 1] = li[j + 1], li[j]
                isSwap = True
            print("Hello")
        if not isSwap : 
            return
bubble_sort(li)
print(li)
