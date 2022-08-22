import random
print("----------Number guessing game---------")
print("----------Rules of the Game------------")
print("1.you will be given 5 chances to guess the correct number.")
print("2.for correct guess you will earn 1 point and loose 1 point for wrong guess.")
print("3.Maximum score : 5")
print("4.Minimum score : 0")
print("_________________________________________________________________________")
print("_________________________________________________________________________")
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print("***Congratulations,you have Won!!!!!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print("***Congratulations,you have Won!!!!!!")


guess(10)
