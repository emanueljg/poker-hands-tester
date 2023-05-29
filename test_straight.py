from lib import *

class TestStraight:
    def test_simple(self):
        p = Hand(list((
            Card(CLUBS, THREE),
            Card(DIAMONDS, FOUR),
            Card(HEARTS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(list((
            Card(HEARTS, TWO),
            Card(DIAMONDS, THREE),
            Card(HEARTS, FOUR),
            Card(CLUBS, FIVE),
            Card(HEARTS, SIX)
        )))        

        mk_tester(p, a, Hand.straight)

    def test_ace_high(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN)
        )))        

        a = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, QUEEN),
            Card(HEARTS, JACK),
            Card(HEARTS, TEN),
            Card(CLUBS, NINE)
        )))        

        mk_tester(p, a, Hand.straight)

    def test_ace_low(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, TEN)
        )))        

        a = Hand(list((
            Card(DIAMONDS, ACE),
            Card(DIAMONDS, TWO),
            Card(HEARTS, THREE),
            Card(CLUBS, FOUR),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.straight)

    def test_tie(self):
        p = Hand(list((
            Card(CLUBS, THREE),
            Card(DIAMONDS, FOUR),
            Card(HEARTS, FIVE),
            Card(CLUBS, SIX),
            Card(CLUBS, SEVEN)
        )))        

        a = Hand(list((
            Card(HEARTS, THREE),
            Card(CLUBS, FOUR),
            Card(DIAMONDS, FIVE),
            Card(HEARTS, SIX),
            Card(DIAMONDS, SEVEN)
        )))        

        mk_tester(p, a, Hand.straight, check_for='tie')
