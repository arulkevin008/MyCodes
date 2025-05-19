def sub(n1,n2):
    return n1-n2

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if a<b:
    print("A is lesser than B")
    a=int(input("(Re-enter) a="))

subtract=sub(a,b)
output=subtract*c
print(output)
