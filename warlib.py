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


class CardCollection:
    """
    A class to hold a collection of cards.
    """

    def __init__(self, *cards_init):
        self.cards = []
        for cards in cards_init:
            if type(cards) is list:
                self.cards.extend(cards)
            elif type(cards) is Card:
                self.cards.append(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_last(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def get_first(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

    def add_cards(self, *new_cards):
        """
        Add new cards to the collection.
        new_cards can either be a single Card object
        or a list of Card objects
        """
        for cards in new_cards:
            if type(cards) is list:
                self.cards.extend(cards)
            elif type(cards) is Card:
                self.cards.append(cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        all_strings = [str(cc) for cc in self.cards]
        return ", ".join(all_strings)

    def __getitem__(self, item):
        return self.cards[item]

    def __iter__(self):
        return (card for card in self.cards)


class Deck(CardCollection):
    """
    Class to hold a collection of cards
    """

    def __init__(self):
        # self.cards = []
        super().__init__()
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def deal_one(self):
        return super().get_last()

    def __str__(self):
        the_head = f"Deck with {len(self.cards)} cards: "
        return the_head + super().__str__()


class Player:
    """
    Class to hold a Player object
    """

    def __init__(self, name):
        self.name = name
        # self.card_hand = []
        self.card_hand = CardCollection()

    def play_card(self):
        # return self.card_hand.pop(0)
        return self.card_hand.get_first()

    def add_cards(self, *new_cards):
        """
        Add new cards to the player's hand
        new_cards can either be a single Card object
        or a list of Card objects
        """
        self.card_hand.add_cards(*new_cards)

    def cards_left(self):
        return len(self.card_hand)

    def __str__(self):
        the_head = f"Player {self.name} has {len(self.card_hand)} cards"
        the_middle = ": " if len(self.card_hand) > 0 else "."
        the_tail = str(self.card_hand)
        return the_head + the_middle + the_tail
