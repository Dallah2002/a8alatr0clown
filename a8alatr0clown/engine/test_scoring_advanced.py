from a8alatr0clown.definitions.modifiers import CardEdition
from .handsolver import HandSolver
from .playing_cards import Hand, Card, CardRank, CardSuit

DIAMOND = CardSuit.DIAMOND
HEART = CardSuit.HEART
SPADE = CardSuit.SPADE
CLUB = CardSuit.CLUB


ACE = CardRank.ACE
TWO = CardRank.TWO
THREE = CardRank.THREE
FOUR = CardRank.FOUR
FIVE = CardRank.FIVE
SIX = CardRank.SIX
SEVEN = CardRank.SEVEN
EIGHT = CardRank.EIGHT
NINE = CardRank.NINE
TEN = CardRank.TEN
JACK = CardRank.JACK
QUEEN = CardRank.QUEEN
KING = CardRank.KING
BASIC = CardEdition.BASIC
HOLO = CardEdition.HOLOGRAPHIC
FOIL = CardEdition.FOIL
POLY = CardEdition.POLYCHROME


def _generate_card_fixtures() -> dict:
    return {
        # Foil, Holographic, and Polychrome cards
        "AF": Card(CLUB, ACE, FOIL),
        "AH": Card(CLUB, ACE, HOLO),
        "AP": Card(CLUB, ACE, POLY),
        "KF": Card(HEART, KING, FOIL),
        "QH": Card(HEART, QUEEN, HOLO),
        "JP": Card(HEART, JACK, POLY),
        "TF": Card(DIAMOND, TEN, FOIL),
        "2H": Card(CLUB, TWO, HOLO),
        "3P": Card(CLUB, THREE, POLY),
        "AP2": Card(CLUB, ACE, POLY),  # Additional Polychrome Ace
        "AP3": Card(CLUB, ACE, POLY),
        "AP4": Card(CLUB, ACE, POLY),
        "AP5": Card(CLUB, ACE, POLY),
        "7D": Card(DIAMOND, SEVEN, BASIC),
        "8D": Card(DIAMOND, EIGHT, BASIC),
        "9D": Card(DIAMOND, NINE, BASIC),
        "TD": Card(DIAMOND, TEN, FOIL),
        "JD": Card(DIAMOND, JACK, HOLO),
    }


def test_holo_before_poly_non_commutative():
    """Holo adds 10 mult first, then Poly multiplies: (2 +10) *1.5 =18 mult"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AH"], c["AP"], c["KF"], c["QH"], c["JP"]])  # Pair of Aces
    assert hs.compute_hand_score(hand) == (32 * 18, 32, 18)


def test_poly_before_holo_non_commutative():
    """Poly multiplies first (2*1.5=3), then Holo adds 10: 3 +10 =13 mult"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AP"], c["AH"], c["KF"], c["QH"], c["JP"]])  # Pair of Aces
    assert hs.compute_hand_score(hand) == (32 * 13, 32, 13)


def test_foil_and_poly_pair():
    """Foil adds 50 chips to first Ace, Poly multiplies mult by 1.5"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AF"], c["AP"], c["KF"], c["QH"], c["JP"]])  # Pair of Aces
    # Base Pair: 10 +11*2 =32. Foil adds 50 →82. Poly → mult 2*1.5=3
    assert hs.compute_hand_score(hand) == (82 * 3, 82, 3)


def test_multiple_poly_flush_five():
    """Five Polychrome Aces: mult =16 * (1.5)^5 =121.5"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AP"], c["AP2"], c["AP3"], c["AP4"], c["AP5"]])  # Flush Five
    # Base:160 +11*5=215 chips. Mult:16 *1.5^5=121.5
    assert hs.compute_hand_score(hand) == (215 * 121.5, 215, 121.5)


def test_foil_non_scoring_cards_ignored():
    """Foil cards not part of the Pair should be ignored"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AH"], c["AH"], c["KF"], c["QH"], c["TF"]])  # Pair of Aces
    # Base Pair:10 +11*2=32. Holo adds 10*2=20 mult (but wait: only two Aces are in the Pair)
    # Hand is Pair (AH, AH). Each AH is HOLO.
    # Base:10 chips. Each AH adds 11 chips (total 22) →32 chips.
    # Each HOLO adds 10 mult → mult starts at 2. After first AH: mult=2+10=12. Second AH: mult=12+10=22.
    # Total:32 *22=704.
    # First AH: chips=10+11=21, mult=2+10=12.
    # Second AH: chips=21+11=32, mult=12+10=22.
    # total score 32 *22=704.
    assert hs.compute_hand_score(hand) == (704, 32, 22)


def test_mixed_editions_straight_flush():
    """Straight Flush with Holographic and Foil cards in scoring group"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    # Straight Flush: 7D,8D,9D,TD,JD (all Diamonds). Assume TD is FOIL, JD is HOLO.

    hand = Hand([c["7D"], c["8D"], c["9D"], c["TD"], c["JD"]])
    # Base Straight Flush:100 chips, 8 mult.
    # Chips:100 +7+8+9+10+10=144. TD is Foil (adds 50). JD is Holo (adds 10 mult).
    # Straight Flush uses all 5 cards. So each card contributes:
    # 7 (7D), 8 (8D), 9 (9D), 10+50 (TD), 10 (JD). Total chips:100 +7+8+9+60+10=194.
    # Mult:8 (base) +10 (Holo on JD) =18.
    # Total score:194 *18=3492.
    assert hs.compute_hand_score(hand) == (194 * 18, 194, 18)


def test_high_card_with_editions():
    """High Card (Ace) with Foil and Polychrome editions"""
    c = _generate_card_fixtures()
    hs = HandSolver()
    hand = Hand([c["AF"], c["2H"], c["3P"], c["KF"], c["QH"]])  # High Card Ace (AF)
    # Total:66 *1=66.
    assert hs.compute_hand_score(hand) == (66, 66, 1)
