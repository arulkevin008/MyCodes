import random
options=["rock","paper","scissor"]
print("\t\t\t Rock | Paper | Scissor\t\t\t\n")
user_score=0
while True:
    n=input("Enter your choice:").lower()
    choice=random.choice(options)
    if n not in(options):
        print("Invalid input!")
    elif n==choice:
       print("You choose",n.capitalize(), "and Computer choose",choice.capitalize())
       print("Draw!")
    elif(n=="paper" and choice=="rock")or \
         (n=="rock" and choice=="scissor")or \
         (n=="scissor" and choice=="paper"):
            print("You choose",n.capitalize(), "and Computer choose",choice.capitalize())
            print("You Win!")
            user_score+=1
            print("Score:",user_score)
    else:
            print("You choose",n.capitalize(), "and Computer choose",choice.capitalize())
            print("You Lose!")    
    

