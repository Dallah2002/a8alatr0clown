# a8alatr0clown - a clone of Balatro for educational purposes

## Test Progression

### 1. **Basic hand types** (`test_basic_scoring.py`)
- **Purpose**: Validate the base scoring logic for all hand types (e.g., Pair, Flush, Straight Flush) **without** special card editions.
- **What You'll learn**:
  - How hand types are prioritized (e.g., a Flush House is both a Full House and a Flush).
  - Base chip and multiplier values for each hand type.
  - How card ranks contribute to the total chip score (e.g., Aces = 11 chips, Kings = 10 chips).
- **Key tests**:
  - `test_score_high_card`: Validates the default "high card" scoring.
  - `test_score_pair` to `test_score_flush_five`: Covers all hand types with basic cards.

### 2. **Special card editions** (`test_edition_scoring.py`)
- **Purpose**: Test interactions with special card editions (Foil, Holographic, Polychrome) and their **order-dependent effects**.
- **What you'll learn**:
  - How editions modify scores (e.g., Foil adds chips, Polychrome multiplies the multiplier).
  - Why card order matters (e.g., applying additive bonuses before multiplicative ones).
  - Edge cases where non-scoring cards are ignored.
- **Key tests**:
  - `test_holo_before_poly_non_commutative`: Demonstrates order dependency for additive vs. multiplicative effects.
  - `test_multiple_poly_flush_five`: Tests stacking multiplicative effects.
  - `test_foil_non_scoring_cards_ignored`: Ensures only scoring-group cards are evaluated.

---

## How to use

0. **Install pytest in your virtualenv**

(as we've already discussed)

1. **Run the basic tests first**:

```bash
   pytest -v a8alatr0clown/engine/test_scoring_basic.py
```

2. **Move on to the next ones**

Same thing, different files :)
