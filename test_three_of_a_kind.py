from lib import *

class TestThreeOfAKind:
    def test_simple(self):
        p = Hand(list((
            Card(CLUBS, ACE),
            Card(DIAMONDS, ACE),
            Card(HEARTS, ACE),
            Card(CLUBS, NINE),
            Card(CLUBS, FIVE)
        )))        

        a = Hand(list((
            Card(CLUBS, KING),
            Card(DIAMONDS, KING),
            Card(HEARTS, KING),
            Card(SPADES, NINE),
            Card(SPADES, FOUR)
        )))        

        mk_tester(p, a, Hand.three_of_a_kind)

    # cannot check without dupes
    # def test_kicker(self):
    #     p = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(CLUBS, NINE),
    #         Card(CLUBS, FIVE)
    #     )))        

    #     a = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(CLUBS, NINE),
    #         Card(CLUBS, FOUR)
    #     )))        

    #     mk_tester(p, a, Hand.three_of_a_kind)
      
    # there is no way to have a tie of a 3-in-a-row
    # without introducing a duplicate card.
    # def test_tie(self):
    #     p = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(HEARTS, KING),
    #         Card(CLUBS, NINE),
    #         Card(CLUBS, FIVE)
    #     )))        

    #     a = Hand(list((
    #         Card(CLUBS, KING),
    #         Card(DIAMONDS, KING),
    #         Card(SPADES, KING),
    #         Card(CLUBS, NINE),
    #         Card(SPADES, FIVE)
    #     )))        

    #     mk_tester(p, a, Hand.three_of_a_kind, check_for='tie')