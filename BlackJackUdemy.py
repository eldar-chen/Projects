import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0 # start with 0 value
        self.aces = 0 # add an attribute to keep track of aces

    def add_card(self,card):
        # card passed in from class Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]
            # Track Aces
        if card.rank == 'Ace':
            self.aces += 1
        
        
    def adjust_for_ace(self):
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    
    def __init__(self, total = 100):
        self.total = total # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break


def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop

    while True:
        x = input("Hit or stand? Enter H or S")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter H or S")
            continue

        break


def show_some(player, dealer):
    
    # Show only ONE of the dealers cards
    # dealer.cards[0] = hidden
    print("\n Dealer's Hand: ")
    print("First card Hidden!")
    print(dealer.cards[1])
    # Show all (2 cards) of the players cards
    print("\n Players Hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    # Show all the dealers cards
    # print("\n Dealers Hand:")
    # for card in dealer.cards:
    #     print(card)
    print("\n Dealers Hand: ",*dealer.cards,sep='\n') # replaces the for loop

    # calculate and display the value (e.g: J + K == 20)
    print(f"Value of dealers hand is: {dealer.value}")

    # show all the players cards
    print("Players Hand: ",*player.cards,sep='\n')
    print(f"Value of Players hand is: {player.value}")


def player_busts(player,dealer,chips):
    print("BUST PLAYER!\n")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!\n")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("PLAYER WINS!, DEALER BUSTED!\n")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS! BUST PLAYER!\n")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie! PUSH\n")


while True:
    print("Welcome to Blackjack\n")
    # Create & Shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up players chips
    player_chips = Chips()


    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for player to hit or stand
        hit_or_stand(deck, player_hand)
        #Sgiw cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If players hand exceeds 21, run player_bust() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If the player hasn't busted, play Dealers hand until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_bust(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        
        # Inform player of their chips total
        print(f"\n Player total chips are at: {player_chips.total}")

        # Ask to play again
        new_game = input("Would you like to play another hand? y/n")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break


