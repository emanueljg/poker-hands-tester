from lib import *

class TestTwoPairs:
    def test_both_lower(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, QUEEN),
            Card(DIAMONDS, QUEEN),
            Card(HEARTS, JACK),
            Card(CLUBS, JACK),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs)

    def test_one_lower(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, JACK),
            Card(CLUBS, JACK),
            Card(CLUBS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs)
        
    def test_kicker(self):
        p = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, KING),
            Card(CLUBS, KING),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.two_pairs)

    def test_tie(self):
        p = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, QUEEN),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(set((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, QUEEN),
            Card(CLUBS, QUEEN),
            Card(DIAMONDS, FIVE)
        )))        

        mk_tester(p, a, Hand.two_pairs, check_for='tie')
       
