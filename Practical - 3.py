a=[i for i in range(1,11)]
print("Values in the list:",a)
for i in a:
    if i%2==1:
        a.remove(i)
print ("After removal of odd nos from the list:",a)
