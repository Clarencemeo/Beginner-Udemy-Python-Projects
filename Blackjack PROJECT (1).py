#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return ("{} of {}".format(self.rank,self.suit))

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        for x in self.deck:
            print (x)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        pass
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        
    def adjust_for_ace(self):
        if (self.value>21):
            for x in self.cards:
                if (x.rank == "Ace"):
                    self.value-=10 
                    break
                
    def add_card(self,card):
        self.value = 0
        self.cards.append(card)
        for x in self.cards:
            self.value += values[x.rank]
        self.adjust_for_ace()
        
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet
    
    def set_bet(self, setBet): #mutator method
        self.bet = setBet

def take_bet(chipper):    
    while True:
        try:
            bett = int(input("How much would you like to bet?"))

        except:
            print("Please enter a valid integer!")
            continue
        else:
            if (bett > chipper.total):
                print ("You cannot bet more chips than you already possess!")
                continue
            break
            
    return bett


def hit(decker,hand):
    hand.add_card(decker.deck.pop(0))

def hit_or_stand(decker,hand):
    global playing  # to control an upcoming while loop

    while True:
        hitOrstand = input("\nWould you like to Hit or Stand?").title()
        if (hitOrstand == "Hit"):
            hit(decker,hand)
            break
        else:    
            if (hitOrstand == "Stand"):
                break
            else:
                print("Please enter either Hit or Stand.")
                continue
        break

def show_some(player,dealer):
    print("\nThe dealers hand is: ") 
    for x in dealer.cards[1:]:
        print(dealer.cards[dealer.cards.index(x)].__str__())
    print("There is also a flipped over card in the dealer's hand!")
    print("\nThe players hand is: ")
    for x in player.cards:
        print(player.cards[player.cards.index(x)].__str__())
    

    
def show_all(player,dealer):
    print("\nThe dealers hand is: ") 
    for x in dealer.cards:
        print(dealer.cards[dealer.cards.index(x)].__str__())
    print("\nThe total value of the dealer's hand is " + str(dealer.value))
    print("\nThe players hand is: ")
    for x in player.cards:
        print(player.cards[player.cards.index(x)].__str__())
    print("\nThe total value of the players's hand is " + str(player.value))

def player_busts(player, chipsToChange):
    if (player.value > 21): 
        print("\nThe player has BUSTED!")
        chipsToChange.lose_bet()
        
def player_wins(player, dealer, chipsToChange):
    if (player.value > dealer.value and player.value<=21):
        print("\nPlayer has a higher value! Player wins!")
        chipsToChange.win_bet()

def dealer_busts(dealer,chipsToChange):
    if (dealer.value > 21): 
        print("\nThe dealer has BUSTED!")
        chipsToChange.win_bet()
    
def dealer_wins(player, dealer,chipsToChange):
    if (player.value < dealer.value and dealer.value<=21):
        print("\nDealer has a higher value! Dealer wins!")
        chipsToChange.lose_bet()
    
def push(player, dealer):
    if (player.value == dealer.value):
        print("\nYou have equal values! Nobody won or lost.")
        
yourChips = Chips() # place this up here so it doesnt reset on restarts 
while True:
    # Print an opening statement
    print("\nWelcome to Blackjack! Have fun! Remember, Aces count as either 1 or 11 depending on your situation.")

    # Create & shuffle the deck, deal two cards to each player
    playerHand = Hand()
    dealerHand = Hand()
    officialDeck = Deck()
    officialDeck.shuffle()
    playerHand.add_card(officialDeck.deck.pop(0)) ##Clarence note: must pop to take it off of deck
    playerHand.add_card(officialDeck.deck.pop(0))
    dealerHand.add_card(officialDeck.deck.pop(0))
    dealerHand.add_card(officialDeck.deck.pop(0))

    # Set up the Player's chips
    
    yourChips.set_bet(take_bet(yourChips)) 
    
    # Show cards (but keep one dealer card hidden)
    show_some(playerHand, dealerHand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        hit_or_stand(officialDeck, playerHand)
        # Prompt for Player to Hit or Stand
        
        
        # Show cards (but keep one dealer card hidden)
        #show_some(playerHand, dealerHand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if (playerHand.value > 21):
            show_some(playerHand, dealerHand)
            player_busts(playerHand, yourChips)
            break

        

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealerHand.value < 17:
            hit(officialDeck, dealerHand)
    
        # Show all cards
        show_all(playerHand, dealerHand)
        
        # Run different winning scenarios
        player_busts(playerHand, yourChips)
        if (dealerHand.value > 21):
            dealer_busts(dealerHand, yourChips)
            break
        if (playerHand.value > dealerHand.value):
            player_wins(playerHand, dealerHand, yourChips)
            break
        if (dealerHand.value > playerHand.value):
            dealer_wins(playerHand, dealerHand, yourChips)
            break
        if (dealerHand.value == playerHand.value):
            push(playerHand, dealerHand)
            break
    
    # Inform Player of their chips total 
    print("\nYour total chips now are: " + str(yourChips.total))
    
    # Ask to play again
    answer = input("Do you want to play again? Yes or No?")
    if (answer.title() == "Yes"):
        continue
    else:     
        break

