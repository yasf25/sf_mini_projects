#Просто эксперемент, который показывает, что играя в рулетку(исход50х50) и повышая каждый раз ставку х2 - то нрано или поздно человек все равно проиграет всё.
import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = (HEADS, TAILS)

def coinFlip():
    return random.choice(COIN_VALUES)


def play_do_konca(*, start_bank: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_money = start_bank
    current_bet = min_bet


    while current_money > 0:
        steps_to_loose += 1
        current_money -= current_bet
        brosaem_monety = coinFlip()

        if brosaem_monety == HEADS:
            win = current_bet * 2
            current_money += win
            current_bet = min_bet
        elif brosaem_monety == TAILS:

            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_money:
                current_bet = current_money


    return steps_to_loose


def simulator_for_n_players(
        *,
        start_bank: int,
        min_bet: int,
        max_bet: int,
        n_games: int
) -> float:
    total_steps_to_lose = 0
    for i in range(n_games):
        step_to_loose = play_do_konca(
            start_bank = start_bank,
            min_bet=min_bet,
            max_bet=max_bet
        )
        total_steps_to_lose += step_to_loose

        return total_steps_to_lose / n_games

print(simulator_for_n_players(n_games = 1, start_bank=10000000, min_bet=1, max_bet=10000000))
