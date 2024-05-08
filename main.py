import sys
import random
import time
import math
from cards import deck



# Initializations
score = 0
dealer_score = 0
wonbet = 0
lostbet = 0
attempted_wager = 0
chosen_move = ''
bet = 0

# Functions
def hit():
    global score
    random_card = random.choice(list(deck.keys()))
    card_value = deck[random_card]
    score += card_value
    return random_card

def dealer_hit():
    global dealer_score
    random_card = random.choice(list(deck.keys()))
    card_value = deck[random_card]
    dealer_score += card_value
    return random_card

def get_valid_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")




# Currency System
house_balance = get_valid_integer_input('Enter how much the house has as a whole number: ') 
cash = get_valid_integer_input('Enter your buy-in as a whole number: ')
wonbet += bet * 2
lostbet -= cash







# Intro
print("Welcome to BlackJack where your odds to win are very high!")
time.sleep(3)
print("Type 'quit' to exit at anytime.")
time.sleep(1)




# The Blackjack
while chosen_move != 'quit':
#put dealer_score = 0 if bug happens

    # Checks if player has enough money or not
    while True:
        if cash == 0:
            print("You are out of money goodbye!")
            sys.exit()
        
        
        bet = get_valid_integer_input(f"Current Balance: ${cash}\nHow much would you like to wager? ")
        
        
        if bet > cash:
            print("You don't have enough to wager that amount!")
        else:
            print("Thanks for betting with ChrisTDB Casino!")
            time.sleep(2)
            break
        


    cash -= bet
    chosen_move = ''
    


    if house_balance <= 0:
        # If house is making a loss, program automatically pulls ace of hearts
        dealer_score += 11
        print("The Dealer's first card is: Ace of hearts")
        print(f"Dealer score: {dealer_score}")
    else:
        # This makes it appear legit!
        dealer_drawn_card = dealer_hit()
        print(f"The Dealer's first card is: {dealer_drawn_card}")
        print(f"Dealer score: {dealer_score}")
    
    time.sleep(3)

    # Mechanics
    while score <= 21 and chosen_move != 's':
        
        chosen_move = input("Type 'h' to hit 's' to stand, anything else will result in forfeit: ")
        
        if chosen_move == 'h':
            drawn_card = hit()  # Get the drawn card
            print("You drew:", drawn_card)
            print("Your score:", score)
        elif chosen_move == 's':
            print(f'You stand...',end=' ')
            print(f'your score is {score}')
            break
        else:
            print('You forfeit the hand')
            break
        
        time.sleep(2)

    # Dealers move after players turn
    while dealer_score <= 17:
        # Riggity Rigged
        if house_balance <= 0:
            dealer_score += 10
            print("The Dealer's first card is: Jack of hearts")
            print(f"Dealer score: {dealer_score}\n")
            break
        
        # Fair Odds as long as the house is making a profit!
        if dealer_score > score:
            break
        else:
            
            dealer_drawn_card = dealer_hit()
            
            print(f"The Dealer's pulled: {dealer_drawn_card}")
            print(f"Dealer score: {dealer_score}\n")
            time.sleep(2)


        
    # Scoring Logic
    if score > 21:
        print('You bust, thank you for your money GGEZ!')
        house_balance += bet
        continue
    elif score == 21:
        print(f'Wow you got blackjack your lucky here is your ${math.floor(bet * 2.5)}')
        cash += math.floor(bet * 2.5)
        house_balance -= math.floor(bet * 2.5)
    elif score < 21:
        if score > dealer_score or dealer_score > 21:
            print(f'You got lucky and won ${bet}')
            cash += bet * 2
            house_balance -= bet
        elif score == dealer_score:
            cash += bet
        elif score < dealer_score:
            print(f'You lost ${bet}')
            house_balance += bet
    
    score = 0
    dealer_score = 0