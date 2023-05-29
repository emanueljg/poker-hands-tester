from lib import *

class TestFullHouse:

    def test_high_triplet(self):
        p = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, QUEEN),
            Card(HEARTS, QUEEN)
        )))        

        a = Hand(list((
            Card(CLUBS, JACK),
            Card(DIAMONDS, JACK),
            Card(HEARTS, JACK),
            Card(DIAMONDS, QUEEN),
            Card(SPADES, QUEEN)
        )))        

        mk_tester(p, a, Hand.full_house)

    # cannot check
    # def test_high_pair(self):
    #     p = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(CLUBS, QUEEN),
    #         Card(HEARTS, QUEEN)
    #     )))        

    #     a = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(CLUBS, JACK),
    #         Card(HEARTS, JACK)
    #     )))        

    #     mk_tester(p, a, Hand.full_house)

    def test_high_both(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, ACE),
            Card(CLUBS, THREE),
            Card(HEARTS, THREE)
        )))        

        a = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(CLUBS, TWO),
            Card(HEARTS, TWO)
        )))        

        mk_tester(p, a, Hand.full_house)

    # can't occur due to triple
    # def test_tie(self):
    #     p = Hand(list((
    #         Card(CLUBS, ACE),
    #         Card(DIAMONDS, ACE),
    #         Card(HEARTS, ACE),
    #         Card(CLUBS, THREE),
    #         Card(HEARTS, THREE)
    #     )))        

    #     a = Hand(list((
    #         Card(SPADES, ACE),
    #         Card(DIAMONDS, ACE),
    #         Card(HEARTS, ACE),
    #         Card(CLUBS, THREE),
    #         Card(DIAMONDS, THREE)
    #     )))        

    #     mk_tester(p, a, Hand.full_house, check_for='tie')
        
