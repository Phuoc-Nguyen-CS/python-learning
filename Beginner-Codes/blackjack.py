# blackjack.py
# Name : Phuoc Nguyen
# Date : May 23, 2022
# Last Edit : May 23, 2022

# Sample Output:
# + ----------------------------------------------- +
# |    _     _            _    _            _       |
# |   | |   | |          | |  (_)          | |      |
# |   | |__ | | __ _  ___| | ___  __ _  ___| | __   |
# |   | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /   |
# |   | |_) | | (_| | (__|   <| | (_| | (__|   <    |
# |   |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\   |
# |                          _/ |                   |
# |                         |__/                    |
# + ----------------------------------------------- +

# + ----------------------------------------------- +
# |             Please Enter Your Name:             |
# |                 => _________                    |
# |                 Hello ________                  |
# + ----------------------------------------------- +
#                          |
# + ----------------------------------------------- +
# |             Starting Game . . .                 |
# + ----------------------------------------------- +
#
#
# + ----------------------------------------------- +
# |          The Dealer has pulled a [10]           |
# |             Your hand is a [10,2]               |
# |       Would you like to (h)it or (s)tay         |
# |       => h                                      |
# |             Your hand is now [10,2,3]           |
# |       Would you like to (h)it or (s)tay         |
# |       => s                                      |
# |          The Dealer's hand is now [10,11]       |
# |                 The Dealer Won!                 |
# |                                                 |
# |                 Play Again?(y/n)                |
# |       => n                                      |
# + ----------------------------------------------- +



import random
import time

def intro_art():
    print("""
    + ----------------------------------------------- +
    |    _     _            _    _            _       |
    |   | |   | |          | |  (_)          | |      |
    |   | |__ | | __ _  ___| | ___  __ _  ___| | __   |
    |   | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /   |
    |   | |_) | | (_| | (__|   <| | (_| | (__|   <    |
    |   |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\   |
    |                          _/ |                   |
    |                         |__/                    |
    + ----------------------------------------------- +
    """)

def user_name_prompt():
    """ Displays the user name the user has chosen. """

    print("""
    + ----------------------------------------------- +
                 Please Enter Your Name:             
    """)
    username = input("""
                     => """)

    print(f"""
    + ----------------------------------------------- +
                     Hello {username}                  
    + ----------------------------------------------- +
    """)


def play_game(deck):
    """ Returns a boolean value indicating whether the
        player wants to continue playing"""

    players_hand = []
    players_values = []
    dealers_hand = []
    dealers_values = []

    draw_name = ""

    draw_name, draw_value = random.choice(list(deck.items()))

    dealers_hand.append(draw_name)
    dealers_values.append(draw_value)

    print(dealers_hand,dealers_values)

    for i in range(2):
        draw_name, draw_value = random.choice(list(deck.items()))
        players_hand.append(draw_name)
        players_values.append(draw_value)

    print(players_hand, players_values)

    print(f"""
    + ----------------------------------------------- +
              The Dealer has pulled a [10]           
                 Your hand is a [10,2]               
           Would you like to (h)it or (s)tay         
           => h                                      
                 Your hand is now [10,2,3]           
           Would you like to (h)it or (s)tay         
           => s                                      
              The Dealer's hand is now [10,11]       
                     The Dealer Won!                 
                                                    
                     Play Again?(y/n)                
           => n                                      
    + ----------------------------------------------- +
    """)

def black_jack_game():

    cards = {
        "Ace of Spades"   : [1,11],
        "Ace of Clovers"   : [1,11],
        "Ace of Diamonds" : [1,11],
        "Ace of Hearts" : [1,11],
        "Two of Spades"   : 2,
        "Two of Clovers" : 2,
        "Two of Diamonds"   : 2,
        "Two of Hearts" : 2,
        "Three of Spades" : 3,
        "Three of Clovers" : 3,
        "Three of Diamonds" : 3,
        "Three of Hearts" : 3,
        "Four of Spades"  : 4,
        "Four of Clovers" : 4,
        "Four of Diamonds": 4,
        "Four of Hearts" : 4,
        "Five of Spades"  : 5,
        "Five of Clovers" : 5,
        "Five of Diamonds": 5,
        "Five of Hearts" : 5,
        "Six of Spades"   : 6,
        "Six of Clovers" : 6,
        "Six of Diamonds" : 6,
        "Six of Hearts": 6,
        "Seven of Spades" : 7,
        "Seven of Clovers" : 7,
        "Seven of Diamonds" : 7,
        "Seven of Hearts": 7,
        "Eight of Spades" : 8,
        "Eight of Clovers" : 8,
        "Eight of Diamonds" : 8,
        "Eight of Hearts" : 8,
        "Nine of Spades"  : 9,
        "Nine of Clovers" : 9,
        "Nine of Diamonds" : 9,
        "Nine of Hearts" : 9,
        "Ten of Spades" : 10,
        "Ten of Clovers" : 10,
        "Ten of Diamonds" : 10,
        "Ten of Hearts" : 10,
        "Jack of Spades" : 10,  
        "Jack of Clovers" : 10,
        "Jack of Diamonds" : 10,
        "Jack of Hearts" : 10,
        "Queen of Spades" : 10,
        "Queen of Clovers" : 10,
        "Queen of Diamonds" : 10,
        "Queen of Hearts" : 10,
        "King of Spades" : 10,
        "King of Clovers" : 10,
        "King of Diamonds" :  10,
        "King of Hearts" : 10
    }

    continue_game = True

    intro_art()
    user_name_prompt()


    while(continue_game):
        continue_game = play_game(cards)


black_jack_game()
