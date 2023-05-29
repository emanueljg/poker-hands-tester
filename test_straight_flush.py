from lib import *

class TestStraightFlush:
    def test_simple(self):
        p = Hand(list((
            Card(CLUBS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(list((
            Card(SPADES, TWO),
            Card(SPADES, THREE),
            Card(SPADES, FOUR),
            Card(SPADES, FIVE),
            Card(SPADES, SIX)
        )))        

        mk_tester(p, a, Hand.straight_flush)

    def test_ace(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(CLUBS, KING),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN)
        )))        

        a = Hand(list((
            Card(DIAMONDS, KING),
            Card(DIAMONDS, QUEEN),
            Card(DIAMONDS, JACK),
            Card(DIAMONDS, TEN),
            Card(DIAMONDS, NINE)
        )))        

        mk_tester(p, a, Hand.straight_flush)

    def test_tie(self):
        p = Hand(list((
            Card(CLUBS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(list((
            Card(HEARTS, THREE),
            Card(HEARTS, FOUR),
            Card(HEARTS, FIVE),
            Card(HEARTS, SIX),
            Card(HEARTS, SEVEN)
        )))        

        mk_tester(p, a, Hand.straight_flush, check_for='tie')
