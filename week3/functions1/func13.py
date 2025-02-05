import random
print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')
number = random.randint(1, 20)
def tron():
    i = 1
    while True:
        valve = int(input())
        if number == valve:
            print(f'Good job, {name}! You guessed my number in {i} guesses!')
            break
        elif valve < number:
            print('Your guess is too low->.' "\n" 'Take a guess.')
        elif valve > number:
            print('Your guess is too high<-.' "\n" 'Take a guess.')
        i += 1
tron()