from lib import *

class TestStraight:
    def test_simple(self):
        p = Hand(set((
            Card(CLUBS, THREE),
            Card(DIAMONDS, FOUR),
            Card(HEARTS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(set((
            Card(CLUBS, TWO),
            Card(DIAMONDS, THREE),
            Card(HEARTS, FOUR),
            Card(CLUBS, FIVE),
            Card(CLUBS, SIX)
        )))        

        mk_tester(p, a, Hand.straight)

    def test_ace(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, QUEEN),
            Card(HEARTS, JACK),
            Card(CLUBS, TEN),
            Card(CLUBS, NINE)
        )))        

        mk_tester(p, a, Hand.straight)

    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, THREE),
            Card(DIAMONDS, FOUR),
            Card(HEARTS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(set((
            Card(CLUBS, THREE),
            Card(DIAMONDS, FOUR),
            Card(HEARTS, FIVE),
            Card(CLUBS, SIX),
            Card(DIAMONDS, SEVEN)
        )))        

        mk_tester(p, a, Hand.straight, check_for='tie')
