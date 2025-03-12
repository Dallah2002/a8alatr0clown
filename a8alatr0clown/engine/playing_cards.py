from __future__ import annotations
from dataclasses import dataclass
from typing import List
from functools import total_ordering
from a8alatr0clown.definitions import CardRank, CardSuit, CardEdition


@total_ordering
@dataclass
class Card:
    """A playing card.

    Cards are sorted by suit, then rank, then edition"""

    suit: CardSuit
    rank: CardRank
    edition: CardEdition

    def _is_card(self, other):
        return (
            hasattr(other, "suit")
            and hasattr(other, "rank")
            and hasattr(other, "edition")
        )

    def __eq__(self, other):
        return self._is_card(other) and (self.suit, self.rank, self.edition) == (
            other.suit,
            other.rank,
            other.edition,
        )

    def __hash__(self):
        return hash(f"S{self.suit}\0R{self.rank}\0E{self.edition}")

    def __lt__(self, other):
        """Cards are sorted by suit, then rank, then edition"""

    def __str__(self):
        return f"""[{self.suit}{self.rank}] """


@dataclass
class Hand:
    """A playing hand"""

    cards: List[Card]

    def __len__(self):
        return len(self.cards)


@dataclass
class Collection:
    """The collection of cards possessed by the player"""

    cards: List[Card]

    def add_card(self, card: Card):
        """Add a card to the collection"""
        raise NotImplementedError("implement Collection.add_card")

    def remove_card(self, card: Card):
        """remove one instance of the given card from the collection."""
        raise NotImplementedError("implement Collection.remove_card")

    def create_shuffled_deck(self) -> Deck:
        """Return a shuffled deck from the collection of cards

        So that they are mixed!"""
        raise NotImplementedError("Implement create_shuffled_deck")


@dataclass
class Deck:
    """The shuffled deck of the player"""

    cards: List[Card]

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        s = f"Deck of {len(self)} cards: "
        for c in self.cards:
            s += str(c)
        return s


@dataclass
class Discarded:
    """The discarded cards, in order of discard"""

    cards: List[Card]


@dataclass
class PlayingTable:
    deck: Deck
    discarded: Discarded
    hand: Hand


__all__ = ["PlayingTable", "Discarded", "Deck", "Collection", "Hand"]
