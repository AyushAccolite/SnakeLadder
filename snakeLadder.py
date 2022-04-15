#class to obtain random dice roll number
import random

#function to play a move by player
def move(pos, player : str):
    dice = random.randint(1,6)
    # print(f"Dice:{dice}")
    #when move is valid move the player
    if(pos + dice <= 100):
        pos = pos + dice
    else:
        print(f"You got number:{dice}, Player {player} remains on the {pos}, keep playing to win \n")
        return pos
    
    #if current tile contains a snake use the dictionary value to move player to defined spot
    if pos in snake:
        # print("Bitten by snake")
        pos = snake[pos]
        print(f"You got number:{dice} Snake bite Player {player}. Player {player} is on {pos}")

    #if current tile contains a ladder use the dictionary value to move player to defined spot
    elif pos in ladder:
        # print("Climbed the ladder")
        pos = ladder[pos]
        print(f"You got number:{dice}, Congrats Player {player} you got the ladder. Player {player} is on {pos}")
    
    else:
        print(f"You got number:{dice}, Player {player} is on {pos}")
    
    print("\n")
    return pos


#making the snake and ladder dictionary for easy access 
ladder = {7:27, 21:91, 31:56}
snake  = {99:6, 90:65, 73:3}

#initial positions of both the players
pos1 = 0
pos2 = 0

print("RULES: Hit the enter button to throw the dice and move the player ahead every time when prompted.")

#running an infinite loop to keep playing until one of the player wins
while True:
    A = input("Player 1: to Roll the dice:")
    pos1 = move(pos1, 1)
    #end the game for any of the player only when it reaches 100th tile and not >= 100
    if (pos1 == 100):
        print("Player 1 won the game. 👍👍👍")
        break
    
    B = input("Player 2: Roll the dice:")
    pos2 = move(pos2, 2)
    if (pos2 == 100):
        print("Player 2 won the game. 👍👍👍")
        break
    
print("Thanks for playing!!!")
