n=int(input("Enter a no:"))
s=0
for i in range(1,n+1):
    s=s+(i**i/i)
print("Sum of series of",n,"is",s)
