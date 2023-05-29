from lib import *

class TestOnePair:
    def test_simple(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, QUEEN),
            Card(HEARTS, QUEEN),
            Card(SPADES, EIGHT),
            Card(SPADES, NINE),
            Card(SPADES, FIVE)
        )))        

        mk_tester(p, a, Hand.one_pair)

    def test_kicker(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(HEARTS, QUEEN),
            Card(SPADES, QUEEN),
            Card(SPADES, EIGHT),
            Card(SPADES, NINE),
            Card(SPADES, FOUR)
        )))        

        mk_tester(p, a, Hand.one_pair)

    def test_ace(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(DIAMONDS, KING),
            Card(SPADES, EIGHT),
            Card(SPADES, NINE),
            Card(SPADES, FOUR)
        )))        

        mk_tester(p, a, Hand.one_pair)
        
    def test_tie(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(HEARTS, KING),
            Card(SPADES, EIGHT),
            Card(HEARTS, NINE),
            Card(HEARTS, FIVE)
        )))        

        mk_tester(p, a, Hand.one_pair, check_for='tie')