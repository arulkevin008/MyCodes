print("\t\t\tBubble Sort")
array=list(map(int,input("Enter the values with seperated spaces:").split()))
print("Before Sorting:",array)
n=len(array)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
            swapped = True
    if not swapped:
        break

print("After Sorting:",array)
