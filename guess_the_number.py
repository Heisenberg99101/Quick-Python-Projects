import random
randNumber = random.randint(1, 20)

userguess = None
guesses = 0

while userguess != randNumber:
    userguess = int(input('Guess the number:\n'))
    guesses += 1
    if userguess==randNumber :
        print('You guessed the right number !!!\n')
    else:
        if userguess > randNumber:
            print('You guessed the wrong number. Try a smaller number.\n')
        else:
            print('You guessed the wrong number. Try a larger number.\n')

print(f"You guessed the number in {guesses} guesses.\n")

with open("hiscore.txt") as f:
    hiscore = int(f.read())

if guesses<hiscore:
    print('You have broken the highscore !!!')
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))