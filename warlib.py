import random

suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

ranks = tuple(values.keys())


class Card:
    """
    Class to hold card objects.
    Cards should be comparable to other objects of this class.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class Deck:
    """
    Class to hold a collection of cards
    """

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        else:
            return None

    def __len__(self):
        return len(self.all_cards)

    def __str__(self):
        the_head = f"Deck with {len(self.all_cards)} cards: "
        all_strings = [str(cc) for cc in self.all_cards]
        the_tail = ", ".join(all_strings)
        return the_head + the_tail


class Player:
    """
    Class to hold a Player object
    """

    def __init__(self, name):
        self.name = name
        self.card_hand = []

    def play_card(self):
        return self.card_hand.pop(0)

    def add_cards(self, *new_cards):
        """
        Add new cards to the player's hand
        new_cards can either be a single Card object
        or a list of Card objects
        """
        for cards in new_cards:
            if type(cards) == type([]):
                self.card_hand.extend(cards)
            else:
                self.card_hand.append(cards)

    def cards_left(self):
        return len(self.card_hand)

    def __str__(self):
        return f"Player {self.name} has {len(self.card_hand)} cards."
