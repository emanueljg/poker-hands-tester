from dataclasses import dataclass, InitVar, field
from typing import Optional
from functools import total_ordering
import itertools


class DuplicateCardsException(Exception):
    pass


@dataclass(eq=True, frozen=True)
class Suit:
    name: str
    symbol: str

    def __str__(self) -> str:
        return self.symbol

@total_ordering
@dataclass(eq=True, frozen=True)
class Rank:
    _value: int
    name: str = None

    @property
    def value(self) -> int:
        # if None, it's a non-converted Ace.
        # assume high ace in that case.
        return self._value or 14

    def __str__(self) -> str:
        return self.name or str(self.value)

    def __lt__(self, other) -> bool:
        return self.value < other

    def __eq__(self, other) -> bool:
        return self.value == other


@total_ordering
@dataclass(eq=True, frozen=True)
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def value(self) -> int:
        return self.rank.value 

    def __lt__(self, other) -> bool:
        return self.value < other

    def __eq__(self, other) -> bool:
        return self.value == other
    
    @staticmethod
    def comp(x, y):
        if x > y: return True
        if x < y: return False
        else:     return None


@dataclass
class Hand:
    # to fix the potential issue of a hand being initialized
    # with duplicate cards, we need to guard against that.
    # But using a set fails silently. So what we end up doing
    # is INTERNALLY storing it as a set, but in the initializer
    # ask for a list so we can dupe check when converting it to a set.
    _cards: InitVar[list[Card]]
    cards: set[Card] = field(init=False)

    def __post_init__(self, _cards: list[Card]):
        cards_set = set(_cards)
        cards_list = _cards

        if len(cards_set) < len(cards_list): # has dupes!
            raise DuplicateCardsException

        self.cards = cards_set
    

    @property
    def asc_cards(self) -> list[Card]:
        return sorted(self.cards)

    @property
    def desc_cards(self) -> list[Card]:
        return sorted(self.cards, reverse=True)
    
    def __str__(self) -> str:
        return ', '.join(str(x) for x in self.cards)
    
    def _with_aces_value(self, new_value: Rank) -> Card:
        return Hand(set([
            Card(card.suit, new_value) 
                if card.rank == ACE  
                else card                   
            for card in self.cards        
        ]))

    def with_low_aces(self):
        return self._with_aces_value(ACE_ONE)
    
    def with_high_aces(self):
        return self._with_aces_value(ACE_FOURTEEN)

    def high_card(self) -> Card:
        hand = self.with_high_aces()
        return max(hand.cards, key=lambda c: c.rank.value)

    def _combinations(self, r):
        cards = self.with_high_aces().desc_cards
        combs = itertools.combinations(cards, r)
        return set(filter(lambda comb:
            all(comb[0].rank.value == card.rank.value for card in comb),
            combs
        ))

    @staticmethod
    def _combs_sort(combs):
        return tuple(sorted(combs, 
                      key=lambda comb: comb[0].value,
                      reverse=True))

    def pairs(self) -> set[tuple[Card]]:
        return self._combinations(2)

    def one_pair(self, pairs=None) -> tuple[Card]: 
        inner_pairs = pairs if pairs is not None else self.pairs()
        if inner_pairs:
            return max(inner_pairs, key=lambda p: p[0].value)

    def two_pairs(self) -> set[tuple[Card]]:
        pairs = self.pairs()
        if len(pairs) == 2:
            return Hand._combs_sort(pairs)

    def three_of_a_kind(self) -> tuple[Card]:
        return next(iter(self._combinations(3)), None)

    def _straight(self, hand) -> Optional[tuple[Card]]:
        cards = hand.asc_cards
        bottom, top = cards[0], cards[-1]
        if top.rank.value - bottom.rank.value == 4:
            return tuple(cards)

    def straight(self, introspect=False) -> Optional[tuple[Card]]:
        high_ace_straight = self._straight(self.with_high_aces())
        low_ace_straight = self._straight(self.with_low_aces())

        # standard
        if not introspect:
            return high_ace_straight or low_ace_straight

        # used when testing
        if introspect and high_ace_straight:
            return 'high-ace'
        if introspect and low_ace_straight and high_ace_straight:
            return 'no-ace'
        if introspect and low_ace_straight:
            return 'low-ace'
                                

    def flush(self) -> Optional[set[Card]]:
        suit = next(iter(self.cards)).suit
        if all(c.suit == suit for c in self.cards):
            return self.cards

    def full_house(self) -> Optional[tuple[Card]]:
        triple = self.three_of_a_kind()
        if triple:
            pair = self.one_pair(pairs=[
                p for p in self.pairs() if p[0].value != triple[0].value
            ])
            if pair: return triple, pair

    def four_of_a_kind(self) -> Optional[tuple[Card]]:
        return next(iter(self._combinations(4)), None)

    def straight_flush(self) -> Optional[tuple[Card]]:
        if (straight := self.straight()) and self.flush():
            return straight

    def __gt__(self, other):
        return Judge.judge(self, other) == 'win'


class Judge:

    def _j_single_comb(f, p, a):
        pcomb = f(p)[0]
        acomb = f(a)[0]

        if (cc := Card.comp(pcomb, acomb)) is not None:
            return cc
        else:
            return Judge.j_high_card(p, a)
        
    def j_straight_flush(p, a): 
        return Judge.j_straight(p, a)

    def j_four_of_a_kind(p, a): 
        return Judge._j_single_comb(Hand.four_of_a_kind, p, a)

    def j_full_house(p, a): 
        if (cc1 := Judge.j_three_of_a_kind(p, a)) is not None:
            return cc1
        elif (cc2 := Judge.j_one_pair(p, a)) is not None:
            return cc2
       
    def j_flush(p, a): 
        return Judge.j_high_card(p, a)

    def j_straight(p, a): 
        # this entire method SHOULD just be a simple high-card check,
        # but the fact that you can have both high and low straights requires
        # peeking into what kind of straight Hand.straight got, otherwise
        # we get a tie when we compare two hands that both have aces.
        # low ace straight is the worst possible straight so therefore
        # we set that card  to -1 to enforce lowest value
        ps = p.straight(introspect=True)
        # as is a reserved keyword
        _as = a.straight(introspect=True)
        
        pc = p.high_card() if ps != 'low-ace' else -1
        ac = a.high_card() if _as != 'low-ace' else -1  

        return Card.comp(pc, ac)

    def j_three_of_a_kind(p, a): 
        return Judge._j_single_comb(Hand.three_of_a_kind, p, a)

    def j_two_pairs(p, a):
        pp1, pp2 = p.two_pairs()      
        ap1, ap2 = a.two_pairs()

        cc1 = Card.comp(pp1[0], ap1[0])
        if cc1 is not None: return cc1
        cc2 = Card.comp(pp2[0], ap2[0])
        if cc2 is not None: return cc2

        return Judge.j_high_card(p, a)

    def j_one_pair(p, a): 
        return Judge._j_single_comb(Hand.one_pair, p, a)

    def j_high_card(p, a):
        for pc, ac in zip(p.desc_cards, a.desc_cards):
            if (cc := Card.comp(pc, ac)) is not None:
                return cc
        else:
            return None

    ORDER = {
        Hand.straight_flush:  j_straight_flush, 
        Hand.four_of_a_kind:  j_four_of_a_kind,
        Hand.full_house:      j_full_house,
        Hand.flush:           j_flush,
        Hand.straight:        j_straight,
        Hand.three_of_a_kind: j_three_of_a_kind,
        Hand.two_pairs:       j_two_pairs,
        Hand.one_pair:        j_one_pair,
        Hand.high_card:       j_high_card
    }

    def best_of_hand(hand: Hand): 
        for worth, form in enumerate(Judge.ORDER):
            if form(hand):
                return worth, form

    def judge(protag: Hand, antag: Hand):

        # dupe check
        p_len = len(protag.cards)
        a_len = len(antag.cards)
        pa_len = len(protag.cards | antag.cards)
        print(pa_len, p_len, a_len)
        if pa_len != (p_len + a_len):
            raise DuplicateCardsException
        
        p_worth, p_form = Judge.best_of_hand(protag)
        a_worth, a_form = Judge.best_of_hand(antag)
        if p_worth < a_worth: return 'win'
        elif p_worth > a_worth: return 'loss'
        else:  
            assert p_form == a_form
            result = Judge.ORDER[p_form](protag, antag)
            if result is None: return 'tie'
            elif result: return 'win'
            else: return 'loss'

SPADES   = Suit('Spades', '♠')
HEARTS   = Suit('Hearts', '♥')
DIAMONDS = Suit('Diamonds', '♦')
CLUBS    = Suit('Clubs', '♣')

ACE = Rank(None, 'Ace')
# not used normally
ACE_ONE = Rank(1, 'Ace1') 
ACE_FOURTEEN = Rank(14, 'Ace14')

TWO = Rank(2)
THREE = Rank(3)
FOUR = Rank(4)
FIVE = Rank(5)
SIX = Rank(6)
SEVEN = Rank(7)
EIGHT = Rank(8)
NINE = Rank(9)
TEN = Rank(10)
JACK = Rank(11, 'Jack')
QUEEN = Rank(12, 'Queen')
KING = Rank(13, 'King')

