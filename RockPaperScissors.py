import random

emojis = {'R': '🪨', 'P': '📃', 'S': '✂️'}
choices = ('R', 'P', 'S')

while True:
    user_choice = input('Rock, paper, or scissors? (R/P/S): ').upper()
    
    if user_choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == 'R' and computer_choice == 'S') or
        (user_choice == 'S' and computer_choice == 'P') or 
        (user_choice == 'P' and computer_choice == 'R')
    ):
        print('You WIN')
    else:
        print('You LOSE')

    should_continue = input('Continue? (Y/N): ').lower()

    if should_continue != 'y':  
        break


           
                                                
       








    







    
    