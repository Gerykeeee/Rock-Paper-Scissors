import random
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Game_Result(Enum):
    TIE = "It's a TIE"
    WIN = "You WIN!"
    LOSE = "Computer wins"

class Game_Logic:
    def __init__(self):
        
        self.winning_combos = {
             Move.ROCK: Move.SCISSORS,
             Move.PAPER: Move.ROCK,
             Move.SCISSORS: Move.PAPER
        }

    
    def determine_winner(self, player_move: Move, computer_move: Move) -> Game_Result:
        if player_move == computer_move:
            return Game_Result.TIE
        elif self.winning_combos[player_move] == computer_move:
            return Game_Result.WIN
        else:
            return Game_Result.LOSE
            
    def play(self) -> None:
        print("--Welcome--")

        while True:
            user_input = input("Give me your choice (ROCK --> 1 // PAPER --> 2 // SCISSORS --> 3 // 'q' to QUIT):\n ")

            if user_input.lower() == 'q':
                print("Goodbye!")
                break 

            try:
                player_move = Move(int(user_input))
            except ValueError:
                print("Invalid number or character, try again!")
                continue

            
            computer_move = random.choice(list(Move))

            print(f"Your choice: {player_move.name} // Computer choice: {computer_move.name}")

            
            result = self.determine_winner(player_move, computer_move)
            print(result.value)

if __name__ == '__main__':
    game = Game_Logic()
    game.play()
