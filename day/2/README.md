# Solutions:

### All

    The dictionaries/maps used are essentially a schema for what should happen if a
    particular move is played by the opponent and the player.

    e.g.
        vals denotes the value of each move
        if the player plays 'A' (rock) then it is worth 1 point
        if the player plays 'B' (paper) then it is worth 2 point
        so on and so forth
        the format is =>
            value = vals[player's move]

        get_result denotes the score of the match
        if the opponent plays 'A' (rock)
        and the player plays 'Z' (scissors)
        then the player gets 0 points
        the format is =>
            score = get_result[opponent's move][player's move]

        in part 2, actions denotes the recommended action for the player to play
        if the opponent plays 'A' (rock)
        and the player's instruction is 'X' (lose)
        then the player should play 'Z' (scissors)
        the format is =>
            new move = actions[player's move][opponent's move]

    the program uses the dictionaries/maps in the same way shown above to calculate
    the score of each match and adds it to the sum.
