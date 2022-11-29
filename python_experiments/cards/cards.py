# some exercises about a deck of cards
import random


class Card:
    """class representing a card of a deck"""

    def __init__(self, number, suit):
        """initialise card object"""
        # define the lists needed
        suits_p = ('spade', 'coppe', 'denari', 'bastoni')
        numbers_p = (range(1, 11))
        self.number = number
        self.suit = suit
        if self.suit not in suits_p:
            raise ValueError("Il seme non è valido!")
        if self.number not in numbers_p:
            raise ValueError("Il seme non è valido!")

    def get_n(self):
        return self.number

    def get_s(self):
        return self.suit

    def __str__(self):
        """describes better the card"""
        return f'Questa carta è un {self.get_n()} di {self.get_s()}'


def think_random_card():
    """generate a random card"""
    return Card(random.choice(range(1, 11)), random.choice(('spade', 'coppe', 'denari', 'bastoni')))


class Deck:
    """a class representing a deck"""

    def __init__(self, cards_deck=None):
        """initialise deck attributes"""
        if cards_deck is None:
            cards_deck = []
        self.cards_deck = cards_deck
        self.removed = []

    def g_cards(self):
        return self.cards_deck

    def r_next_card(self, n=1):
        for _ in range(n):
            to_rem = self.cards_deck.pop(0)
            self.removed.append(to_rem)

    def reinstate(self):
        while self.removed:
            self.cards_deck.append(self.removed.pop(0))

    def g_removed(self):
        return self.removed

    def g_len(self):
        return len(self.g_cards())

    def __str__(self):
        """better describe the deck"""
        return f'Questo mazzo ha {self.g_len()} carte.'

    def g_remaining(self, n):
        """Returns the remaining cards for the specified number"""
        return len([card for card in self.g_cards() if card.get_n() == n])

    def shuffle_deck(self):
        """shuffle the deck"""
        print('Il mazzo è stato mischiato.')
        random.shuffle(self.cards_deck)

    def see_cards(self):
        """look at all the cards of the deck"""
        for card in self.g_cards():
            print(card)

    def first_last(self):
        """puts the first card in the end"""
        add = self.cards_deck.pop(0)
        print("Adesso la prima carta è l'ultima!")
        return self.cards_deck.append(add)

    def first_or_last_x_cards(self, x=1, last=False):
        """look at the first X card in the deck"""
        if not last:
            for a in range(x):
                print(self.g_cards()[a])
        else:
            for a in range(-1, -x - 1, -1):
                print(self.g_cards()[a])

    def split_deck(self):
        """divides the deck almost in half and put one half on the other"""
        j = random.randrange(14, 26)
        first_part = self.cards_deck[:j]
        second_part = self.cards_deck[j:]
        print("Il mazzo è stato splittato.")
        self.cards_deck = second_part + first_part
        return self.cards_deck

    def prob_n(self, n):
        """returns probability of card with n number"""
        return round(self.g_remaining(n) / self.g_len(), 2)

    def prob(self, group=True):
        """returns a dictionary with all probabilities, grouped by number or percentage"""
        p = {e: self.prob_n(e) for e in {k.get_n() for k in self.g_cards()}}
        return {e: [key for key in p if p[key] == e] for e in p.values()} if group else p


def create_new_deck():
    """create a new deck"""
    suits = ('spade', 'coppe', 'denari', 'bastoni')
    numbers = (range(1, 11))
    new_deck = Deck()
    new_deck.cards_deck = [Card(number, suit) for number in numbers for suit in suits]
    return new_deck


class Table:
    """a class representing the table"""

    def __init__(self, cards_table=None):
        """initialise table attributes"""
        if cards_table is None:
            cards_table = []
        self.cards_table = cards_table


class Player:
    """a class representing the player"""

    def __init__(self, cards_player=None):
        """initialise player attributes"""
        if cards_player is None:
            cards_player = []
        self.cards_player = cards_player


d = create_new_deck()
d.shuffle_deck()