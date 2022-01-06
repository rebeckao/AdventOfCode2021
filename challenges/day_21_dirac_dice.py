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
