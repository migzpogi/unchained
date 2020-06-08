from ultraboost.euler.lib.deuces.Card import Card
from ultraboost.euler.lib.deuces.Evaluator import Evaluator
# sample input: 8C TS KC 9H 4S 7D 2S 5D 3S AC
# 376

def to_lower_second_char(hand):
    formatted = []
    for a in hand:
        formatted.append(a.capitalize())

    return formatted

with open('poker.txt', 'r') as f:
    p1_wins = 0
    for line in f.readlines():
        hands = line.strip().split(' ')
        p1 = to_lower_second_char(hands[0:5])
        p2 = to_lower_second_char(hands[5:10])

        hand = list(map(lambda c: Card.new(c), p1))
        evaluator = Evaluator()
        p1_score = evaluator.evaluate(cards=hand, board=[])
        p1_name = evaluator.class_to_string(evaluator.get_rank_class(p1_score))

        hand = list(map(lambda c: Card.new(c), p2))
        evaluator = Evaluator()
        p2_score = evaluator.evaluate(cards=hand, board=[])
        p2_name = evaluator.class_to_string(evaluator.get_rank_class(p2_score))

        if p1_score < p2_score:
            p1_wins += 1

    print(p1_wins)



