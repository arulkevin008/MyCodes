try:
    a=int(input("Enter no:"))
    b=input("Enter string:")
    c=a*b
    print(a*b,'\n')
except Exception as e:
    print("Error:",e)
finally:
    print("Done")
