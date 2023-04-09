from lib import *

class TestThreeOfAKind:
    def test_simple(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, ACE),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.three_of_a_kind)

    def test_kicker(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, NINE),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.three_of_a_kind)
      
    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(SPADES, KING),
            Card(CLUBS, NINE),
            Card(SPADES, FIVE)
        )))        

        mk_tester(p, a, Hand.three_of_a_kind, check_for='tie')