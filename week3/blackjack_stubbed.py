'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Tips:
1) Aces can count as an eleven or a one - but it only counts as a one if your score is over 21
2) Research random.shuffle()
3) You are not allowed to code until you design your program!
4) Optional: Research __radd__ - it is a built-in method in Python

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''


import random



suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

class Card:
    def __init__(self,suit,rank):
        pass

    def __str__(self):
        "Optional to fill out"
        pass

    def __repr__(self):
        "optional to fille out"

    def __radd__(self,other):
        pass
        
    def value(self):
        pass


class Deck:
    def __init__(self):
        pass

    def shuffle(self):
        pass

    def one(self):
        "get one card"
        pass


class Player:
    def __init__(self,name):
        pass

    def __str__(self):
        "optional"
        pass

    def __lt__(self,other):
        pass
    
    def get(self,card):
        "adds a card to the users hand"
        pass

    def choose(self):
        "ui, ask user to hit or stand"

    def hand(self):
        "calculate the number value of the users hand"
        pass
    
    def bust(self):
        "did the user bust"

    def won(self):
        "do they have 21"
        pass


class Dealer(Player):
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        "optional"
        pass

    def choose(self):
        "computer logic to decide to hit or stay"
        pass
    
class Game:
    def __init__(self):
        "Game setup, adds players and a dealer"
        pass
    
    def print_table(self,player):
        "helper method to print out all the players hands"
        pass
    
    def deal(self):
        "deal to all players"
        pass

    def play(self):
        "top level, manages the game"
        pass




    
