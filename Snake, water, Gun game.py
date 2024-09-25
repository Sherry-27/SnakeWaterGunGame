import random

def game():
    print("Welcome to Snake, Water, Gun Game!")
    print("You will be playing against the computer.")
    print("Enter 's' for snake, 'w' for water, and 'g' for gun.")
    print("You can play as many times as you want. To quit the game, enter 'q'.")
    options = ['s', 'w', 'g']
    player_score = 0
    computer_score = 0
    
    while True:
        player_choice = input("Your turn: ").lower()
        if player_choice == 'q':
            break
        elif player_choice not in options:
            print("Invalid input. Please enter 's', 'w', 'g', or 'q'.")
            continue
        else:
            computer_choice = random.choice(options)
            print(f"Computer's turn: {computer_choice}")
            if player_choice == computer_choice:
                print("It's a tie!")
            elif player_choice == 's' and computer_choice == 'w':
                print("You win! Snake drinks water.")
                player_score += 1
            elif player_choice == 'w' and computer_choice == 'g':
                print("You win! Water douses fire.")
                player_score += 1
            elif player_choice == 'g' and computer_choice == 's':
                print("You win! Gun shoots snake.")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        print(f"Your score: {player_score}, Computer's score: {computer_score}")
    print("Thanks for playing!")
    
game()
