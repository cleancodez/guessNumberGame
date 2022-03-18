import random

while True:
    num_len = int(input("Guess a number from 1 to ___ : "))
    for i in range(1,num_len):
        num = random.randrange(1,num_len)
        guess = int(input(f"Guess a number from 1 to {num_len}: "))

        while guess != num:
            if guess < num:
                print('You need to guess higher. Try again!')
                guess = int(input('\nGuess a number : '))
            else:
                print('You need to guess lower. Try again!')
                guess = int(input('\nGuess a number : '))
        print("You guessed it! Congrats!")