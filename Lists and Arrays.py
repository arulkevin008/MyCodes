print("\t\t\tMin & Max Value in a List or Array")

try:
    my_array = list(map(int, input("\nEnter values separated by space: ").split()))
    
    min_value = my_array[0]
    max_value = my_array[0]

    for i in my_array:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i

    print("\nMin Value:", min_value)
    print("Max Value:", max_value)

except Exception as e:
    print("\nError:", e)
