import random

emojis = { 'r': '🪨', 'p': '🧻', 's': '✂️'}
choices = ('r','p','s')


while True:

    preson = input("Wanna play with Computer or Friend? (c/f)").lower()
    
    if preson == 'c':
        user_win = 0 
        computer_win = 0

        while (user_win<3) and (computer_win<3):

            user_choice = input("Rock, paper or scissors? (r/p/s)").lower()
            if user_choice not in choices:
                print("Invalid choice!")
                continue

            computer_choice = random.choice(choices)
            print(f'You choose: {emojis[user_choice]}  Computer choose: {emojis[computer_choice]}')

            if computer_choice == user_choice:
                print("Tie!")
            elif (
                (user_choice == 'r' and computer_choice == 's') or 
                (user_choice == 'p' and computer_choice == 'r') or
                (user_choice == 's' and computer_choice == 'p')):
                print("You Win")
                user_win += 1
            else:
                print("You Lose!")
                computer_win += 1    
        print(f'Human: {user_win} || Computer: {computer_win}')
        if user_win > computer_win:
            print("Human Win All Game!")
        else:
            print("Computer Win All Game!")
         

    elif preson == 'f':
        user_win = 0
        friend_win = 0
        while (friend_win < 3) and (user_win < 3) :

            user_choice = input("P1: Rock, paper or scissors? (r/p/s)").lower()
            if user_choice not in choices:
                print("Invalid choice! P1")
                continue

            friend_choice = input("P2: Rock, paper or scissors? (r/p/s)").lower()
            if friend_choice not in choices:
                print("Invalid choice! P2")
                continue

            
            print(f'P1 choose:{emojis[user_choice]}  P2 choose:{emojis[friend_choice]}')

            if friend_choice == user_choice:
                print("Tie!")
            elif (
                (user_choice == 'r' and friend_choice == 's') or 
                (user_choice == 'p' and friend_choice == 'r') or
                (user_choice == 's' and friend_choice == 'p')):
                print("P1 Win!")
                user_win += 1
            else:
                print("P2 Win!")
                friend_win += 1

        print(f'P1: {user_win} || P2: {friend_win}')
        if user_win > friend_win:
            print("P1 Win All Game!")
        else:
            print("P2 Win All Game!")
    else:
        print("Invalid Choice!")
        continue

    choice = input("One More Game? y/n")
    if choice == 'n':
        break
    
