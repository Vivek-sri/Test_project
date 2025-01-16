import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    '''This class represents an individual card with
        its suit and rank and provides a readable format when printed'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):      # String representation of a card
        return self.rank + ' of ' + self.suit

class Deck:
    '''This class represents the entire deck and involves the dealing and shuffling of the cards'''

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):



        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: '+deck_comp

    def shuffle(self): # shuffling using the random module
        random.shuffle(self.deck)

    def deal(self): # Dealing the cards i.e remove and return the last card from the deck randomly
        single_card = self.deck.pop()
        return single_card


class Hand:

    '''Keeping track of aces is essential for this game.
    The Hand class tracks the player's (or dealer's) cards, calculates the total value, and adjusts for Aces as needed'''


    def __init__(self):
         self.cards = []    # Initialize a hand with an empty list of cards, value = 0, and 0 Aces
         self.value = 0
         self.aces = 0      # Count the number of Aces (since Aces can have special rules)

    def add_card(self,card):   # Add a card to the hand
        self.cards.append(card)
        self.value += values[card.rank]     # Used to update the Hand's total value using the card's rank
        if card.rank == 'Ace' : # Check if the card is an ace
            self.aces += 1  # Update the counter by one

    def adjust_for_ace(self):
        while self.value > 21 and self.aces :       # Only adjust if the value exceeds 21 and there are Aces
            self.value -= 10    # Count the Ace as 1 instead of 11
            self.aces -= 1      # Reduce the Ace counter


class Chips:

    '''Chips are what we use to bet in this game... A fixed amount of chips will be given in the start
        using which all the betings will take place. The chip count will increase or decrease based on
        winning and losing respectively'''

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    '''This function basically prompts the player tp place a bet and ensures that the i/p is valid and the bet places is within
    the player's total number of chips by using exception handling and if else statements'''


    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())  # Adds a card to the hand            add_card method from the Hand class
    hand.adjust_for_ace()       # Adjusts for aces if necessary      adjust_for_ace method from the hand class


def hit_or_stand(deck, hand):

    '''hit means to take another card and stand means ending their turn'''


    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':     # using the input sting to understand if the player wants to hit or stand
            hit(deck, hand)  # hit() function defined above is used to hit

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):  # Displays the players cards and one dealer card and hides the oteher
    print("\nDealer's Hand:")   # displays the text inside the double quotes and the \n is to display the next text in the next line
    print(" <card hidden>")     # displays the text inside the double quotes
    print('', dealer.cards[1])  # displays one of the dealers cards
    print("\nPlayer's Hand:", *player.cards, sep='\n ') # displays the text inside the quotes and then in the next two lines displayes the player cards


def show_all(player, dealer):   # Reveals both hands and their values
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

''' bust is to exceed the total of 21 which means loss as the motive of the game is to keep the total below 21
while push means tied total for dealer and the player... The following function handles those scenarios and correspondingly 
adjusts the chip count based on win and loss'''

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

            # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break