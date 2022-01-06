from dataclasses import dataclass
from typing import Tuple, Dict


def dirac_dice(player1_starting_position: int, player2_starting_position: int):
    player1_score = 0
    player2_score = 0
    player1_position = player1_starting_position
    player2_position = player2_starting_position
    die_rolls = 0
    while True:
        player1_move = die_rolls * 3 + 6
        die_rolls += 3
        player1_position += player1_move
        player1_position = mod_position(player1_position)
        player1_score += player1_position
        if player1_score >= 1000:
            return die_rolls, player2_score

        player2_move = die_rolls * 3 + 6
        die_rolls += 3
        player2_position += player2_move
        player2_position = mod_position(player2_position)
        player2_score += player2_position
        if player2_score >= 1000:
            return die_rolls, player1_score


def mod_position(position):
    return ((position - 1) % 10) + 1


@dataclass(frozen=True)
class GameState:
    next_player_pos: int
    other_player_pos: int
    next_player_remaining_score: int
    other_player_remaining_score: int


def dirac_quantum_dice_round(
        next_player_position: int,
        other_player_position: int,
        next_player_score_remaining: int,
        other_player_score_remaining: int,
        known_outcomes: Dict[GameState, Tuple[int, int]]
) -> Tuple[int, int]:
    current_state = GameState(next_player_position, other_player_position, next_player_score_remaining, other_player_score_remaining)
    if current_state in known_outcomes:
        return known_outcomes[current_state]
    if next_player_score_remaining <= 0:
        known_outcomes[current_state] = (1, 0)
        return 1, 0
    if other_player_score_remaining <= 0:
        known_outcomes[current_state] = (0, 1)
        return 0, 1

    universes_where_next_player_wins = 0
    universes_where_other_player_wins = 0
    for first_die in range(1, 4):
        for second_die in range(1, 4):
            for third_die in range(1, 4):
                move = first_die + second_die + third_die
                new_position = mod_position(next_player_position + move)
                new_score = next_player_score_remaining - new_position
                other_player_wins, this_player_wins = dirac_quantum_dice_round(
                    other_player_position,
                    new_position,
                    other_player_score_remaining,
                    new_score,
                    known_outcomes
                )
                universes_where_next_player_wins += this_player_wins
                universes_where_other_player_wins += other_player_wins
    known_outcomes[current_state] = (universes_where_next_player_wins, universes_where_other_player_wins)
    print(f"known outcomes: {len(known_outcomes)}")
    return universes_where_next_player_wins, universes_where_other_player_wins


def dirac_quantum_dice(player1_start_position: int, player2_start_position: int):
    return dirac_quantum_dice_round(player1_start_position, player2_start_position, 21, 21, dict())
