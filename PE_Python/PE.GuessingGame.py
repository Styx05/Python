#!/usr/bin/env pyhton

import random
import time

#Create a function
def play_guessing_game():
    print("Welcome to the 2 player Guessing Game!")
    
    # Get player names 
    print("Player 1, please enter your name:")
    player1 = input("> ")
    print("Player 2, please enter your name:")
    player2 = input("> ")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Using formatted string literals to keep code clean
    print(f"\nOkay, {player1} and {player2}, I'm thinking of a number between 1 and 100. Let's begin!")
    
    # Game starts
    # Start the timer. Not in loop because time has to start without any further condition
    start_time = time.time()
    
    # Initialize scores
    score1 = 0
    score2 = 0
    
    # Using a while loop to keep the game going untill the correct number is guessed.
    # Within the while loop there is an if-elif-else block to specify the further context of the game
    while True:
        print(f"\n{player1}, it's your turn to guess!")
        guess1 = int(input("> ")) #Get answer from player 1
        score1 += 1 #Increment the score each guess + 1
        
        print(f"{player2}, it's your turn to guess!")
        guess2 = int(input("> ")) #Get answer from player 2
        score2 += 1 #Increment the score each guess + 1
        
        if guess1 == number:
            # Stop the timer and calculate elapsed time. In loop because time needs to stop after a correct guess
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print(f"\nWe have a winner!! Congratulations, {player1}! You guessed the correct number, {number}!")
            print(f"Time taken: {elapsed_time:.2f} seconds") # using time format specifier
            score1 += 1
            break # Returns to the rest of the program if the condition is true
        elif guess2 == number:
            # Stop the timer and calculate elapsed time
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print(f"\nWe have a winner!! Congratulations, {player2}! You guessed the correct number, {number}!")
            print(f"Time taken: {elapsed_time:.2f} seconds") # using time format specifier
            score2 += 1
            break # Returns to the rest of the program if the condition is true
        # Player specific messages to indicate whether each player needs to guess higher or lower
        elif guess1 < number:
            print(f"{player1}, guess higher!")
        elif guess1 > number:
            print(f"{player1}, guess lower!")
        if guess2 < number: # Start a new if-elif block so both players receive feedback on their guesses
            print(f"{player2}, guess higher!")
        elif guess2 > number:
            print(f"{player2}, guess lower!")
        else:
            print("Oops! That's not the correct number. Try again!")
            
        # Add a delay of 1 second before the next turn - for player comfort
        time.sleep(1)
    
    # Display the number of guesses for each player
    print("\n||--- Final Scores ---||")
    print(f"{player1}: {score1} guess(es)")
    print(f"{player2}: {score2} guess(es)")

play_guessing_game()
