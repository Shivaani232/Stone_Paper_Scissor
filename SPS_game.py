import random
min=1
max=3

player1=0
player2=0

obj1=0
obj2=0
print("Welcome to Stone,Paper,Scissor Game")
print("-------------------------------------------------------------")
print("Your Name:")
name=input()
print("_"+name+" Vs Computer_")
print("Number of Rounds:")
n=int(input())
print("Result is based on "+str(n)+" rounds.")
print("Game Starts")
print("-------------------------------------------------------------")
for i in range(1,n+1):
    print("Ready for round "+str(i)+"?")
    ans=input()
    if ans.lower()=="yes" or ans.lower()=="y":
        print("Round "+str(i))
        print("Enter your choice(Number)(1.Stone/2.Paper/3.Scissor):")
        obj1=int(input())
        obj2=random.randint(min,max)
        if obj1==1 and obj2==1:
            player1+=1
            player2+=1
            print("Both chose Stone")
            print("Draw in round "+str(i))
        elif obj1==1 and obj2==2:
            player2+=1
            print("You chose Stone and Computer chose Paper")
            print("Computer won in round "+str(i))
        elif obj1==1 and obj2==3:
            player1+=1
            print("You chose Stone and Computer chose Scissor")
            print("You won in round "+str(i))
        elif obj1==2 and obj2==1:
            player1+=1
            print("You chose Paper and Computer chose Stone")
            print("You won in round "+str(i))
        elif obj1==2 and obj2==2:
            player1+=1
            player2+=1
            print("Both chose Paper")
            print("Draw in round "+str(i))
        elif obj1==2 and obj2==3:
            player2+=1
            print("You chose Paper and Computer chose Scissor")
            print("Computer won in round "+str(i))
        elif obj1==3 and obj2==1:
            player2+=1
            print("You chose Scissor and Computer chooses Stone")
            print("Computer won in round "+str(i))
        elif obj1==3 and obj2==2:
            player1+=1
            print("You chose Scissor and Computer chose Paper")
            print("You won in round "+str(i))
        elif obj1==3 and obj2==3:
            player1+=1
            player2+=1
            print("Both chose Scissor")
            print("Draw in round "+str(i))
        else:
            print(" ")
    else:
        print("Game forcefully closed")
        exit()
        
print("Game Ends")
print("-------------------------------------------------------------")
print("RESULT:")
print(name+"'s"+" SCORE:"+str(player1))
print("Computer's SCORE:"+str(player2))
if player1>player2:
    print(name+" WON")
elif player1==player2:
    print("DRAW match")
else:
    print("Computer WON")
        
