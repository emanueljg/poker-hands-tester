from lib import *

class TestHighCard:
    def test_simple_kicker(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(HEARTS, KING),
            Card(CLUBS, TEN),
            Card(DIAMONDS, SEVEN),
            Card(HEARTS, NINE),
            Card(HEARTS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card)

    def test_ace(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(SPADES, TEN),
            Card(SPADES, EIGHT),
            Card(SPADES, NINE),
            Card(DIAMONDS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card)

    def test_tie(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, TEN),
            Card(HEARTS, EIGHT),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(SPADES, TEN),
            Card(SPADES, EIGHT),
            Card(SPADES, NINE),
            Card(HEARTS, FIVE)
        )))        

        mk_tester(p, a, Hand.high_card, check_for='tie')
