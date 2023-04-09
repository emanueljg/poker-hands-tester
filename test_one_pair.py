from lib import *

class TestOnePair:
    def test_simple(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, QUEEN),
            Card(DIAMONDS, QUEEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.one_pair)

    def test_kicker(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, QUEEN),
            Card(DIAMONDS, QUEEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.one_pair)

    def test_ace(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.one_pair)
        
    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.one_pair, check_for='tie')