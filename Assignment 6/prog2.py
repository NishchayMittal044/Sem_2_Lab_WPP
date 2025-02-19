# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.

# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.

import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        """Randomly selects rock, paper, or scissors for the computer."""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """Determines the winner of a round."""
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def has_winner(self):
        """Checks if someone has won the entire game."""
        return self.user_wins > self.total_rounds // 2 or self.computer_wins > self.total_rounds // 2

    def play_round(self, user_choice):
        """Plays a single round of the game."""
        if self.current_round >= self.total_rounds:
            return "Game over!"
        
        self.current_round += 1
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        return {
            "round": self.current_round,
            "user_choice": user_choice,
            "computer_choice": computer_choice,
            "winner": winner,
            "user_wins": self.user_wins,
            "computer_wins": self.computer_wins,
        }

    def get_winner(self):
        """Returns the overall winner of the game."""
        if self.user_wins > self.computer_wins:
            return "User wins"
        elif self.computer_wins > self.user_wins:
            return "Computer wins"
        else:
            return "Tie"
        
game = RockPaperScissors(3)
print(game.play_round("rock"))
print(game.play_round("paper"))
print(game.play_round("scissors"))
print(game.get_winner())
