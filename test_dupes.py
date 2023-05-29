from lib import *
from pytest import raises

def test_no_hand_dupe():
    try:
        Hand(list((
            # not identical value...
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(SPADES, KING),
            # nor identical suit...
            Card(HEARTS, KING),
            Card(HEARTS, THREE)
        )))
    except DuplicateCardsException:
        assert False

def test_hand_dupe():
    with raises(DuplicateCardsException):
        Hand(list((
            Card(HEARTS, KING),  # DUPE
            Card(DIAMONDS, FOUR),
            Card(HEARTS, KING),  # DUPE
            Card(CLUBS, KING),
            Card(HEARTS, FIVE)
        )))

def test_judge_dupe():
    p = Hand([
      Card(HEARTS, KING),
      Card(CLUBS, FIVE),  # DUPE
      Card(DIAMONDS, FOUR),
      Card(SPADES, FIVE),
      Card(HEARTS, FOUR)
    ])

    a = Hand([
      Card(CLUBS, FIVE),  # DUPE
      Card(SPADES, FOUR),
      Card(SPADES, QUEEN),
      Card(HEARTS, THREE),
      Card(SPADES, TWO)  
    ])

    with raises(DuplicateCardsException):
        Judge.judge(p, a)
