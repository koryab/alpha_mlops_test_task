import sys

sys.path.insert(0, './alpha_mlops_test_task')

from task_9 import randlist

def compete(player1, player2):
    STONE = 1
    SCISSORS = 2
    PAPER = 3

    score = [0, 0]
    for bets in zip(player1, player2):
        max_bet = max(bets)
        min_bet = min(bets)
        if bets[0] == bets[1]:
            score[0] += 1
            score[1] += 1
        elif min_bet == 1 and max_bet == 3:
            score[bets.index(min_bet)] += 1
        else:
            score[bets.index(max_bet)] += 1

    return score

def main():
    Ivan = randlist(10, 1, 3)
    Peter = randlist(10, 1, 3)
    score = compete(Ivan, Peter)
    result = f"{score[0]}:{score[1]}"
    if score[0] == score[1]:
        result = "5:5 ничья"
    elif score[0] == max(score):
        result += " победил Иван"
    else:
        result += " победил Петр"

    print(result)

if __name__ == "__main__":
    main()
