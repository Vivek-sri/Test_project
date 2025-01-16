import random
import pdb

suits = ("Hearts", "Diamonds", "Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# two_hearts = Card(suits[0], ranks[0])
# print(two_hearts)

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)
        return self.all_cards
    def deal(self):
        return self.all_cards.pop()

# my_deck = Deck()
# print(my_deck.shuffle())
# my_card = my_deck.deal()
# print(my_card)

class Player():

    def __init__(self,player_name):
        self.player_name = player_name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_card):

        if type(new_card) == type([]):
            self.all_cards.extend(new_card)

        else:
            self.all_cards.append(new_card)

    def __str__(self):
        return f"Player {self.player_name} has {len(self.all_cards)} cards"

# player = Player("Harry")
# print(player)
# player.add_card(two_hearts)
# print(player)
# player.add_card([two_hearts,two_hearts,two_hearts])
# print(player)


player_one = Player("Player One")
player_two = Player("Player Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.deal())
    player_two.add_card(new_deck.deal())

game_on = True
round_num=0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One has no cards")
        print("Player two wins")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two has no cards")
        print("Player ine wins")
        game_on = False
        break


    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            at_war = False

        else:
            print("WAR!!")

            if len(player_one.all_cards) < 5:
                print("Player one has lesss cards and is unable to play! Game Over at war")
                print("Player two wins and Player one loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two has lesss cards and is unable to play! Game Over at war")
                print("Player one wins and Player two loses!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())





