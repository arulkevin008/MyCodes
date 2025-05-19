import random
options=[0,1,2,3,4,5,6,7,8,9]
user_score=0
n=input("Select Batting or Bowling:")
if(n=="Batting"):
    print("You are Batting")
else:
    print("You are Bowling")
while True:
    choice=random.choice(options)
    s=int(input("Enter Your choice from 1 to 10:"))
    print(s,choice)
    user_score+=s
    if(s==choice):
        print("You Lose")
        print(user_score)
        user_score=0
        break

