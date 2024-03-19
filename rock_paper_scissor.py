import random as r
sc = 0
n = int(input("Enter how many times do you want to play: "))
for i in range(n):
    s = int(input("Enter 1 for rock 2 for paper and 3 for scissor: "))
    c = r.randint(1,3)
    if(c==1):
        print("Computer chooses rock")
    elif(c==2):
        print("Computer chooses paper")
    elif(c==3):
        print("Computer chooses scissor")
    if(s==1 and c==3):
        print("You won")
        sc+=1
    elif(s==1 and c==2):
        print("You lose")
        sc+=0
    elif(s==2 and c==1):
        print("You won")
        sc+=1
    elif(s==2 and c==3):
        print("You lose")
        sc+=0
    elif(s==3 and c==2):
        print("You won")
        sc+=1
    elif(s==3 and c==1):
        print("You lose")
        sc+=0
    elif(s==c):
        print("Tie")
    print(f"Your score: {sc}")
