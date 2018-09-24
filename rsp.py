p1=input("Rock,Paper or Scissors: ")
p2=input("Rock,Paper or Scissors: ")
print("Player1 choosed ",p1)
print("Player2 choosed ",p2)
while p1=="Rock":
    if p2=="Rock":
        print("Game is equal")
    elif p2=="Paper":
        print("Winner is Player2")
    elif p2=="Scissors":
        print("Winner is player2")
    break

while p1=="Paper":
    if P2=="Rock":
        print("Winner is player1")
    elif p2=="Paper":
        print("Game is equal")
    elif p2=="Scissors":
        print("Winner is player2")
    break

while p1=="Scissors":
    if P2=="Rock":
        print("Winner is player2")
    elif p2=="Paper":
        print("Winner is player1")
    elif p2=="Scissors":
        print("Game is equal")
    break



    
