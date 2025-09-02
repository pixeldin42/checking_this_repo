import random

# A program that simulates a simple dice rolling game.

def roll_dice():
  """Rolls a pair of six-sided dice and returns the sum."""
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  return die1 + die2

<<<<<<< HEAD
# Generate and print 10 sets of numbers
for _ in range(10):
    numbers = generate_numbers()
    print_set (numbers)
=======
def game_loop():
  """Main game loop."""
  player_score = 0
  computer_score = 0
  
  print("Let's play a dice game!")
  print("The first to a score of 10 or more wins!")

  while player_score < 10 and computer_score < 10:
    input("Press Enter to roll your dice...")
    player_roll = roll_dice()
    player_score += player_roll
    print(f"You rolled a {player_roll}. Your score is now {player_score}.")

    computer_roll = roll_dice()
    computer_score += computer_roll
    print(f"The computer rolled a {computer_roll}. The computer's score is now {computer_score}.")
    
  if player_score >= 10:
    print("Congratulations! You won!")
  else:
    print("The computer won. Better luck next time!")

game_loop()
>>>>>>> main
