print("\t\t\tLinear Search")
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            index_array.append(i)

my_array=list(map(int,input("Enter the array values with seperated space:").split()))
target=int(input("Enter the search value:"))
index_array=[]

linear_search(my_array,target)

if index_array != []:
    print("Found at",len(index_array),"index",index_array)
else:
    print("Not found")
