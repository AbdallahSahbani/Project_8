# This program simulates a simple Rock, Paper, Scissors game.
import random


# Function to simulate a player's throw
def throw_rps():
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)


# Function to play one round and decide the winner
def play_round(player1_throw, player2_throw):
    print(f'Player 1 throws {player1_throw}, Player 2 throws {player2_throw}.')

    if player1_throw == player2_throw:
        print('The round is a tie.\n')
        return 'Tie'
    elif (player1_throw == 'Rock' and player2_throw == 'Scissors') or \
            (player1_throw == 'Scissors' and player2_throw == 'Paper') or \
            (player1_throw == 'Paper' and player2_throw == 'Rock'):
        print('Player 1 wins the round.\n')
        return 'Player 1'
    else:
        print('Player 2 wins the round.\n')
        return 'Player 2'


# Main function to run the game
def main():
    # Ask how many rounds to play
    try:
        rounds = int(input('How many rounds do you want to play? '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        return

    player1_wins = 0
    player2_wins = 0
    ties = 0

    # Play the game
    for _ in range(rounds):
        player1_throw = throw_rps()
        player2_throw = throw_rps()
        result = play_round(player1_throw, player2_throw)

        if result == 'Player 1':
            player1_wins += 1
        elif result == 'Player 2':
            player2_wins += 1
        else:
            ties += 1

    # Final results
    print(
        f'Final Score: Player 1 wins {player1_wins} round(s). Player 2 wins {player2_wins} round(s). {ties} round(s) ended in a tie.')

    if player1_wins > player2_wins:
        print('Overall Winner: Player 1!')
    elif player2_wins > player1_wins:
        print('Overall Winner: Player 2!')
    else:
        print('Overall Winner: The game ends in a tie!')


# Call the main function
main()
