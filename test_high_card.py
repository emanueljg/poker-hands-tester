from lib import *

class TestHighCard:
    def test_simple_kicker(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, SEVEN),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card)

    def test_simple_kicker(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, SEVEN),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card)

    def test_ace(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card)

    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card, check_for='tie')
