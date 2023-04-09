from lib import *

class TestFlush:
    def test_flush(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(CLUBS, QUEEN),
            Card(CLUBS, JACK),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.flush)
        
    def test_tie(self):
        p = Hand(set((
            Card(DIAMONDS, KING),
            Card(DIAMONDS, QUEEN),
            Card(DIAMONDS, EIGHT),
            Card(DIAMONDS, NINE),
            Card(DIAMONDS, FIVE)
        )))        

        a = Hand(set((
            Card(HEARTS, KING),
            Card(HEARTS, QUEEN),
            Card(HEARTS, EIGHT),
            Card(HEARTS, NINE),
            Card(HEARTS, FIVE)
        )))        

        mk_tester(p, a, Hand.flush, check_for='tie')