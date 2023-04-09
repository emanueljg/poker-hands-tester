from main import *

def mk_tester(p, a, hand_type, check_for='win'):

    # bonus sanity check
    # if we are checking high card, f.e., we don't
    # want to accidentaly create a hand with a pair.
    assert Judge.best_of_hand(p)[1] == \
        Judge.best_of_hand(a)[1] == \
        hand_type

    # main check
    print(Judge.judge(p, a))
    assert Judge.judge(p, a) == check_for

    # add on inverse as a bonus if win-checking
    # (tie-check has no complement, obviously)
    if check_for == 'win':  
        assert Judge.judge(a, p) == 'loss'
