from a8alatr0clown.definitions import HandType, CardSuit, CardRank
from .playing_cards import Hand
from decimal import Decimal
from typing import Tuple
class HandSolver:
    def __init__(self):
        pass

    def compute_hand_score(self, hand: Hand) -> Tuple[Decimal, Decimal, Decimal]:
        """Compute the score of a hand

        Returns: (total score, chips count, mult factor)
        """
        raise NotImplementedError("implement compute_hand_score")

    def solve_hand_type(self, hand: Hand) -> HandType:
        """Identify the hand type of the given hand"""
        raise NotImplementedError("implement solve_hand_type")
    
    def hand_contains(self, hand: Hand, hand_type: HandType) -> bool:
        """Tells if a hand contains a given type"""
        raise NotImplementedError("implement hand_contains")
