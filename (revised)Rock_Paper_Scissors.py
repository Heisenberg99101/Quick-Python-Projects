import random, sys

wins = 0 
loses = 0
draws = 0

while True:
    print("%s Wins, %s Loses, %s Draws" % (wins, loses, draws))
    while True:
        player = input('Your Turn: Rock(1), Paper(2), Scissor(3) or Quit(q)\n')
        if player == 'q':
            sys.exit()
        if player == '1' or player == '2' or player == '3':
            break
        
    
    if player == '1':
        print('You chose: ROCK')
    if player == '2':
        print('You chose: PAPER')
    if player == '3':
        print('You chose: SCISSOR')

    a = random.randint(1,3)
    if a == 1:
        comp = '1'
        print("Computer chose: ROCK")
    if a == 2:
        comp = '2'
        print("Computer chose: PAPER")
    if a == 3:
        print("Computer chose: SCISSOR")

    # MAIN
    if player == comp:
        print("IT IS TIE !!!")
        draws = draws + 1
    
    elif player == '1' and comp == '2':
        print('YOU LOSE !!!')
        loses = loses + 1
    elif player == '1' and comp == '3':
        print('YOU WIN !!!')
        wins = wins + 1

    elif player == '2' and comp == '1':
        print('YOU WIN !!!')
        wins = wins + 1
    elif player == '2' and comp == '3':
        print('YOU LOSE !!!')
        loses = loses + 1
    
    elif player == '3' and comp == '2':
        print('YOU WIN !!!')
        wins = wins + 1
    elif player == '3' and comp == '1':
        print('YOU LOSE !!!')
        loses = loses + 1

    




        