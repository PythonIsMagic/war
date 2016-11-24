#!/usr/bin/env python
"""
Creates a Deck of cards.
"""
import random
import card


class Deck(object):
    """ Creates a standard 52 card deck, with no Jokers. """
    def __init__(self):
        self.cards = [card.Card(r, s[0]) for s in card.SUITS for r in card.RANKS if r != 'Z']

    def __str__(self):
        """ Returns a string showing all the cards in the deck. """
        _str = ''
        for i, _card in enumerate(self.cards):
            if i % 13 == 0 and i != 0:
                _str += '\n'
            _str += '{} '.format(str(_card))
        return _str.strip()

    def __len__(self):
        """ Returns how many cards are in the Deck. """
        return len(self.cards)

    def __contains__(self, _card):
        """ Returns True if the given Card is in the deck, False otherwise. """
        return _card in self.cards

    def shuffle(self):
        """ Shuffles the deck of cards once."""
        random.shuffle(self.cards)

    def deal(self):
        """ Removes the top card off the deck and returns it. Raises an
            exception if the deck is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise Exception('Deck is empty, cannot deal cards!')


class Deck2Joker(Deck):
    """ Creates a deck with two Jokers. """
    def __init__(self):
        super(Deck2Joker, self).__init__()
        self.cards.append(card.JOKER1)
        self.cards.append(card.JOKER2)
