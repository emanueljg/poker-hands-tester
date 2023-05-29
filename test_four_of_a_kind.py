from lib import *

class TestFourOfAKind:
    def test_simple(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, ACE),
            Card(SPADES, ACE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(SPADES, KING),
            Card(CLUBS, FOUR)
        )))        

        mk_tester(p, a, Hand.four_of_a_kind)

    # cannot check
    # def test_kicker(self):
    #     p = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(SPADES, KING),
    #         Card(CLUBS, FIVE)
    #     )))        

    #     a = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(SPADES, KING),
    #         Card(CLUBS, FOUR)
    #     )))        

    #     mk_tester(p, a, Hand.four_of_a_kind)

    # cannot check
    # def test_tie(self):
    #     p = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(SPADES, KING),
    #         Card(CLUBS, FIVE)
    #     )))        

    #     a = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(SPADES, KING),
    #         Card(HEARTS, KING),
    #         Card(SPADES, FIVE)
    #     )))        

    #     mk_tester(p, a, Hand.four_of_a_kind, check_for='tie')