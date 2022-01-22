import random


class Card:
    

    def set(self):
        self.value = 0
        self.points = 0
    def generate(self):
        pass
        #Assigns Points and Creates a Card
       
"""
The code run but lack logical function.
It will make more sense if someone could just go through and fix it
or suggest something different."""
    
    # The best way to represent a “playing card” is 
# by using objects. So We create a Card class.
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

"""
Before we move onto the game logic, we need set up some game variables:

Previous Card = We need to initialize the previous card with an empty card.
Current Card = Initialize the current card

A standard rule of Hi-Lo game requires the starting card to not be the lowest card or the highest card.
We rmove the current card from the deck of cards
Score = The count of correct guesses.
Chances = The number of chances left for an incorrect guess. 
      
"""
# The function hi_lo_game is responsible for the running of a game. 
# It requires a deck of cards for its working.
def hi_lo_game(deck):
 
    global cards_values
 
    # Initialize the previous card
    previous_card = Card(" ", " ")
 
    # Initialize the current card
    current_card = random.choice(deck)
 
    # The starting card cannot be lowest or highest
    while current_card.value == "A" or current_card.value == "K":
        current_card = random.choice(deck)
 
    # Remove the card from the deck 
    deck.remove(current_card)
 
    # Number of chances left in the game
    chances = 5
 
    # The current score
    score = 0
    
    
    # The while loop runs until the chances left for the player is not zero.
    # The GAME LOOP
    while chances:
        print()
        print("------------------------------------")
        print("HILO GAME MENU")
        print("------------------------------------")
        print()
        print("Enter 3--4 to bet for a high card")
        print("Enter 1--2 to bet for a low card")
        print()
         
        # Check if we reached the end of the deck
        if len(deck) == 0:
           
            print(previous_card, current_card)
            print("YOU HAVE REACHED THE END OF THE DECK!")
            print("Congratulations!!!")
            print()
            print("Your Final Score is=", score)
            print()
            print("Thank you for playing!!! Do play again next time.")
            break
 
        # Try block for player input error
        try:
            choice = int(input("Please Enter your choice =: "))
        except ValueError:
            
            print("Wrong Input!! Try Again.")
            continue   
 
        # Some wrong choice
        if choice > 4 or choice < 1:
            print("Invalid Response!! Please Try Again.")
            continue       
 
        # Switch the current card to the previous card
        previous_card = current_card
 
        # Choose the new current card
        current_card = random.choice(deck)
 
        # Remove the new card from the deck
        deck.remove(current_card)
 
        # A high card
        if cards_values[current_card.value] > cards_values[previous_card.value]:
            result = 4
 
        # A low card    
        elif cards_values[current_card.value] < cards_values[previous_card.value]:
            result = 1
 
        # Same value card   
        else:
            result = -1    
 
        # A Tie Round
        if result == -1:
            print("TIE GAME!! Please Play Again")
 
        # Round won
        elif choice == result:
            print("YOU WIN!!! Please Play Again")
            score = score + 1  
 
        # Round Lost    
        else:
            if chances == 1:
                
                print("GAME OVER")
                print(previous_card, current_card)
                print("Your Final Score is =", score)
                print()
                print("Thank you for playing!!!")
            
            elif chances == 0:
                print("GAME OVER")
                print(previous_card, current_card)
                print("Your Final Score is =", score)
                print()
                print("Thank you for playing!!!")
                
            
            else:
                print("YOU LOSE!! Please Try Again next time") 
 
  
"""
We need certain data structures to store the types of suits and cards because
each of these data structures play some certain roles in the smooth functioning of the game.
    """
# The card's suites
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
# The suit value 
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
# The card value
cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
    
"""
A deck of cards contain 52 cards, each with a different combination
of suit and value. Using a list of objects, we store all the cards.
"""
# The deck of cards
deck = []
 
# Loop for every type of suit
for suit in suits:
 
# Loop for every type of card in a suit
    for card in cards:
 
    # Adding card to the deck
        deck.append(Card(suits_values[suit], card))
    
    #After all the preparations are done, it is time to start the game.
hi_lo_game(deck)
            
