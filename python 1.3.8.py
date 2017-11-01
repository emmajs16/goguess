from __future__ import print_function
import random

def validate():
     guess = '1' # initialization with a bad guess
     answer = 'hangman word'
     while guess not in answer:
         guess = raw_input('Name a letter in \'' + answer + '\': ')
     print('Thank you!')

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
     
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # This code goes through and ask the user to choose who they think won the lottery.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # for each player and the total players minus one
        print(p+', ', end='')
    print(players[len(players)-1]) # print until you get it right

    ####
    # It keeps a count of how many guesses have been taken.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
    

def goguess():
    secret = random.randint(1, 20)
    print('Guess a number between 1 and 20: ',end='')
    guesses=1
    guess = int(raw_input('Guess: '))
    while guess != secret:
        if guess > secret: 
            print('Too big!')
            guess = int(raw_input('Guess: ')) 
            guesses+=1
        if guess < secret:
            print('Too small!')
            guess = int(raw_input('Guess: '))
            guesses+=1
    if guess == secret:
        print('Correct! The right answer is', secret,'. In only', guesses,' guesses.')