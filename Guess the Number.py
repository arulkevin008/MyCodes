import random
options=[0,1,2,3,4,5,6,7,8]
print("\t\t\tGuess from 1 to 10\t\t\t\n")
user_score=0
while True:
    n=int(input("\nGuess the right number:"))
    choice=random.choice(options)
    (n,choice)
    if(n<choice):
        print(n,"is Too Low")
    elif(n>choice):
        print(n,"is Too High")
    else:
        print(n,"is the correct no")
        print("YOU GUESSED RIGHT!!")
        user_score+=1
        print("Score:",user_score)

        
    
