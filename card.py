""" Manages the components of a Card object. """

# Use tuples instead of lists
SUITS = ('c', 'd', 'h', 's')
FACECARDS = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'Z': 15}
RANKS = dict({str(x): x for x in range(2, 10)}, **FACECARDS)
HIDDEN = 'Xx'


class Card(object):
    """ Defines a standard playing card. """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit.lower()
        self.hidden = True  # Hide cards by default

    def __str__(self):
        """
        Returns the colored string representation
        """
        if self.hidden:
            return HIDDEN
        else:
            return self.rank + self.suit

    def __eq__(self, other):
        """
        Returns True if this card is equal to the other card, False otherwise.
        """
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        """
        Returns True if this card's rank is greater than the other card, False otherwise.
        """
        return RANKS[self.rank] > RANKS[other.rank]

    def __lt__(self, other):
        """
        Returns True if this card's rank is lesser than the other card, False otherwise.
        """
        return RANKS[self.rank] < RANKS[other.rank]

    def val(self):
        """
        Returns the value of the Cards rank.
        """
        return RANKS[self.rank]

    def peek(self):
        """
        This is how human/hero's are able to view hidden cards.
        """
        return self.rank + self.suit


# Define the Joker cards
JOKER1 = Card('Z', 's')
JOKER2 = Card('Z', 'c')
