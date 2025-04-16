# Abdallah_Sahbani_IA_7

import random
import time


# This function simulates rolling a six-sided dice and returns a random number between 1 and 6
def roll_dice():
    return random.randint(1, 6)


# This function compares the random dice rolls between two players and prints results
def play_round(player1_name, player2_name, player1_roll, player2_roll):
    if player1_roll > player2_roll:
        print(
            f"{player1_name} rolls a {player1_roll}, {player2_name} rolls a {player2_roll}. {player1_name} wins the round.")
        return 1  # Player 1 wins
    elif player2_roll > player1_roll:
        print(
            f"{player1_name} rolls a {player1_roll}, {player2_name} rolls a {player2_roll}. {player2_name} wins the round.")
        return 2  # Player 2 wins
    else:
        print(f"{player1_name} rolls a {player1_roll}, {player2_name} rolls a {player2_roll}. The round is a tie.")
        return 0  # Tie


# This is the main function that runs the entire dice game
def main():
    # Get each player's name from user input allows for personalized smoother user interaction
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    # Ask the user how many rounds they want to play can only be a integer
    rounds = int(input("How many rounds do you want to play? "))

    # Set counters to keep track of each player's wins and number of ties
    player1_wins = 0
    player2_wins = 0
    ties = 0

    # Loop through the number of rounds
    for _ in range(rounds):
        # Simulate dice roll for Player 1
        player1_roll = roll_dice()
        print(f"{player1_name} rolls...")
        time.sleep(0.8)

        # Simulate dice roll for Player 2
        player2_roll = roll_dice()
        print(f"{player2_name} rolls...")
        time.sleep(0.8)

        # Play one round and determine the winner
        result = play_round(player1_name, player2_name, player1_roll, player2_roll)

        # Short pause before next round
        time.sleep(1)

        # Update the running score based on the result of the round
        if result == 1:
            player1_wins += 1
        elif result == 2:
            player2_wins += 1
        else:
            ties += 1

    # After all rounds, print the final results
    print(
        f"\nFinal Score: {player1_name} wins {player1_wins} round(s). {player2_name} wins {player2_wins} round(s). {ties} round(s) ended in a tie.")

    # functional equation determining correct winner
    if player1_wins > player2_wins:
        print(f"Overall Winner: {player1_name}!")
    elif player2_wins > player1_wins:
        print(f"Overall Winner: {player2_name}!")
    else:
        print("The game is a tie!")


# Start the game by calling main
main()
