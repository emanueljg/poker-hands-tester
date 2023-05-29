from lib import *

hand1 = Hand(list((
    Card(HEARTS, KING),
    Card(DIAMONDS, QUEEN),
    Card(SPADES, SEVEN),
    Card(SPADES, FOUR),
    Card(HEARTS, THREE)
)))

hand1a = Hand(list((
    Card(HEARTS, KING),
    Card(CLUBS, QUEEN),
    Card(SPADES, SEVEN),
    Card(SPADES, FOUR),
    Card(HEARTS, TWO)
)))

hand2 = Hand(list((
    Card(SPADES, TEN),
    Card(HEARTS, TEN),
    Card(SPADES, EIGHT),
    Card(HEARTS, SEVEN),
    Card(CLUBS, FOUR)
)))

hand3 = Hand(list((
    Card(HEARTS, JACK),
    Card(SPADES, JACK),
    Card(CLUBS, THREE),
    Card(SPADES, THREE),
    Card(HEARTS, TWO)
)))

hand4 = Hand(list((
    Card(CLUBS, QUEEN),
    Card(SPADES, QUEEN),
    Card(HEARTS, QUEEN),
    Card(HEARTS, NINE),
    Card(SPADES, TWO)
)))

hand5 = Hand(list((
    Card(DIAMONDS, TEN),
    Card(SPADES, NINE),
    Card(HEARTS, EIGHT),
    Card(DIAMONDS, SEVEN),
    Card(CLUBS, SIX)
)))

hand6 = Hand(list((
    Card(DIAMONDS, JACK),
    Card(DIAMONDS, NINE),
    Card(DIAMONDS, EIGHT),
    Card(DIAMONDS, FOUR),
    Card(DIAMONDS, THREE)
)))

hand7 = Hand(list((
    Card(SPADES, SIX),
    Card(HEARTS, SIX),
    Card(DIAMONDS, SIX),
    Card(CLUBS, KING),
    Card(DIAMONDS, KING)
)))

hand8 = Hand(list((
    Card(CLUBS, FIVE),
    Card(DIAMONDS, FIVE),
    Card(HEARTS, FIVE),
    Card(SPADES, FIVE),
    Card(CLUBS, TWO)
)))

hand9 = Hand(list((
    Card(CLUBS, JACK),
    Card(CLUBS, TEN),
    Card(CLUBS, NINE),
    Card(CLUBS, EIGHT),
    Card(CLUBS, SEVEN)
)))

wikihands = (
    (hand1, Hand.high_card),
    (hand2, Hand.one_pair),
    (hand3, Hand.two_pairs),
    (hand4, Hand.three_of_a_kind),
    (hand5, Hand.straight),
    (hand6, Hand.flush),
    (hand7, Hand.full_house),
    (hand8, Hand.four_of_a_kind),
    (hand9, Hand.straight_flush)
)

def test_best_hands():
    for worth, (hand, form) in enumerate(reversed(wikihands)):
        test_worth, test_form = Judge.best_of_hand(hand)
        assert test_worth == worth
        assert test_form == form

def test_simple_judges():
    for worth, (champion, _) in enumerate(wikihands[1:]):
        challengers = wikihands[:worth]
        for challenger, _ in challengers:
            assert Judge.judge(champion, challenger) == 'win'
            assert Judge.judge(challenger, champion) == 'loss'
