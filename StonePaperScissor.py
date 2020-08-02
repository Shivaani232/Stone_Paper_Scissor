import random
min=1
max=3
n=4
player1=0
player2=0
obj1=0
obj2=0
print("Welcome to Stone,Paper,Scissor Game!")
print("Two players required.")
print("Result is based on three rounds!")
print("Game Starts!")
for i in range(1,n):
    print("Ready for round "+str(i)+"?")
    ans=input()
    if ans.lower()=="yes" or ans.lower()=="y":
        print("Round "+str(i))
        obj1=random.randint(min,max)
        obj2=random.randint(min,max)
        if obj1==1 and obj2==1:
            player1+=1
            player2+=1
            print("Both the players choose Stone")
            print("Draw in round "+str(i))
        elif obj1==1 and obj2==2:
            player2+=1
            print("Player 1 chooses Stone and Player 2 chooses Paper")
            print("Player 2 wins in round "+str(i))
        elif obj1==1 and obj2==3:
            player1+=1
            print("Player 1 chooses Stone and Player 2 chooses Scissor")
            print("Player 1 wins in round "+str(i))
        elif obj1==2 and obj2==1:
            player1+=1
            print("Player 1 chooses Paper and Player 2 chooses Stone")
            print("Player 1 wins in round "+str(i))
        elif obj1==2 and obj2==2:
            player1+=1
            player2+=1
            print("Both the players choose Paper")
            print("Draw in round "+str(i))
        elif obj1==2 and obj2==3:
            player2+=1
            print("Player 1 chooses Paper and Player 2 chooses Scissor")
            print("Player 2 wins in round "+str(i))
        elif obj1==3 and obj2==1:
            player2+=1
            print("Player 1 chooses Scissor and Player 2 chooses Stone")
            print("Player 2 wins in round "+str(i))
        elif obj1==3 and obj2==2:
            player1+=1
            print("Player 1 chooses Scissor and Player 2 chooses Paper")
            print("Player 1 wins in round "+str(i))
        elif obj1==3 and obj2==3:
            player1+=1
            player2+=1
            print("Both the players choose Scissor")
            print("Draw in round "+str(i))
        else:
            print(" ")
    else:
        print("Game forcefully closed")
        exit()
        
print("Game Ends")
print("---------------------------------------------------------------")
print("RESULT:")
print("SCORE of Player 1:"+str(player1))
print("SCORE of Player 2:"+str(player2))
if player1>player2:
    print("Player 1 WINS")
elif player1==player2:
    print("DRAW match")
else:
    print("Player 2 WINS")
        
    
    
