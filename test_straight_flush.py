from lib import *

class TestStraightFlush:
    def test_simple(self):
        p = Hand(set((
            Card(CLUBS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(set((
            Card(CLUBS, TWO),
            Card(CLUBS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX)
        )))        

        mk_tester(p, a, Hand.straight_flush)

    def test_ace(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(CLUBS, KING),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN),
            Card(CLUBS, NINE)
        )))        

        mk_tester(p, a, Hand.straight_flush)

    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(set((
            Card(HEARTS, THREE),
            Card(HEARTS, FOUR),
            Card(HEARTS, FIVE),
            Card(HEARTS, SIX),
            Card(HEARTS, SEVEN)
        )))        

        mk_tester(p, a, Hand.straight_flush, check_for='tie')
