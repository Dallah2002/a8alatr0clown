from __future__ import annotations
from enum import IntEnum
class CardSuit(IntEnum):
    """The different card suits that exist"""
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4

    @property
    def symbol(self):
        if self == CardSuit.SPADE:
            return "♣"
        elif self == CardSuit.CLUB:
            return "♠"
        elif self == CardSuit.DIAMOND:
            return "♦"
        elif self == CardSuit.HEART:
            return "♥"
        
class CardRank(IntEnum):
    """The different ranks a card may have"""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    @property
    def symbol(self):
        if self == CardRank.ACE:
            return "A"
        elif self == CardRank.KING:
            return "K"
        elif self == CardRank.QUEEN:
            return "Q"
        elif self == CardRank.JACK:
            return "J"
        else:
            return str(self.value)
