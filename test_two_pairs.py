from lib import *

class TestTwoPairs:
    def test_both_lower(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, QUEEN),
            Card(HEARTS, QUEEN),
            Card(DIAMONDS, JACK),
            Card(SPADES, JACK),
            Card(DIAMONDS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs)

    def test_one_lower(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, ACE),
            Card(HEARTS, ACE),
            Card(DIAMONDS, JACK),
            Card(SPADES, JACK),
            Card(DIAMONDS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs)
        
    def test_kicker(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, QUEEN),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(HEARTS, KING),
            Card(DIAMONDS, QUEEN),
            Card(SPADES, QUEEN),
            Card(DIAMONDS, FOUR)
        )))        

        mk_tester(p, a, Hand.two_pairs)

    def test_tie(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, QUEEN),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(SPADES, KING),
            Card(HEARTS, KING),
            Card(DIAMONDS, QUEEN),
            Card(SPADES, QUEEN),
            Card(DIAMONDS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs, check_for='tie')
       
