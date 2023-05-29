from lib import *

class TestFlush:
    def test_flush(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        a = Hand(list((
            Card(DIAMONDS, KING),
            Card(DIAMONDS, QUEEN),
            Card(DIAMONDS, JACK),
            Card(DIAMONDS, NINE),
            Card(DIAMONDS, FOUR)
        )))        

        mk_tester(p, a, Hand.flush)
        
    def test_tie(self):
        p = Hand(list((
            Card(DIAMONDS, KING),
            Card(DIAMONDS, QUEEN),
            Card(DIAMONDS, EIGHT),
            Card(DIAMONDS, NINE),
            Card(DIAMONDS, FIVE)
        )))        

        a = Hand(list((
            Card(HEARTS, KING),
            Card(HEARTS, QUEEN),
            Card(HEARTS, EIGHT),
            Card(HEARTS, NINE),
            Card(HEARTS, FIVE)
        )))        

        mk_tester(p, a, Hand.flush, check_for='tie')