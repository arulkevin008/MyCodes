    #Average of a List
while True:
    List=[2,4,6,78]
    list_avg=[]
    for i in List:
        i+=i
    list_avg=[i/len(List)]
    print(list_avg)

    #Check if the number exist in list
    ##List=[1,2,4,56,6,7]
    ##n=int(input("Enter the no to check:"))
    ##for i in List:
    ##    if(i==n):
    ##        print(n,"exists!")

    #Count elements less than 10
    My_List=[1,2,3,5,66,7,8,45,9,67]
    count=0
    for i in My_List:
        if(i<10):
            count+=1
    print(count)

    #Count elements to their index
    My_List=[0,1,2,3,4,5,6,8,9]
    count = 0
    i = 0
    while i < len(My_List):
        if My_List[i] == i:
            count += 1
        i += 1
    print("Count of elements equal to their index:", count)

    #Count number of times
    ##MyList=[2,3,4,5,2,5,7,9,4]
    ##num=int(input("Enter the number to count:"))
    ##num_count=0
    ##for i in MyList:
    ##    if(num==i):
    ##            num_count+=1
    ##print("The no of times are:",num_count)

    #Count +ve and -ve num
    MyList=[-1,-4,-6,2,5,8]
    positive=0
    negative=0
    for i in MyList:
        if(i<0):
            negative+=1
        elif(i>=0):
            positive+=1
    print("Positive numbers:",positive)
    print("Negative numbers:",negative)

    List=[]
    for i in range(1,11):
        List.append(i)
    print(List)

    #Create list of numbers divisible by 5 and 7
    List=[]
    for i in range(1,101):
        if(i%5==0):
            List.append(i)
        if(i%7==0):
            List.append(i)
    print(List)

    #Duplicate elements
    List=[2,2,4,6,5]
    dups = []
    for i in range(len(List)):
        for j in range(i+1, len(List)):
            if List[i] == List[j] and List[i] not in dups:
                dups.append(List[i])
    print(dups)

    #Filter alphabet char
    Mixed_List=["dfd",12,34,"dsafsf"]
    Str_list=[]
    for i in Mixed_List:
        if(type(i) is str):
            Str_list.append(i)
    print(Str_list)

    #Less than 10
    List=[2,4,5,23,56,67,7]
    list_10=[]
    for i in List:
        if(i<10):
            list_10.append(i)
    print(list_10)

    #Sqaured List
    Listnum = [2, 4, 5, 6, 7]
    square_list = []
    for i in Listnum:
        square_list.append(i ** i)
    print(square_list)

    #Multiple elements in a List
    List_num=[2,3,5,6]
    m=0
    for i in List_num:
        i*=i
        m+=i
    print(m)

    #Divisble by 3
    List=[1,2,3,4,5,6,7,8,9,0]
    for i in List:
        if(i%3==0):
            print(i,"is divisible by 3")

    #Prime num of a List
    List=[1,2,3,4,5,6,7,8,9]
    primes = []
    for x in List:
        if x > 1:
            is_prime = True
            for i in range(2, x):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(x)
    print(primes)

    #Print common elements in two lists
    List_one=[1,2,4,5,7,8,9]
    List_two=[2,4,6,7,8,5,3]
    Common_list=[]
    for i in List_one:
        for j in List_two:
            if(i==j):
                Common_list.append(i)
    print(Common_list)

    #Remove all zeroes
    list_numbers=[0,2,3,5,0,5,6]
    for i in list_numbers:
        if(i==0):
            list_numbers.remove(i)
    print(list_numbers)

    #Remove elements less than 10
    List=[1,2,5,7,9,12,54,67]
    for i in List:
        if(i<=10):
            List.remove(i)
    print(List)

    List=[-2,5,2,4,5,-6]
    for i in List:
        if(i<0):
            List.remove(i)
    print(List)

    My_list=[2,3,4,5,6,7,8,9]
    for i in My_list:
        if(i%2==0):
            My_list.remove(i)
            My_list.append(-1)
    print(My_list)

    #Replace negative with zero
    num=[-2,2,4,-4,1]
    for i in num:
        if(i<0):
            num.append(0)
    print(num)

    #Reverse a list
    mylist=[2,4,6,7,8]
    print(mylist[::-1])

    #Reverse even numbers
    MyList=[0,12,5,7,3,6,2,8]
    EvenList=[]
    for i in MyList:
        if(i%2==0):
            EvenList.append(i)
            MyList.remove(i)
    MyList.extend(EvenList)
    print(MyList)

    #Sum even numbers
    My_List=[1,2,3,5,6,7,8,0]
    Even_sum=0
    for i in My_List:
        if(i%2==0):
            Even_sum+=i
    print(Even_sum)
