# Selection sort
#
# Use a static list
# Use selection sort to sort this list

li = [5,7,3,10,1,4]

def selection_sort(li) :
    n = len(li)
    for i in range(n - 1):
        smallestIndex = i
        for j in range(i + 1, n):
            if li[smallestIndex] > li[j]:
                smallestIndex = j
        li[smallestIndex], li[i] = li[i], li[smallestIndex]

selection_sort(li)
print(li)
